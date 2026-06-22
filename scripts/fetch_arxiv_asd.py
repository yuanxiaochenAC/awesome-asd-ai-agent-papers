from __future__ import annotations

import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ARXIV_API = "http://export.arxiv.org/api/query"
ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}

QUERY = (
    '(all:autism OR all:"autism spectrum disorder" OR all:asd) AND '
    '(all:agent OR all:agentic OR all:"multi-agent" OR all:llm OR all:"large language model")'
)

AUTISM_TERMS = (
    "autism",
    "autistic",
    "autism spectrum disorder",
)

AGENT_TERMS = (
    "agent",
    "agentic",
    "multi-agent",
    "llm",
    "large language model",
    "chatbot",
)

EXCLUDE_TERMS = (
    "architectural smell density",
    "active speaker detection",
    "target speech extraction",
)


def fetch_xml() -> str:
    params = {
        "search_query": QUERY,
        "start": "0",
        "max_results": "100",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "ASDAgentPapers/0.1"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def parse_feed(xml_text: str) -> list[dict[str, object]]:
    root = ET.fromstring(xml_text)
    rows: list[dict[str, object]] = []
    for entry in root.findall("atom:entry", ARXIV_NS):
        entry_id = entry.findtext("atom:id", "", ARXIV_NS).rstrip("/")
        paper_id = entry_id.rsplit("/", maxsplit=1)[-1]
        title = " ".join(entry.findtext("atom:title", "", ARXIV_NS).split())
        summary = " ".join(entry.findtext("atom:summary", "", ARXIV_NS).split())
        text = f"{title} {summary}".lower()
        if not any(term in text for term in AUTISM_TERMS):
            continue
        if not any(term in text for term in AGENT_TERMS):
            continue
        if any(term in text for term in EXCLUDE_TERMS):
            continue
        rows.append(
            {
                "paper_id": paper_id,
                "title": title,
                "summary": summary,
                "published": entry.findtext("atom:published", "", ARXIV_NS),
                "url": f"https://arxiv.org/abs/{paper_id}",
                "pdf_url": f"https://arxiv.org/pdf/{paper_id}.pdf",
            }
        )
    return rows


def main() -> None:
    xml_text = fetch_xml()
    rows = parse_feed(xml_text)
    path = OUTPUT_DIR / "arxiv_asd_candidates.json"
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} arXiv candidates to {path}")


if __name__ == "__main__":
    main()
