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

| Paper | Year | Type | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| [SocialWise: LLM-Agentic Conversation Therapy for Individuals with Autism Spectrum Disorder to Enhance Communication Skills](https://arxiv.org/abs/2604.15347v1) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2604.15347v1) / [PDF](https://arxiv.org/pdf/2604.15347v1.pdf) | Browser-based conversation therapy system with LLM role-play, retrieval, and structured communication feedback. |
| [NeuroWise: A Multi-Agent LLM Glass-Box System for Practicing Double-Empathy Communication with Autistic Partners](https://arxiv.org/abs/2602.18962) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2602.18962) / [PDF](https://arxiv.org/pdf/2602.18962.pdf) | Glass-box multi-agent communication training system grounded in the double-empathy framework. |
| [InterventionLens: A Multi-Agent Framework for Detecting ASD Intervention Strategies in Parent-Child Shared Reading](https://arxiv.org/abs/2603.13710v1) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2603.13710v1) / [PDF](https://arxiv.org/pdf/2603.13710v1.pdf) | Multi-agent video analysis framework for recognizing caregiver intervention strategies in home-based ASD reading sessions. |
| [From Synthesis to Clinical Assistance: A Strategy-Aware Agent Framework for Autism Intervention based on Real Clinical Dataset](https://arxiv.org/abs/2605.02916) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2605.02916) / [PDF](https://arxiv.org/pdf/2605.02916.pdf) | Strategy-aware autism intervention framework with specialized doctor and child agents for clinically grounded dialogue synthesis. |
| [A Proactive Multi-Agent Dialogue Framework for Assessing Social Language Disorder Traits in Autism](https://arxiv.org/abs/2605.22993v1) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2605.22993v1) / [PDF](https://arxiv.org/pdf/2605.22993v1.pdf) | Doctor and patient agents improve diagnostic coverage and efficiency for autism-related social language assessment. |
| [Human-mediated Large Language Models for Robotic Intervention in Children with Autism Spectrum Disorders](https://arxiv.org/abs/2402.00260v3) | 2024 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2402.00260v3) / [PDF](https://arxiv.org/pdf/2402.00260v3.pdf) | LLM-powered robot intervention pipeline for perspective-taking training in children with autism. |
| [A Virtual Conversational Agent for Teens with Autism: Experimental Results and Design Lessons](https://arxiv.org/abs/1811.03046v3) | 2018 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/1811.03046v3) / [PDF](https://arxiv.org/pdf/1811.03046v3.pdf) | Early but still useful virtual-agent benchmark for private social-skills practice and feedback. |

## LLMs, Multi-Agent Systems, And Autism

| Paper | Year | Type | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| [When Machines Get It Wrong: Large Language Models Perpetuate Autism Myths More Than Humans Do](https://arxiv.org/abs/2601.22893v3) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2601.22893v3) / [PDF](https://arxiv.org/pdf/2601.22893v3.pdf) | Directly measures autism-myth endorsement and finds major knowledge fidelity gaps in frontier LLMs. |
| [NeuroMambaLLM: Dynamic Graph Learning of fMRI Functional Connectivity in Autistic Brains Using Mamba and Language Model Reasoning](https://arxiv.org/abs/2602.13770v3) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2602.13770v3) / [PDF](https://arxiv.org/pdf/2602.13770v3.pdf) | Combines dynamic brain connectivity modeling with language-model reasoning for autism-related neuroimaging analysis. |
| [Large Language Models as Simulative Agents for Neurodivergent Adult Psychometric Profiles](https://arxiv.org/abs/2601.15319v1) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2601.15319v1) / [PDF](https://arxiv.org/pdf/2601.15319v1.pdf) | Tests whether LLMs can simulate neurodivergent psychometric responses with useful fidelity. |
| [Exploring Implicit Perspectives on Autism in Large Language Models Through Multi-Agent Simulations](https://arxiv.org/abs/2601.15437) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2601.15437) / [PDF](https://arxiv.org/pdf/2601.15437.pdf) | Multi-agent simulations expose how LLMs implicitly frame autistic and non-autistic social interaction. |
| [Affordances and Risks of ChatGPT to Autistic Users](https://arxiv.org/abs/2601.17946) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2601.17946) / [PDF](https://arxiv.org/pdf/2601.17946.pdf) | Examines the practical benefits and risks autistic users report when using ChatGPT in daily life. |
| ["Are we writing an advice column for Spock here?" Understanding Stereotypes in AI Advice for Autistic Users](https://arxiv.org/abs/2601.12690v1) | 2026 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2601.12690v1) / [PDF](https://arxiv.org/pdf/2601.12690v1.pdf) | Large-scale audit of how disclosure of autism changes LLM advice and can trigger stereotyped recommendations. |
| [NeuroBridge: Using Generative AI to Bridge Cross-neurotype Communication Differences through Neurotypical Perspective-taking](https://arxiv.org/abs/2509.23434v1) | 2025 | ASD-specific | arXiv | [Paper](https://arxiv.org/abs/2509.23434v1) / [PDF](https://arxiv.org/pdf/2509.23434v1.pdf) | Generative AI platform for helping neurotypical users experience and reflect on autistic communication styles. |

## Latest ASD Medical And Clinical AI Papers

| Paper | Year | Type | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| [ScreeningPaL: LLM-NLP Enabled Early Autism Detection Method from Caregiver's Free-Text Input](https://pubmed.ncbi.nlm.nih.gov/42317820/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42317820/) | Uses free-text caregiver descriptions with LLM-NLP methods to support early autism detection. |
| [Safety-Constrained Agentic AI for Autism Screening: A Multimodal, Clinician-Guided Architecture](https://pubmed.ncbi.nlm.nih.gov/42306396/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42306396/) | Clinician-guided agentic architecture aimed at safer multimodal autism screening workflows. |
| [Parents' perspectives on the use of artificial intelligence chatbots to promote physical activity among individuals with autism spectrum disorder](https://pubmed.ncbi.nlm.nih.gov/42301801/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42301801/) | Useful applied paper on caregiver acceptance of AI chatbots for autism-support routines. |
| [Multimodal behavioral analysis of child play interactions for early detection of Autism Spectrum Disorder](https://pubmed.ncbi.nlm.nih.gov/42263387/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42263387/) | Recent multimodal behavioral study for early ASD detection in naturalistic play settings. |
| [Multimodal Data Integration for Early Autism Detection and LLM-Assisted Intervention Planning](https://pubmed.ncbi.nlm.nih.gov/41797112/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41797112/) | Combines multimodal early detection with LLM-assisted planning for downstream intervention decisions. |
| [Machine Learning Algorithms for Detection of Autism Spectrum Disorders in Early Childhood: A Scoping Review](https://pubmed.ncbi.nlm.nih.gov/41910220/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41910220/) | Broad review of machine-learning approaches for early-childhood autism detection. |
| [GPT-Powered Chatbot-Based Positive Psychology Intervention for Parents of Autistic Children](https://pubmed.ncbi.nlm.nih.gov/41802236/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41802236/) | Chatbot intervention study focused on supporting parents of autistic children. |
| [Functional near-infrared spectroscopy-based machine learning techniques for autism spectrum disorder diagnosis: a systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/42296703/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42296703/) | Meta-analysis of machine-learning diagnosis pipelines using fNIRS for ASD detection. |
| [Autism Detection Based on Computational Analysis of Parental Speech](https://pubmed.ncbi.nlm.nih.gov/41696837/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41696837/) | Computational speech analysis approach for autism screening using parental-language signals. |
| [Accuracy of Autism-Related TikTok Information in Italian: A Comparison Between Human Raters and Large Language Models](https://pubmed.ncbi.nlm.nih.gov/41706307/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/41706307/) | Benchmarks whether human reviewers and LLMs can reliably judge autism-related health information quality. |
| [A PATE-to-MedPrompt System for Autism Detection](https://pubmed.ncbi.nlm.nih.gov/42121994/) | 2026 | ASD-specific | PubMed | [Paper](https://pubmed.ncbi.nlm.nih.gov/42121994/) | Medical prompting pipeline for autism detection from symptom-centered narratives. |

## General Capabilities Helpful For ASD AI Agents: Self-Evolving, Reflection, And Prompt Optimization

| Paper | Year | Type | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| [Tree-based Credit Assignment for Multi-Agent Memory System](https://arxiv.org/abs/2605.04811v1) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2605.04811v1) / [PDF](https://arxiv.org/pdf/2605.04811v1.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [Towards AGI A Pragmatic Approach Towards Self Evolving Agent](https://arxiv.org/abs/2601.11658) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.11658) / [PDF](https://arxiv.org/pdf/2601.11658.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [ST-EVO:TowardsGenerativeSpatio-TemporalEvolutionof Multi-AgentCommunicationTopologies](https://arxiv.org/abs/2602.14681) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2602.14681) / [PDF](https://arxiv.org/pdf/2602.14681.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [SHIELD: An Auto-Healing Agentic Defense Framework for LLM Resource Exhaustion Attacks](https://arxiv.org/abs/2601.19174) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.19174) / [PDF](https://arxiv.org/pdf/2601.19174.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [PRISMA: Reinforcement Learning Guided Two-Stage Policy Optimization in Multi-Agent Architecture for Open-Domain Multi-Hop QA](https://arxiv.org/abs/2601.05465) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.05465) / [PDF](https://arxiv.org/pdf/2601.05465.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning](https://arxiv.org/abs/2601.06794) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.06794) / [PDF](https://arxiv.org/pdf/2601.06794.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/abs/2601.21557) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.21557) / [PDF](https://arxiv.org/pdf/2601.21557.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux](https://arxiv.org/abs/2601.13060) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.13060) / [PDF](https://arxiv.org/pdf/2601.13060.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.06623) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2605.06623) / [PDF](https://arxiv.org/pdf/2605.06623.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization](https://arxiv.org/abs/2604.20714) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2604.20714) / [PDF](https://arxiv.org/pdf/2604.20714.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [From Self-Evolving Synthetic Data to Verifiable-Reward RL: Post-Training Multi-turn Interactive Tool-Using Agents](https://arxiv.org/abs/2601.22607) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.22607) / [PDF](https://arxiv.org/pdf/2601.22607.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [Experiential Reflective Learning for Self-Improving LLM Agents](https://arxiv.org/abs/2603.24639) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2603.24639) / [PDF](https://arxiv.org/pdf/2603.24639.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [Evolutionary Generation of Multi-Agent Systems](https://arxiv.org/abs/2602.06511) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2602.06511) / [PDF](https://arxiv.org/pdf/2602.06511.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems](https://arxiv.org/abs/2605.08769v1) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2605.08769v1) / [PDF](https://arxiv.org/pdf/2605.08769v1.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics](https://arxiv.org/abs/2605.03871) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2605.03871) / [PDF](https://arxiv.org/pdf/2605.03871.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [EvoFSM: Controllable Self-Evolution for Deep Research with Finite State Machines](https://arxiv.org/abs/2601.09465) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.09465) / [PDF](https://arxiv.org/pdf/2601.09465.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [EvoConfig: Self-Evolving Multi-Agent Systems for Efficient Autonomous Environment Configuration](https://arxiv.org/abs/2601.16489) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2601.16489) / [PDF](https://arxiv.org/pdf/2601.16489.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery](https://arxiv.org/abs/2604.01658) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2604.01658) / [PDF](https://arxiv.org/pdf/2604.01658.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [AEL: Agent Evolving Learning for Open-Ended Environments](https://arxiv.org/abs/2604.21725) | 2026 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2604.21725) / [PDF](https://arxiv.org/pdf/2604.21725.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |
| [Truly Self-Improving Agents Require Intrinsic Metacognitive Learning](https://arxiv.org/abs/2506.05109) | 2025 | Self-evolving / reflection / prompt optimization | arXiv | [Paper](https://arxiv.org/abs/2506.05109) / [PDF](https://arxiv.org/pdf/2506.05109.pdf) | General capability helpful for ASD AI agents: self-evolution, reflection, prompt optimization, and automatic improvement. |

## General Capabilities Helpful For ASD AI Agents: Skills, Tool-Use, And Workflow

| Paper | Year | Type | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| [When Single-Agent with Skills Replace Multi-Agent Systems and When They Fail](https://arxiv.org/abs/2601.04748) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2601.04748) / [PDF](https://arxiv.org/pdf/2601.04748.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](https://arxiv.org/abs/2602.08234) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2602.08234) / [PDF](https://arxiv.org/pdf/2602.08234.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2605.06614) / [PDF](https://arxiv.org/pdf/2605.06614.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [SkillEvolver: Skill Learning as a Meta-Skill](https://arxiv.org/abs/2605.10500) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2605.10500) / [PDF](https://arxiv.org/pdf/2605.10500.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [SkillCraft: Can LLM Agents Learn to Use Tools Skillfully?](https://arxiv.org/abs/2603.00718) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2603.00718) / [PDF](https://arxiv.org/pdf/2603.00718.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [SkillClaw: Let Skills Evolve Collectively with Agentic Evolver](https://arxiv.org/abs/2604.08377) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2604.08377) / [PDF](https://arxiv.org/pdf/2604.08377.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2605.06130) / [PDF](https://arxiv.org/pdf/2605.06130.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [Skill-R1: Agent Skill Evolution via Reinforcement Learning](https://arxiv.org/abs/2605.09359v1) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2605.09359v1) / [PDF](https://arxiv.org/pdf/2605.09359v1.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [Skill-Pro: Learning Reusable Skills from Experience via Non-Parametric PPO for LLM Agents](https://arxiv.org/abs/2602.01869) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2602.01869) / [PDF](https://arxiv.org/pdf/2602.01869.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents](https://arxiv.org/abs/2605.03353) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2605.03353) / [PDF](https://arxiv.org/pdf/2605.03353.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2602.02474) / [PDF](https://arxiv.org/pdf/2602.02474.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [Group of Skills: Group-Structured Skill Retrieval for Agent Skill Libraries](https://arxiv.org/abs/2605.06978) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2605.06978) / [PDF](https://arxiv.org/pdf/2605.06978.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [From Context to Skills: Can Language Models Learn from Context Skillfully?](https://arxiv.org/abs/2604.27660v1) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2604.27660v1) / [PDF](https://arxiv.org/pdf/2604.27660v1.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents](https://arxiv.org/abs/2605.10332) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2605.10332) / [PDF](https://arxiv.org/pdf/2605.10332.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification](https://arxiv.org/abs/2604.01687) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2604.01687) / [PDF](https://arxiv.org/pdf/2604.01687.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks](https://arxiv.org/abs/2604.20987) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2604.20987) / [PDF](https://arxiv.org/pdf/2604.20987.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |
| [CUA-Skill: Develop Skills for Computer Using Agent](https://arxiv.org/abs/2601.21123) | 2026 | Skills | arXiv | [Paper](https://arxiv.org/abs/2601.21123) / [PDF](https://arxiv.org/pdf/2601.21123.pdf) | Useful for building reusable skills, safer tool use, and workflow orchestration in ASD-focused agents. |

## General Capabilities Helpful For ASD AI Agents: Memory And Long-Horizon Ability

| Paper | Year | Type | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| [delta-mem: Efficient Online Memory for Large Language Models](https://arxiv.org/abs/2605.12357) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2605.12357) / [PDF](https://arxiv.org/pdf/2605.12357.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [SwiftMem: Fast Agentic Memory via Query-aware Indexing](https://arxiv.org/abs/2601.08160) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.08160) / [PDF](https://arxiv.org/pdf/2601.08160.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [StackPlanner: A Centralized Hierarchical Multi-Agent System with Task-Experience Memory Management](https://arxiv.org/abs/2601.05890) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.05890) / [PDF](https://arxiv.org/pdf/2601.05890.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.02553) / [PDF](https://arxiv.org/pdf/2601.02553.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2605.10870) / [PDF](https://arxiv.org/pdf/2605.10870.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [ROMA: Recursive Open Meta-Agent Framework for Long-Horizon Multi-Agent Systems](https://arxiv.org/abs/2602.01848) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2602.01848) / [PDF](https://arxiv.org/pdf/2602.01848.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](https://arxiv.org/abs/2605.15128) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2605.15128) / [PDF](https://arxiv.org/pdf/2605.15128.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Mem2Evolve: Towards Self-Evolving Agents via Co-Evolutionary Capability Expansion and Experience Distillation](https://arxiv.org/abs/2604.10923) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2604.10923) / [PDF](https://arxiv.org/pdf/2604.10923.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Mem-W: Latent Memory-Native GUI Agents](https://arxiv.org/abs/2605.09317v1) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2605.09317v1) / [PDF](https://arxiv.org/pdf/2605.09317v1.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [MedMemoryBench: Benchmarking Agent Memory in Personalized Healthcare](https://arxiv.org/abs/2605.11814) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2605.11814) / [PDF](https://arxiv.org/pdf/2605.11814.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [MAGMA: A Multi-Graph based Agentic Memory Architecture](https://arxiv.org/abs/2601.03236) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.03236) / [PDF](https://arxiv.org/pdf/2601.03236.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Learning How to Remember: A Meta-Cognitive Management Method for Structured and Transferable Agent Memory](https://arxiv.org/abs/2601.07470) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.07470) / [PDF](https://arxiv.org/pdf/2601.07470.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents](https://arxiv.org/abs/2601.16649) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.16649) / [PDF](https://arxiv.org/pdf/2601.16649.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [LSTM-MAS: A Long Short-Term Memory Inspired Multi-Agent System for Long-Context Understanding](https://arxiv.org/abs/2601.11913) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.11913) / [PDF](https://arxiv.org/pdf/2601.11913.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Grounding Agent Memory in Contextual Intent](https://arxiv.org/abs/2601.10702) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.10702) / [PDF](https://arxiv.org/pdf/2601.10702.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Generalizable Self-Evolving Memory for Automatic Prompt Optimization](https://arxiv.org/abs/2603.21520) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2603.21520) / [PDF](https://arxiv.org/pdf/2603.21520.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory](https://arxiv.org/abs/2601.21714) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.21714) / [PDF](https://arxiv.org/pdf/2601.21714.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Continuum Memory Architectures for Long-Horizon LLM Agents](https://arxiv.org/abs/2601.09913) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.09913) / [PDF](https://arxiv.org/pdf/2601.09913.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.01885) / [PDF](https://arxiv.org/pdf/2601.01885.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [AMER-RCL: Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices](https://arxiv.org/abs/2601.02732) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.02732) / [PDF](https://arxiv.org/pdf/2601.02732.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [AMA: Adaptive Memory via Multi-Agent Collaboration](https://arxiv.org/abs/2601.20352) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2601.20352) / [PDF](https://arxiv.org/pdf/2601.20352.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [AI Agent Systems for Supply Chains: Structured Decision Prompts and Memory Retrieval](https://arxiv.org/abs/2602.05524) | 2026 | Memory | arXiv | [Paper](https://arxiv.org/abs/2602.05524) / [PDF](https://arxiv.org/pdf/2602.05524.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://arxiv.org/abs/2510.17281) | 2025 | Memory | arXiv | [Paper](https://arxiv.org/abs/2510.17281) / [PDF](https://arxiv.org/pdf/2510.17281.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [MemGen: WeavingGenerativeLatentMemoryfor Self-Evolving Agents](https://arxiv.org/abs/2509.24704) | 2025 | Memory | arXiv | [Paper](https://arxiv.org/abs/2509.24704) / [PDF](https://arxiv.org/pdf/2509.24704.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957) | 2025 | Memory | arXiv | [Paper](https://arxiv.org/abs/2507.07957) / [PDF](https://arxiv.org/pdf/2507.07957.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |
| [G-Memory: Tracing Hierarchical Memory for Multi-Agent Systems](https://arxiv.org/abs/2506.07398) | 2025 | Memory | arXiv | [Paper](https://arxiv.org/abs/2506.07398) / [PDF](https://arxiv.org/pdf/2506.07398.pdf) | Useful for long-horizon personalization, history tracking, and memory management in ASD-focused agents. |

## General Capabilities Helpful For ASD AI Agents: Recommendation, Collaboration, And Other Agentic Methods

| Paper | Year | Type | Source | Access | Why It Matters |
| --- | --- | --- | --- | --- | --- |
| [Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents](https://arxiv.org/abs/2602.10226) | 2026 | Agentic recommendation | arXiv | [Paper](https://arxiv.org/abs/2602.10226) / [PDF](https://arxiv.org/pdf/2602.10226.pdf) | General capability helpful for ASD AI agents: personalization, recommendation, ranking, and adaptive support decisions. |
| [Self-Distilled Reinforcement Learning for Co-Evolving Agentic Recommender Systems](https://arxiv.org/abs/2604.10029) | 2026 | Agentic recommendation | arXiv | [Paper](https://arxiv.org/abs/2604.10029) / [PDF](https://arxiv.org/pdf/2604.10029.pdf) | General capability helpful for ASD AI agents: personalization, recommendation, ranking, and adaptive support decisions. |
| [Optimizing Agentic Reasoning with Retrieval via Synthetic Semantic Information Gain Reward](https://arxiv.org/abs/2602.00845) | 2026 | Other agentic | arXiv | [Paper](https://arxiv.org/abs/2602.00845) / [PDF](https://arxiv.org/pdf/2602.00845.pdf) | General capability helpful for ASD AI agents: collaboration, retrieval, planning, and evaluation infrastructure. |
| [OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory](https://arxiv.org/abs/2604.26622) | 2026 | Other agentic | arXiv | [Paper](https://arxiv.org/abs/2604.26622) / [PDF](https://arxiv.org/pdf/2604.26622.pdf) | General capability helpful for ASD AI agents: collaboration, retrieval, planning, and evaluation infrastructure. |
| [Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148) | 2026 | Other agentic | arXiv | [Paper](https://arxiv.org/abs/2604.17148) / [PDF](https://arxiv.org/pdf/2604.17148.pdf) | General capability helpful for ASD AI agents: collaboration, retrieval, planning, and evaluation infrastructure. |
| [Context Training with Active Information Seeking](https://arxiv.org/abs/2605.13050) | 2026 | Other agentic | arXiv | [Paper](https://arxiv.org/abs/2605.13050) / [PDF](https://arxiv.org/pdf/2605.13050.pdf) | General capability helpful for ASD AI agents: collaboration, retrieval, planning, and evaluation infrastructure. |
| [Agentic Recommender Systems: A Systematic Literature Review](https://www.computer.org/csdl/journal/ts/2026/04/11363682/2dB08bNroQM) | 2026 | Agentic recommendation | Computer Society | [Paper](https://www.computer.org/csdl/journal/ts/2026/04/11363682/2dB08bNroQM) | General capability helpful for ASD AI agents: personalization, recommendation, ranking, and adaptive support decisions. |
| [AgentRecBench: Benchmarking LLM Agent-based Personalized Recommender Systems](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2d6f7249add096e26679eade1b4cc6f-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | Agentic recommendation | NeurIPS | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e2d6f7249add096e26679eade1b4cc6f-Abstract-Datasets_and_Benchmarks_Track.html) | General capability helpful for ASD AI agents: personalization, recommendation, ranking, and adaptive support decisions. |

## Notes

- This repository is designed as a curated reading list, not a fully automatic ranking system.
- PubMed and arXiv queries are intentionally broad; manual review is expected before publishing updates.
