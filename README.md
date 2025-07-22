# 📧 CRM Email AI Assistant

An AI assistant that streamlines CRM communications by **summarizing customer email threads**, **suggesting context-aware replies**, and **generating proactive follow-up emails**.

Built with **Python**, **Streamlit**, and **LangChain**.

---

## 🚀 Features

- 📄 **Email Summarization** – Understand long threads at a glance.
- 💬 **Smart Reply Suggestions** – Generate contextually appropriate responses.
- 🔁 **Follow-Up Generator** – Create professional follow-up messages automatically.
- 📂 **Prompt-Driven Design** – Easily customize AI behavior using modular prompt templates.
- 🧪 **Sample CRM Scenarios** – Preloaded with example threads (billing, claims, upgrades, etc.).

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **[Streamlit](https://streamlit.io/)** – for the interactive UI
- **[LangChain](https://www.langchain.com/)** – to manage prompt logic and model calls
- **OpenAI API** (or compatible LLM)

---
## 📁 Project Structure

```text
email_assistant_crm/
│
├── app/    
│   │
│   ├── core/  
│   │   └── __init__.py 
│   │   └── config.py
│   │   └── utils.py
│   │
│   ├── services/
│   │   └── __init__.py 
│   │   └── ai_services.py
│   │
│   ├── loaders/
│   │   └── __init__.py 
│   │   └── model_loader.py
│   │   └── prompt_loader.py
│   │   └── runnable_parallel_loader.py
│   │
│   ├── pages/                                    # Streamlit pages
│   │   └── 1_Summarize_Email_Interaction.py
│   │   └── 2_Suggest_Replies.py
│   │   └── 3_Generate_Follow_Up_Email.py
│   │
│   ├── streamlit/                                # Streamlit secrets (something like .env) 
│   │   └── secrets.toml
│   │
│   └── CRM_AI_Assistant.py                       # Streamlit app entrypoint
│
├── tests/     
│   └── __init__.py 
│   └── test_ai_services.py
│
├── prompts/...                                   # Contains system prompts (for display purposes)
│
├── sample_email_threads_CRM/...                  # Contains sample email threads for testing (feel free to use your own)
│
├── requirements.txt 
└── README.md
```

## 📌 Required in secrets.toml

**Example: LLM="gpt-4o-mini"**

| Variable         | Description                 | Example                 |
|------------------|-----------------------------|--------------------------|
| `LLM`            | Model name (LLM)            | `gpt-4o-mini`            |
| `OPENAI_API_KEY` | Your OpenAI API key         | `sk-...`                 |


## 🚀 Visit the App

🔗 [Click here to try the AI Email Assistant for CRM](https://ai-email-assistant-for-crm.streamlit.app/)