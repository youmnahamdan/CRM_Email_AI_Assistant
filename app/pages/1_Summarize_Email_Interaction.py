import time
import streamlit as st
import streamlit.components.v1 as components
from services.ai_services import summarize_interaction_service
from core.utils import create_copy_btn

# Typing animation
def stream_data(text: str):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# Page configuration
st.set_page_config(page_icon='✉️', page_title="CRM Email Assistant", layout="centered")

# Title
st.markdown("## ✉️ AI Email Interaction Summarizer")
st.markdown("Use this assistant to get a smart summary of your email conversation.")

# Inputs
with st.form("email_summary_form"):
    email_thread = st.text_area(
        "📬 Paste the email thread below",
        height=300,
        placeholder="e.g. From: John\nTo: Sarah\nSubject: Proposal...\n\nHi Sarah, ..."
    )
    # Empolyee's notes regarding the summary
    summary_notes = st.text_area(
        "📝 Add any special instructions (optional)",
        placeholder="e.g. Make it 3 sentences. Focus on key decisions."
    )

    submitted = st.form_submit_button("✨ Summarize Interaction")

if submitted:
    # Check for empty email threads
    if email_thread.strip() == "":
        st.warning("Please enter an email thread.")
    else:
        with st.spinner("Generating summary..."):
            summary = summarize_interaction_service(email_thread, summary_notes)
            st.success("Summary generated!")
            st.markdown("### 📄 Summary")
            st.write_stream(stream_data(summary))
            create_copy_btn(f"summary-text", summary)
