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

| Paper | Year | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- |
| [SocialWise: LLM-Agentic Conversation Therapy for Individuals with Autism Spectrum Disorder to Enhance Communication Skills](https://arxiv.org/abs/2604.15347v1) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2604.15347v1) / [PDF](https://arxiv.org/pdf/2604.15347v1.pdf) | Browser-based conversation therapy system with LLM role-play, retrieval, and structured communication feedback. |
| [NeuroWise: A Multi-Agent LLM Glass-Box System for Practicing Double-Empathy Communication with Autistic Partners](https://arxiv.org/abs/2602.18962) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2602.18962) / [PDF](https://arxiv.org/pdf/2602.18962.pdf) | Glass-box multi-agent communication training system grounded in the double-empathy framework. |
| [InterventionLens: A Multi-Agent Framework for Detecting ASD Intervention Strategies in Parent-Child Shared Reading](https://arxiv.org/abs/2603.13710v1) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2603.13710v1) / [PDF](https://arxiv.org/pdf/2603.13710v1.pdf) | Multi-agent video analysis framework for recognizing caregiver intervention strategies in home-based ASD reading sessions. |
| [From Synthesis to Clinical Assistance: A Strategy-Aware Agent Framework for Autism Intervention based on Real Clinical Dataset](https://arxiv.org/abs/2605.02916) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2605.02916) / [PDF](https://arxiv.org/pdf/2605.02916.pdf) | Strategy-aware autism intervention framework with specialized doctor and child agents for clinically grounded dialogue synthesis. |
| [A Proactive Multi-Agent Dialogue Framework for Assessing Social Language Disorder Traits in Autism](https://arxiv.org/abs/2605.22993v1) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2605.22993v1) / [PDF](https://arxiv.org/pdf/2605.22993v1.pdf) | Doctor and patient agents improve diagnostic coverage and efficiency for autism-related social language assessment. |
| [Human-mediated Large Language Models for Robotic Intervention in Children with Autism Spectrum Disorders](https://arxiv.org/abs/2402.00260v3) | 2024 | arXiv | [Paper](https://arxiv.org/abs/2402.00260v3) / [PDF](https://arxiv.org/pdf/2402.00260v3.pdf) | LLM-powered robot intervention pipeline for perspective-taking training in children with autism. |
| [A Virtual Conversational Agent for Teens with Autism: Experimental Results and Design Lessons](https://arxiv.org/abs/1811.03046v3) | 2018 | arXiv | [Paper](https://arxiv.org/abs/1811.03046v3) / [PDF](https://arxiv.org/pdf/1811.03046v3.pdf) | Early but still useful virtual-agent benchmark for private social-skills practice and feedback. |

## LLMs, Multi-Agent Systems, And Autism

| Paper | Year | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- |
| [When Machines Get It Wrong: Large Language Models Perpetuate Autism Myths More Than Humans Do](https://arxiv.org/abs/2601.22893v3) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2601.22893v3) / [PDF](https://arxiv.org/pdf/2601.22893v3.pdf) | Directly measures autism-myth endorsement and finds major knowledge fidelity gaps in frontier LLMs. |
| [NeuroMambaLLM: Dynamic Graph Learning of fMRI Functional Connectivity in Autistic Brains Using Mamba and Language Model Reasoning](https://arxiv.org/abs/2602.13770v3) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2602.13770v3) / [PDF](https://arxiv.org/pdf/2602.13770v3.pdf) | Combines dynamic brain connectivity modeling with language-model reasoning for autism-related neuroimaging analysis. |
| [Large Language Models as Simulative Agents for Neurodivergent Adult Psychometric Profiles](https://arxiv.org/abs/2601.15319v1) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2601.15319v1) / [PDF](https://arxiv.org/pdf/2601.15319v1.pdf) | Tests whether LLMs can simulate neurodivergent psychometric responses with useful fidelity. |
| [Exploring Implicit Perspectives on Autism in Large Language Models Through Multi-Agent Simulations](https://arxiv.org/abs/2601.15437) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2601.15437) / [PDF](https://arxiv.org/pdf/2601.15437.pdf) | Multi-agent simulations expose how LLMs implicitly frame autistic and non-autistic social interaction. |
| [Affordances and Risks of ChatGPT to Autistic Users](https://arxiv.org/abs/2601.17946) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2601.17946) / [PDF](https://arxiv.org/pdf/2601.17946.pdf) | Examines the practical benefits and risks autistic users report when using ChatGPT in daily life. |
| ["Are we writing an advice column for Spock here?" Understanding Stereotypes in AI Advice for Autistic Users](https://arxiv.org/abs/2601.12690v1) | 2026 | arXiv | [Paper](https://arxiv.org/abs/2601.12690v1) / [PDF](https://arxiv.org/pdf/2601.12690v1.pdf) | Large-scale audit of how disclosure of autism changes LLM advice and can trigger stereotyped recommendations. |
| [NeuroBridge: Using Generative AI to Bridge Cross-neurotype Communication Differences through Neurotypical Perspective-taking](https://arxiv.org/abs/2509.23434v1) | 2025 | arXiv | [Paper](https://arxiv.org/abs/2509.23434v1) / [PDF](https://arxiv.org/pdf/2509.23434v1.pdf) | Generative AI platform for helping neurotypical users experience and reflect on autistic communication styles. |

## Latest ASD Medical And Clinical AI Papers

| Paper | Year | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- |
| [ScreeningPaL: LLM-NLP Enabled Early Autism Detection Method from Caregiver's Free-Text Input](https://pubmed.ncbi.nlm.nih.gov/42317820/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42317820/) | Uses free-text caregiver descriptions with LLM-NLP methods to support early autism detection. |
| [Safety-Constrained Agentic AI for Autism Screening: A Multimodal, Clinician-Guided Architecture](https://pubmed.ncbi.nlm.nih.gov/42306396/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42306396/) | Clinician-guided agentic architecture aimed at safer multimodal autism screening workflows. |
| [Parents' perspectives on the use of artificial intelligence chatbots to promote physical activity among individuals with autism spectrum disorder](https://pubmed.ncbi.nlm.nih.gov/42301801/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42301801/) | Useful applied paper on caregiver acceptance of AI chatbots for autism-support routines. |
| [Multimodal behavioral analysis of child play interactions for early detection of Autism Spectrum Disorder](https://pubmed.ncbi.nlm.nih.gov/42263387/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42263387/) | Recent multimodal behavioral study for early ASD detection in naturalistic play settings. |
| [Multimodal Data Integration for Early Autism Detection and LLM-Assisted Intervention Planning](https://pubmed.ncbi.nlm.nih.gov/41797112/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41797112/) | Combines multimodal early detection with LLM-assisted planning for downstream intervention decisions. |
| [Machine Learning Algorithms for Detection of Autism Spectrum Disorders in Early Childhood: A Scoping Review](https://pubmed.ncbi.nlm.nih.gov/41910220/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41910220/) | Broad review of machine-learning approaches for early-childhood autism detection. |
| [GPT-Powered Chatbot-Based Positive Psychology Intervention for Parents of Autistic Children](https://pubmed.ncbi.nlm.nih.gov/41802236/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41802236/) | Chatbot intervention study focused on supporting parents of autistic children. |
| [Functional near-infrared spectroscopy-based machine learning techniques for autism spectrum disorder diagnosis: a systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/42296703/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42296703/) | Meta-analysis of machine-learning diagnosis pipelines using fNIRS for ASD detection. |
| [Autism Detection Based on Computational Analysis of Parental Speech](https://pubmed.ncbi.nlm.nih.gov/41696837/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41696837/) | Computational speech analysis approach for autism screening using parental-language signals. |
| [Accuracy of Autism-Related TikTok Information in Italian: A Comparison Between Human Raters and Large Language Models](https://pubmed.ncbi.nlm.nih.gov/41706307/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41706307/) | Benchmarks whether human reviewers and LLMs can reliably judge autism-related health information quality. |
| [A PATE-to-MedPrompt System for Autism Detection](https://pubmed.ncbi.nlm.nih.gov/42121994/) | 2026 | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42121994/) | Medical prompting pipeline for autism detection from symptom-centered narratives. |

## Notes

- This repository is designed as a curated reading list, not a fully automatic ranking system.
- PubMed and arXiv queries are intentionally broad; manual review is expected before publishing updates.
