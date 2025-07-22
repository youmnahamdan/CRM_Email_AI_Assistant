import streamlit as st
import streamlit.components.v1 as components
from services.ai_services import suggest_replies_service
from core.utils import create_copy_btn



# Page configuration
st.set_page_config(page_icon='💬', page_title='Suggest Replies')

# Title
st.markdown("## 💬 AI Assistant For Replies Suggestion")
st.markdown("Use this assistant to obtain relevant replies for your email threads.")

# Inputs
with st.form("email_form"):
    email_thread = st.text_area(
        "📬 Paste the email thread below",
        height=300,
        placeholder="e.g. From: John\nTo: Sarah\nSubject: Proposal...\n\nHi Sarah, ..."
    )
    # Additional details to the replies
    employee_notes = st.text_area(
        "📝 Add any special details or information (optional)",
        placeholder="e.g. Apologize to the customer. Declined refund."
    )

    # Number of replies (default : one)
    number_of_replies = st.number_input("Number of replies", min_value=1, max_value=5)

    # Email tone
    email_tone = st.selectbox(
        "How would you like the email to sound? (email tone)",
        ('friendly', 'formal', 'persuasive')
    )

    suggest_button = st.form_submit_button("✨ Suggest Replies")

if suggest_button: 
    reply_idx = 1
    # Check for invalid (empty) threads
    if email_thread.strip() == "":
        st.warning("Please enter an email thread.")
    else:
        with st.spinner("Generating suggestions..."):
            replies = suggest_replies_service(
                email_thread, 
                employee_notes, 
                email_tone,
                number_of_replies
            )
            st.write("## 💬 Replies")
            for key, value in replies.items():
                st.write(f'### {key}')
                st.text_area("Email", value, height=300)
                create_copy_btn(f"reply-{reply_idx}", value)
                reply_idx += 1



