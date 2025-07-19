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

CRM_Email_AI_Assistant/
├── prompts/ # Prompt templates for the assistant
│ ├── generate_follow_up_prompt.txt
│ ├── suggest_replies_prompt.txt
│ └── summarize_interaction_prompt.txt
│
├── sample_email_threads_CRM/ # Example email threads
│ ├── billing_dispute.md
│ ├── claim_inquiry.md
│ └── ...
│
├── src/
│ ├── CRM_AI_Assistant.py    # Main Streamlit app (UI entry point)
│ └── pages/     
│     ├── 1_Summarize_Email_Interaction.py
│     ├── 2_Suggest_Replies.py
│     └── 3_Generate_Follow_Up_Email.py
│
└── README.md