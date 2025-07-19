import time
import streamlit as st
import streamlit.components.v1 as components

# Dummy API for demonstration
def summarize_email_api(email_thread: str, summary_notes: str):
    return email_thread * 2 + summary_notes * 2

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
            summary = summarize_email_api(email_thread, summary_notes)
            st.success("Summary generated!")
            st.markdown("### 📄 Summary")
            st.write_stream(stream_data(summary))
            components.html(f"""
              <div style="position:relative; font-family: 'Segoe UI', sans-serif; font-size: 14px;  margin-left: 0px; padding: 0px;">
                  <!-- Hidden textarea -->
                  <textarea id="summary-text" style="
                      position: absolute;
                      opacity: 0;
                      height: 1px;
                      pointer-events: none;
                  ">{summary}</textarea>

                  <!-- Inline copy button and status -->
                  <div style="display: inline; align-items: center; gap: 10px; margin-top: 10px;">
                      <button onclick="copyToClipboard()" style="
                          background-color: #006D5B;
                          color: white;
                          padding: 0.5rem 1rem;
                          border: none;
                          border-radius: 0.5rem;
                          cursor: pointer;
                          font-size: 14px;
                          transition: background-color 0.3s;
                      " 
                      onmouseover="this.style.backgroundColor='#005347'" 
                      onmouseout="this.style.backgroundColor='#006D5B'">
                          📋 Copy
                      </button>
                      <span id="copy-status" style="color: gray;"></span>
                  </div>

                  <script>
                  function copyToClipboard() {{
                      var copyText = document.getElementById("summary-text");
                      copyText.select();
                      document.execCommand("copy");
                      document.getElementById("copy-status").innerText = "✅ Copied!";
                  }}
                  </script>
              </div>
          """, height=100)