# Awesome ASD AI Agent Papers

Curated project for:

- AI agent applications in autism spectrum disorder (ASD)
- LLM and multi-agent systems used in ASD support, intervention, and communication
- latest ASD medical and clinical AI papers

Inspired by projects like [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers),
but specialized for the ASD domain.

## What This Repository Covers

- AI agent systems for autism intervention, screening, communication, and therapy support
- LLM, multi-agent, chatbot, and agentic workflows designed for autistic users or ASD clinical settings
- recent ASD medical and clinical AI papers with practical relevance

## Quick Start

```bash
python scripts/fetch_arxiv_asd.py
python scripts/fetch_pubmed_asd.py
python scripts/build_readme.py
```

Generated candidate files are written to `data/generated/`.

## Scope

- Agent systems for autism intervention, therapy support, social practice, and education
- Autism-focused LLM evaluation, safety, and bias papers
- Recent ASD medical and clinical papers involving AI, LLMs, multimodal modeling, or decision support

## Sources

- arXiv
- PubMed
- curated GitHub paper lists

## Update Workflow

- Use `scripts/fetch_arxiv_asd.py` to collect ASD + AI agent arXiv candidates
- Use `scripts/fetch_pubmed_asd.py` to collect ASD medical PubMed candidates
- Review and merge good candidates into `data/seed_papers.json`
- Run `scripts/build_readme.py` to regenerate this README

## Repository Structure

- `README.md`: published paper list
- `data/seed_papers.json`: curated source of truth
- `data/generated/`: raw candidate outputs from source collectors
- `scripts/fetch_arxiv_asd.py`: arXiv collector
- `scripts/fetch_pubmed_asd.py`: PubMed collector
- `scripts/build_readme.py`: README generator

## AI Agent Applications In ASD

- [SocialWise: LLM-Agentic Conversation Therapy for Individuals with Autism](https://arxiv.org/abs/2604.15347) (arXiv, 2026): Conversation-therapy chatbot for autistic users with role-play, knowledge retrieval, and feedback agents.
- [NeuroWise: A Multi-Agent LLM Glass-Box System for Practicing Double-Empathy Communication with Autistic Partners](https://arxiv.org/abs/2602.18962) (arXiv, 2026): Multi-agent LLM system for practicing autism-aware communication grounded in the double-empathy framework.
- [From Synthesis to Clinical Assistance: A Strategy-Aware Agent Framework for Autism Intervention based on Real Clinical Dataset](https://arxiv.org/abs/2605.02916) (arXiv, 2026): Strategy-aware ASD intervention framework with DoctorAgent and ChildAgent for ABA-aligned dialogue synthesis and clinical decision support.

## LLMs, Multi-Agent Systems, And Autism

- [When Machines Get It Wrong: Large Language Models Perpetuate Autism Myths More Than Humans Do](https://arxiv.org/abs/2601.22893) (arXiv, 2026): Benchmarks autism-myth endorsement and shows LLMs underperform humans on autism knowledge fidelity.
- [Exploring Implicit Perspectives on Autism in Large Language Models Through Multi-Agent Simulations](https://arxiv.org/abs/2601.15437) (arXiv, 2026): Uses multi-agent simulations to study implicit autism-related bias and assumptions in LLM behavior.
- [Affordances and Risks of ChatGPT to Autistic Users](https://arxiv.org/abs/2601.17946) (arXiv, 2026): Examines utility and risk patterns of ChatGPT for autistic users from real-world use narratives.

## Latest ASD Medical And Clinical AI Papers

- [Multimodal Data Integration for Early Autism Detection and LLM-Assisted Intervention Planning](https://pubmed.ncbi.nlm.nih.gov/41797112/) (PubMed, 2026): Discusses multimodal early ASD detection and the role of LLMs in intervention planning.
- [GPT-Powered Chatbot-Based Positive Psychology Intervention for Parents of Autistic Children](https://pubmed.ncbi.nlm.nih.gov/41802236/) (PubMed, 2026): Explores a culturally adapted chatbot intervention for parents of autistic children.
- [Autism Detection Based on Computational Analysis of Parental Speech](https://pubmed.ncbi.nlm.nih.gov/41696837/) (PubMed, 2026): Computational analysis pipeline for ASD detection from parents' speech patterns.
- [Accuracy of Autism-Related TikTok Information in Italian: A Comparison Between Human Raters and Large Language Models](https://pubmed.ncbi.nlm.nih.gov/41706307/) (PubMed, 2026): Compares human and LLM assessment quality for autism-related short-video information.
- [A PATE-to-MedPrompt System for Autism Detection](https://pubmed.ncbi.nlm.nih.gov/42121994/) (PubMed, 2026): LLM-based autism detection pipeline using symptom narratives and medical prompting.

## Notes

- This repository is designed as a curated reading list, not a fully automatic ranking system.
- PubMed and arXiv queries are intentionally broad; manual review is expected before publishing updates.
