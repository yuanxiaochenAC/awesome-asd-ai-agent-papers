from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "seed_papers.json"
README_PATH = ROOT / "README.md"

SECTIONS = [
    ("agent_applications", "AI Agent Applications In ASD"),
    ("llm_autism", "LLMs, Multi-Agent Systems, And Autism"),
    ("medical_ai", "Latest ASD Medical And Clinical AI Papers"),
]


def load_items() -> list[dict[str, object]]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def format_access(item: dict[str, object]) -> str:
    access = [f"[Paper]({item['paper_url']})"]
    download_url = item.get("download_url")
    if download_url:
        access.append(f"[PDF]({download_url})")
    return " / ".join(access)


def render_section(items: list[dict[str, object]], section_key: str, title: str) -> list[str]:
    lines = [
        f"## {title}",
        "",
        "| Paper | Year | Source | Access | Why It Matters |",
        "| --- | --- | --- | --- | --- |",
    ]
    section_items = [item for item in items if item["section"] == section_key]
    for item in sorted(section_items, key=lambda row: (row["year"], row["title"]), reverse=True):
        title_cell = f"[{item['title']}]({item['paper_url']})"
        lines.append(
            f"| {title_cell} | {item['year']} | {item['source']} | {format_access(item)} | {item['note']} |"
        )
    lines.append("")
    return lines


def render_readme(items: list[dict[str, object]]) -> str:
    lines = [
        "# Awesome ASD AI Agent Papers",
        "",
        "Curated project for:",
        "",
        "- AI agent applications in autism spectrum disorder (ASD)",
        "- LLM and multi-agent systems used in ASD support, intervention, and communication",
        "- latest ASD medical and clinical AI papers",
        "",
        "Inspired by projects like [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers),",
        "but specialized for the ASD domain.",
        "",
        "## What This Repository Covers",
        "",
        "- AI agent systems for autism intervention, screening, communication, and therapy support",
        "- LLM, multi-agent, chatbot, and agentic workflows designed for autistic users or ASD clinical settings",
        "- recent ASD medical and clinical AI papers with practical relevance",
        "",
        "## Quick Start",
        "",
        "```bash",
        "python scripts/fetch_arxiv_asd.py",
        "python scripts/fetch_pubmed_asd.py",
        "python scripts/build_readme.py",
        "```",
        "",
        "Generated candidate files are written to `data/generated/`.",
        "",
        "## Scope",
        "",
        "- Agent systems for autism intervention, therapy support, social practice, and education",
        "- Autism-focused LLM evaluation, safety, and bias papers",
        "- Recent ASD medical and clinical papers involving AI, LLMs, multimodal modeling, or decision support",
        "",
        "## Sources",
        "",
        "- arXiv",
        "- PubMed",
        "- curated GitHub paper lists",
        "",
        "## Update Workflow",
        "",
        "- Use `scripts/fetch_arxiv_asd.py` to collect ASD + AI agent arXiv candidates",
        "- Use `scripts/fetch_pubmed_asd.py` to collect ASD medical PubMed candidates",
        "- Review and merge good candidates into `data/seed_papers.json`",
        "- Run `scripts/build_readme.py` to regenerate this README",
        "",
        "## Repository Structure",
        "",
        "- `README.md`: published paper list",
        "- `data/seed_papers.json`: curated source of truth",
        "- `data/generated/`: raw candidate outputs from source collectors",
        "- `scripts/fetch_arxiv_asd.py`: arXiv collector",
        "- `scripts/fetch_pubmed_asd.py`: PubMed collector",
        "- `scripts/build_readme.py`: README generator",
        "",
    ]
    for section_key, title in SECTIONS:
        lines.extend(render_section(items, section_key, title))

    lines.extend(
        [
            "## Notes",
            "",
            "- This repository is designed as a curated reading list, not a fully automatic ranking system.",
            "- PubMed and arXiv queries are intentionally broad; manual review is expected before publishing updates.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    items = load_items()
    README_PATH.write_text(render_readme(items), encoding="utf-8")
    print(f"README updated: {README_PATH}")


if __name__ == "__main__":
    main()
