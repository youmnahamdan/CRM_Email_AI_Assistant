import streamlit.components.v1 as components

def create_copy_btn(textarea_id: str, text_to_copy: str) -> None:
    components.html(f"""
        <div style="position:relative; font-family: 'Segoe UI', sans-serif; font-size: 14px;  margin-left: 0px; padding: 0px;">
        <!-- Hidden textarea -->
        <textarea id="{textarea_id}" style="
        position: absolute;
        opacity: 0;
        height: 1px;
        pointer-events: none;
        ">{text_to_copy}</textarea>

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
                    var copyText = document.getElementById("{textarea_id}");
                    copyText.select();
                    document.execCommand("copy");
                    document.getElementById("copy-status").innerText = "✅ Copied!";
                }}
            </script>
        </div>
    """, height=100)
