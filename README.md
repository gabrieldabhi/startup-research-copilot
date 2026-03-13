# Startup Research Copilot

Startup Research Copilot is an **AI-powered research assistant** designed to help users explore startup strategy, funding insights, and market trends.

The system combines **Retrieval-Augmented Generation (RAG)**, **live web search**, and **LLM reasoning** to deliver structured answers with **source citations and reasoning transparency**.

Instead of relying solely on a language model, the assistant intelligently decides whether to retrieve knowledge from a curated startup knowledge base or perform a real-time web search.

---

# Problem

Startup founders, analysts, and operators often need quick insights about:

- Product-market fit
- Venture capital funding
- Startup growth strategies
- Market trends
- Competitor dynamics

However, relevant knowledge is often **scattered across multiple sources**, making research slow and inefficient.

---

# Solution

Startup Research Copilot provides a **single AI interface for startup intelligence** by combining:

- Internal startup knowledge retrieval
- Live internet search
- Language model reasoning

The system dynamically routes each query to the most appropriate knowledge source to provide reliable and contextual answers.

---

# Key Features

- Retrieval-Augmented Generation (RAG)
- FAISS vector database for semantic search
- Live web search integration
- Intelligent query routing between tools
- Streamlit chatbot interface
- Response modes (Concise / Detailed)
- Source citation for transparency
- Reasoning explanation for tool selection

---

# System Architecture

The application follows a modular AI architecture that separates retrieval, reasoning, and user interaction.

```
User Query
    │
    ▼
Query Router
    │
    ▼
Determine Knowledge Source

 ┌───────────────► RAG Pipeline
 │                     │
 │                     ▼
 │               FAISS Vector Search
 │                     │
 │                     ▼
 │              Retrieve Document Context
 │
 ├───────────────► Web Search
 │                     │
 │                     ▼
 │               Tavily Search API
 │                     │
 │                     ▼
 │               Retrieve Web Results
 │
 └───────────────► LLM Reasoning
                       │
                       ▼
                Direct Model Reasoning

All Context Sources
        │
        ▼
Prompt Builder
        │
        ▼
Groq Llama-3.3-70B-Versatile
        │
        ▼
Generated Response
        │
        ▼
Streamlit Chat Interface
```

## Architecture Overview

The system uses a modular AI pipeline that dynamically routes user queries to the most appropriate knowledge source.

1. **Query Router** analyzes the incoming question.
2. The system selects between three tools:
   - **RAG Pipeline** for internal startup knowledge retrieval
   - **Web Search** for real-time information
   - **LLM Reasoning** for general questions
3. Retrieved context is passed to the **Prompt Builder**.
4. The prompt is processed by the **Groq Llama-3.3-70B-Versatile**.
5. The response is returned through the **Streamlit chat interface** with sources and reasoning.

---

# Tech Stack

| Component       | Technology              |
|-----------------|-------------------------|
| Frontend        | Streamlit               |
| Vector Database | FAISS                   |
| Embeddings      | Sentence Transformers   |
| LLM             | llama-3.3-70b-versatile |
| Web Search      | Tavily API              |
| Language        | Python                  |

---

# Dataset

The RAG knowledge base contains curated startup knowledge documents derived from reliable resources such as:

- Y Combinator startup guidance
- Venture capital literature
- Startup strategy frameworks
- Market intelligence research

Covered topics include:

- Product-market fit
- Startup funding stages
- Venture capital basics
- Growth strategies
- Competitor analysis
- Startup failure causes
- Market validation frameworks

---

# Project Structure

```
config/
models/
utils/
data/startup_docs/
vectorstore/
app.py
requirements.txt
README.md
```

---

# Running the Project

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run app.py
```

---

# Example Queries

Try asking questions such as:

- What is product market fit?
- Latest AI startup funding trends
- Why do startups fail?
- How do venture capital funding stages work?

---

# Deployment

The application can be deployed using **Streamlit Cloud**.

After deployment, users can access the chatbot through a browser interface.

Live Demo: https://startup-research-copilot-bpudnwuxxbwiq6hlgzdaov.streamlit.app/

---

# Author

AI Engineer Assignment Submission
