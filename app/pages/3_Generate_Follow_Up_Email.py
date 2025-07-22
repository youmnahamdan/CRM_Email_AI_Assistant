import time
import streamlit as st
from services.ai_services import generate_follow_up_service
from core.utils import create_copy_btn


# Typing animation
def stream_data(text: str):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# Page configuration
st.set_page_config(page_icon='🔁', page_title='Generate Follow-Up Email')

# Title
st.write('# 🔁 Generate Follow-Up Email')

# Email Form
with st.form('email_form'):
    email_thread = st.text_area(
        "📬 Paste the email thread below",
        height=300,
        placeholder="e.g. From: John\nTo: Sarah\nSubject: Proposal...\n\nHi Sarah, ..."
    )
    # Follow-Up email notes
    follow_up_notes = st.text_area(
        "📝 Follow-Up details and goals (optional)",
        placeholder="e.g. Check if the issue was resolved. Check if the refunding was successful."
    )
    # Email tone (friendly / formal / persuasive)
    email_tone = st.selectbox(
        "How would you like the email to sound? (email tone)",
        ('friendly', 'formal', 'persuasive')
    )
    submitted = st.form_submit_button("✨ Generate Follow-Up")

if submitted:
    with st.spinner("Generating follow-up email..."):
        follow_up_email = generate_follow_up_service(email_thread, follow_up_notes, email_tone)
        st.write('## 🔁 Follow-Up Email')
        st.write_stream(stream_data(follow_up_email))
        create_copy_btn(f"follow-up-text", follow_up_email)


