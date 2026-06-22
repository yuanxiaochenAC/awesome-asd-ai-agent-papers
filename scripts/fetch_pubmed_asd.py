from __future__ import annotations

import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "data" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

QUERY = (
    '("autism spectrum disorder"[Title/Abstract] OR autism[Title/Abstract] OR autistic[Title/Abstract]) '
    'AND ("large language model"[Title/Abstract] OR LLM[Title/Abstract] OR GPT[Title/Abstract] '
    'OR agent[Title/Abstract] OR agentic[Title/Abstract] OR chatbot[Title/Abstract] '
    'OR multimodal[Title/Abstract] OR "machine learning"[Title/Abstract] OR "deep learning"[Title/Abstract]) '
    'AND ("2025/01/01"[Date - Publication] : "3000"[Date - Publication])'
)

AUTISM_TERMS = (
    "autism",
    "autistic",
    "autism spectrum disorder",
)

AI_TERMS = (
    "large language model",
    "llm",
    "gpt",
    "agent",
    "agentic",
    "chatbot",
    "multimodal",
    "machine learning",
    "deep learning",
)


def http_get(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "ASDAgentPapers/0.1"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def fetch_pmids() -> list[str]:
    params = {
        "db": "pubmed",
        "term": QUERY,
        "retmax": "100",
        "retmode": "xml",
        "sort": "pub date",
    }
    xml_text = http_get(f"{ESEARCH}?{urllib.parse.urlencode(params)}")
    root = ET.fromstring(xml_text)
    return [node.text for node in root.findall(".//Id") if node.text]


def fetch_summaries(pmids: list[str]) -> list[dict[str, object]]:
    if not pmids:
        return []
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    }
    xml_text = http_get(f"{ESUMMARY}?{urllib.parse.urlencode(params)}")
    root = ET.fromstring(xml_text)
    rows: list[dict[str, object]] = []
    for docsum in root.findall(".//DocSum"):
        pmid = docsum.findtext("Id", "")
        values = {item.get("Name"): item.text or "" for item in docsum.findall("Item")}
        title = values.get("Title", "")
        title_lower = title.lower()
        if not any(term in title_lower for term in AUTISM_TERMS):
            continue
        if not any(term in title_lower for term in AI_TERMS):
            continue
        rows.append(
            {
                "pmid": pmid,
                "title": title,
                "pubdate": values.get("PubDate", ""),
                "source": values.get("Source", ""),
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            }
        )
    return rows


def main() -> None:
    pmids = fetch_pmids()
    rows = fetch_summaries(pmids)
    path = OUTPUT_DIR / "pubmed_asd_candidates.json"
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} PubMed candidates to {path}")


if __name__ == "__main__":
    main()
