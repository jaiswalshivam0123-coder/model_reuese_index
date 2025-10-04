# 🧠 Model Reuse Index (MRI)

A local prototype for discovering, ranking, and reusing AI assets (models, agents, pipelines) in large organizations to reduce cloud costs, duplication, and carbon footprint.

---

## 🚀 Why MRI?

In enterprise environments, teams often:
- Rebuild similar models or agents without realizing it.
- Store projects in siloed locations (Confluence, GitHub, shared drives).
- Miss opportunities for cost savings and reusability.

**MRI** is a smart search & discovery system that helps surface existing AI assets and assess how reusable they are — like a private HuggingFace + agent registry for your company.

---

## 🔍 Features

- 📊 Upload or connect Excel metadata about AI assets (simulated for now).
- 🔎 Search by column (traditional) or use a natural language query via a local LLM (e.g., Mistral via Ollama).
- 🧠 Early structure for scoring reusability (freshness, similarity, usage context).
- 🧩 Modular code for embedding support, chat-based search, and future expansion to Confluence/GitHub scraping.

---

## 📁 Folder Structure

```

model_reuse_index/
├── app/                    # Streamlit or CLI interface
│   └── search_interface.py
├── scripts/                # Logic for reading/searching Excel
│   └── parse_assets.py
├── utils/                  # Embedding + LLM utilities
│   └── embedding_utils.py
├── config/                 # Constants (e.g., prompt text)
│   └── constants.py
├── data/                   # Place your asset metadata Excel file here
├── main.py                 # CLI entry point
├── requirements.txt
└── README.md

````

---

## 🛠️ Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/jaiswalshivam0123-coder/model_reuse_index.git
cd model_reuse_index
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start with CLI (for now)

```bash
python main.py
```

You'll be prompted to:

* Enter the path to your Excel file
* Choose column-based or LLM-based search
* Get matching results or natural-language insights

---

## 🤖 LLM Support (via Ollama)

We use [Ollama](https://ollama.com/) to run local LLMs like Mistral or LLaMA 2.

### Install and run:

```bash
ollama pull mistral
```

Then make sure Ollama is running in the background.

---

## 📈 Roadmap

* [ ] Add semantic search with SentenceTransformer
* [ ] Streamlit or Gradio UI
* [ ] Connect to Confluence / GitHub
* [ ] Reuse scoring (Freshness, Similarity, Modularity)
* [ ] Green-AI recommendations (compute cost, infra optimization)

---

## ♻️ Vision

By helping teams **find and reuse** existing ML assets, MRI:

* Cuts **cloud compute costs**
* Reduces **carbon emissions**
* Improves **collaboration**
* Avoids **duplicate work**

MRI is not just a tool — it’s a mindset for **smarter, more sustainable AI development** in enterprises.

---

## 📬 Want to Contribute?

This project is in early development. PRs, feedback, and collab ideas welcome.

```

---

Just copy this into your `README.md` file and push it to GitHub. It will render perfectly there.
```
