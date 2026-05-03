# 🚀 InventoryGPT
An AI-powered inventory optimization knowledge assistant 

## 📘 Project Overview

InventoryGPT is an AI-powered knowledge assistant designed to provide intelligent insights into inventory management and supply chain optimization. Leveraging advanced RAG (Retrieval-Augmented Generation) technology, it transforms complex inventory research into actionable recommendations.

## ✨ Key Features

- **Smart Document Q&A**: Ask complex questions about inventory management
- **Domain-Specific Insights**: Powered by a curated corpus of industry documents
- **AI-Driven Recommendations**: Intelligent, context-aware suggestions
- **Easy-to-Use Interface**: Streamlit web application

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)

- **Backend**: Python
- **RAG Framework**: LangChain
- **Vector Database**: ChromaDB
- **LLM**: OpenAI GPT-4
- **Web Interface**: Streamlit

## 🎯 Example Queries

- "How to reduce safety stock for seasonal products?"
- "Best forecasting methods for steel manufacturing"
- "Strategies for minimizing inventory holding costs"

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/inventory-optimization-assistant.git

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

## 🤖 LLM Configuration

### Free Open-Source Model
We use Hugging Face's `facebook/opt-350m` for cost-free, open-source AI capabilities.

### Installation for LLM
```bash
pip install transformers torch

# Run the Streamlit app
streamlit run app.py

