# Contributing

This repository is intentionally lightweight. The goal is to keep a high-signal paper list for:

- AI agent applications in ASD
- LLM and multi-agent autism research
- recent ASD medical and clinical AI papers

## Update Steps

1. Run `python scripts/fetch_arxiv_asd.py`
2. Run `python scripts/fetch_pubmed_asd.py`
3. Review files under `data/generated/`
4. Add accepted papers into `data/seed_papers.json`
5. Run `python scripts/build_readme.py`

## Inclusion Rules

- Prefer papers published in 2025 or 2026
- Prefer papers with direct ASD or autism relevance
- Prefer papers with clear AI, LLM, multi-agent, chatbot, multimodal, or clinical decision-support content
- Exclude papers where `ASD` means something unrelated to autism
- Keep notes short and factual

## Style

- Use title case for section headings
- Link to `arXiv abs` or `PubMed` pages
- Keep one-line descriptions under 30 words when possible
