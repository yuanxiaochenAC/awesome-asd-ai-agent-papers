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
    ("evolving_methods", "General Capabilities Helpful For ASD AI Agents: Self-Evolving, Reflection, And Prompt Optimization"),
    ("skills_workflows", "General Capabilities Helpful For ASD AI Agents: Skills, Tool-Use, And Workflow"),
    ("memory_systems", "General Capabilities Helpful For ASD AI Agents: Memory And Long-Horizon Ability"),
    ("other_agentic_methods", "General Capabilities Helpful For ASD AI Agents: Recommendation, Collaboration, And Other Agentic Methods"),
]

SECTION_DESCRIPTIONS = {
    "agent_applications": "Direct ASD applications: intervention, communication practice, screening, and caregiver support.",
    "llm_autism": "LLM and multi-agent studies about autism, neurodiversity, bias, and human-AI interaction.",
    "medical_ai": "Clinical and medical AI evidence relevant to ASD detection, assessment, intervention, and deployment.",
    "evolving_methods": "Self-evolution, reflection, prompt optimization, and feedback loops that can improve ASD agents over time.",
    "skills_workflows": "Reusable skills, tool use, orchestration, and workflow design for reliable ASD agent operation.",
    "memory_systems": "Memory, personalization, long-horizon context, and governed state for continuous ASD support.",
    "other_agentic_methods": "Additional agent architectures, collaboration, routing, evaluation, and safety methods with domain-transfer value.",
}


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
        SECTION_DESCRIPTIONS[section_key],
        "",
        "| Paper | Year | Type | Source | Access | Why It Matters |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    section_items = [item for item in items if item["section"] == section_key]
    for item in sorted(section_items, key=lambda row: (row["year"], row["title"]), reverse=True):
        title_cell = f"[{item['title']}]({item['paper_url']})"
        type_cell = item.get("category", "ASD-specific")
        lines.append(
            f"| {title_cell} | {item['year']} | {type_cell} | {item['source']} | {format_access(item)} | {item['note']} |"
        )
    lines.append("")
    return lines


def render_readme(items: list[dict[str, object]]) -> str:
    count = len(items)
    section_counts = {key: sum(item["section"] == key for item in items) for key, _ in SECTIONS}
    lines = [
        "# Awesome ASD AI Agent Papers",
        "",
        f"[![Papers](https://img.shields.io/badge/papers-{count}-1f6feb.svg)](data/seed_papers.json) "
        "[![Focus](https://img.shields.io/badge/focus-ASD%20%2B%20AI%20Agents-0f766e.svg)](#scope) "
        "[![Sources](https://img.shields.io/badge/sources-arXiv%20%7C%20PubMed-b45309.svg)](#sources) "
        "[![License](https://img.shields.io/badge/license-MIT-111827.svg)](LICENSE)",
        "",
        "> A curated research map for building safer, more useful AI agents for autism spectrum disorder (ASD).",
        "",
        "This list connects ASD-specific evidence with the general agent capabilities that can make an ASD system more reliable: memory, skills, workflow orchestration, reflection, evaluation, and safe self-improvement.",
        "",
        "![The evolution landscape of AI agents](assets/agent-evolution-landscape.png)",
        "",
        "<p align=\"center\"><em>General agent capability layers provide reusable methods; the ASD sections provide the domain evidence and safety context.</em></p>",
        "",
        "## Navigation",
        "",
        "| Layer | Papers | What to read for |",
        "| --- | ---: | --- |",
    ]
    for key, title in SECTIONS:
        lines.append(f"| [{title}](#{key.replace('_', '-')}) | {section_counts[key]} | {SECTION_DESCRIPTIONS[key]} |")
    lines.extend(
        [
            "",
            "## Reading Paths",
            "",
            "- **Build an ASD intervention agent:** start with `AI Agent Applications In ASD`, then read `Memory And Long-Horizon Ability` and `Skills, Tool-Use, And Workflow`.",
            "- **Study clinical reliability:** start with `Latest ASD Medical And Clinical AI Papers`, then compare `LLMs, Multi-Agent Systems, And Autism` for bias, evidence quality, and neurodiversity-affirming design.",
            "- **Design an improving agent:** start with `Self-Evolving, Reflection, And Prompt Optimization`, then add governed memory and evaluation methods before considering autonomous updates.",
            "",
            "## Scope",
            "",
            "- AI agent systems for autism intervention, screening, communication, therapy support, and caregiver assistance",
            "- LLM, multi-agent, chatbot, and agentic workflows designed for autistic users or ASD clinical settings",
            "- Recent ASD medical and clinical AI papers involving AI, LLMs, multimodal modeling, or decision support",
            "- General agent methods selected for clear transfer value to ASD systems, not because they mention ASD directly",
            "",
            "## Curation Principles",
            "",
            "- Each entry has a stable paper link and a short neutral note about its practical relevance.",
            "- ASD-specific evidence and transferable agent methods are kept in separate layers.",
            "- Medical papers are research references, not clinical advice or validated diagnostic recommendations.",
            "- Broad source queries are manually reviewed before inclusion; duplicate titles are removed.",
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
            "## Sources",
            "",
            "- [arXiv](https://arxiv.org/)",
            "- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)",
            "- [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers)",
            "- [masamasa59/ai-agent-papers](https://github.com/masamasa59/ai-agent-papers)",
            "- [ANative-Lab/Awesome-Self-Evolving-Agents](https://github.com/ANative-Lab/Awesome-Self-Evolving-Agents)",
            "",
            "## Update Workflow",
            "",
            "1. Run the arXiv and PubMed collectors to create candidate files.",
            "2. Check the curated agent lists for new capability-layer papers.",
            "3. Review titles, dates, links, and ASD transfer value before editing `data/seed_papers.json`.",
            "4. Run `python scripts/build_readme.py` and verify the generated tables.",
            "",
            "## Repository Structure",
            "",
            "- `README.md`: published research map and tables",
            "- `data/seed_papers.json`: curated source of truth",
            "- `data/generated/`: raw candidate outputs from source collectors",
            "- `assets/agent-evolution-landscape.png`: capability evolution overview figure",
            "- `scripts/fetch_arxiv_asd.py`: arXiv collector",
            "- `scripts/fetch_pubmed_asd.py`: PubMed collector",
            "- `scripts/build_readme.py`: README generator",
            "",
        ]
    )
    for section_key, title in SECTIONS:
        lines.extend(render_section(items, section_key, title))

    lines.extend(
        [
            "## Notes",
            "",
            "- This repository is a curated reading list, not a fully automatic ranking system.",
            "- PubMed and arXiv queries are intentionally broad; manual review is expected before publishing updates.",
            "- The evolution landscape figure is a general-agent reference map; it is not an ASD-specific evidence figure.",
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
