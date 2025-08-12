# ❤️ Heart Log – AI-Powered Love Language Classifier

Heart Log is a lightweight Flask web app with an integrated API that classifies relationship moments into one of the **Five Love Languages** using a local Ollama LLM.

It’s built for quick, structured reflection — submit an entry, get an instant classification with a short reasoning, and track patterns over time.

---

## ✨ Features

- **Five Love Languages Classification**
  - Acts of Service
  - Quality Time
  - Receiving Gifts
  - Words of Affirmation
  - Physical Touch
- **AI-Powered Categorization**
  - Uses Ollama (running locally or on LAN)
  - Prompt-engineered for consistent JSON output
- **Two-Part Architecture**
  - Main Flask app for UI
  - Separate categorization API endpoint
- **Error Handling**
  - Gracefully handles malformed JSON or misclassification
- **Portable Deployment**
  - Dockerized for easy hosting anywhere

---

## 🛠 Tech Stack

- **Python 3**
- **Flask**
- **Ollama LLM API** (model-agnostic)
- **Docker & Docker Compose**
- HTML/CSS templates for the web UI

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/TcDrozd/heart-log.git
cd heart-log