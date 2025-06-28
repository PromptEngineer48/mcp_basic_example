# 🕸️ LLM Web Search App

This Streamlit app enables users to scrape web content from a given URL using Bright Data’s Multi-Server MCP and extract insights by querying a Large Language Model (LLM). Ideal for summarizing or analyzing content from platforms like Reddit, LinkedIn, or general web pages.

## 🚀 Features

- 🔍 Scrape structured content from websites using Bright Data’s MCP tools
- 🤖 Generate intelligent responses using Ollama's local LLM (`gemma3n:latest`)
- 🧠 Automatically selects the right scraper based on URL
- 🖥️ Clean, simple UI built with Streamlit

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – for the frontend interface  
- [LangChain](https://www.langchain.com/) – to manage tools and workflows  
- [Bright Data MCP](https://brightdata.com/) – for scraping tools  
- [Ollama](https://ollama.com/) – to run local LLMs like `gemma3n`  
- Python `asyncio` – for asynchronous execution  

---

## 🧾 Prerequisites

- Python 3.8+  
- Node.js (for running MCP tools)  
- [Bright Data](https://brightdata.com/) API Token  
- [Ollama](https://ollama.com/) installed with the `gemma3n` model  

---

## 🔧 Installation

```bash
# Clone the repo
git clone https://PromptEngineer48/mcp_basic_example.git
cd mcp_basic_example

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
