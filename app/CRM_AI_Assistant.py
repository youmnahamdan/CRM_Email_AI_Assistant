import streamlit as st

# Page configuration
st.set_page_config(page_icon='📬', page_title='AI Email Assistant for CRM')

# Title
st.write('# 📬 Welcome to Your AI Email Assistant for CRM')

# Intro paragraph
st.write('''This AI-powered assistant is designed to help you handle customer emails efficiently — 
saving you time, reducing effort, and maintaining high-quality communication.''')

# Assistant capabilities
st.write('## ✨ What can it do?')

st.markdown("""
- 💬 **Suggest up to five diverse replies**  
  Get multiple AI-generated response options tailored to your original email.

- 📚 **Summarize long email threads**  
  Avoid reading long chains by receiving clear and concise summaries.

- 🔄 **Generate follow-up emails**  
  Automatically create proactive follow-ups to keep the conversation going.

- 🛠️ **Customize with your instructions**  
  At every step, you can give the assistant extra directions to fine-tune the output.
""", unsafe_allow_html=True)

# Feedback and contact
st.write('## 🤝 Feedback & Contact')
st.write("""If you find this tool helpful or have suggestions for improvement, feel free to reach out!💡  
I'm also happy to collaborate or build a custom solution for your use case.""")

st.markdown("""
- 📧 **Contact**: hamdanyoumna@gmail.com  
- 🔗 **LinkedIn**: www.linkedin.com/in/youmna-hamdan
- 🔗 **GitHub**: https://github.com/youmnahamdan
- 🖊️ **Created by**: Youmna Hamdan
""")
