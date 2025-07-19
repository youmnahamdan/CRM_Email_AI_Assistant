# Dummy API call
def suggest_replies_api(email_thread: str, 
                        additional_notes: str, 
                        number_of_replies: int) -> tuple:
    """This function generates email thread replies
    using LLMs.

    Args:
        - email_thread (str): Conversation between a cutomer and 
        an empolyee as an email thread.
        - additional_notes (str): Additional instructions given 
        to the model 
        - number_of_replies (int): The number of replies to be 
        generated. Also represents the number of parallel API 
        calls to the LLM.

    Returns:
        - tuple: The generated replies
    """
    return ('reply 1', 'reply 2', 'reply 3')

import streamlit as st

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
    additional_notes = st.text_area(
        "📝 Add any special details or information (optional)",
        placeholder="e.g. Apologize to the customer. Declined refund."
    )

    # Number of replies (default : one)
    number_of_replies = st.number_input("Number of replies", min_value=1, max_value=5)

    suggest_button = st.form_submit_button("✨ Suggest Replies")

if suggest_button: 
    # Check for invalid (empty) threads
    if email_thread.strip() == "":
        st.warning("Please enter an email thread.")
    else:
        with st.spinner("Generating suggestions..."):
            replies = suggest_replies_api(email_thread, additional_notes, number_of_replies)
            st.write("## 💬 Replies")
            for reply in replies:
                st.code(reply, language="python")


