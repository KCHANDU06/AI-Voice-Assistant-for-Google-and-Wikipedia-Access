import streamlit as st
import subprocess
import os
import time

# Page setup
st.set_page_config(page_title="AI Voice Assistant for Google and Wikipedia Access", page_icon="🔍", layout="wide")

# === Custom CSS ===
custom_css = """
<style>
body {
    background-image: url('https://images.unsplash.com/photo-1581091012184-5c1c7e18336e?auto=format&fit=crop&w=1400&q=80');  /* Soft tech background */
    background-size: cover;
    background-attachment: fixed;
}

h1.gradient {
    background: -webkit-linear-gradient(45deg, #00f260, #0575e6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.5em;
    font-weight: 800;
    text-align: center;
    margin-top: 30px;
    text-shadow: 2px 2px 4px #00000055;
}

.stButton>button {
    background-color: #00c4cc;
    color: white;
    font-size: 1.2em;
    border-radius: 10px;
    padding: 0.6em 1.2em;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #007c80;
    transform: scale(1.05);
}

.transcript-box {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 15px;
    font-size: 1.2em;
    color: #111;
    font-weight: bold;
    text-align: center;
    margin-top: 30px;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.3);
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# === App UI ===
st.markdown('<h1 class="gradient">AI Voice Assistant for Google and Wikipedia Access</h1>', unsafe_allow_html=True)
st.markdown("### Click the button below to ask your assistant! 🎙️")

# Button to start assistant
if st.button("🔊 Start to Speak "):
    st.success("🎧 Listening... Speak now.")
    try:
        subprocess.run(["python", "backend.py"])
        time.sleep(1)

        if os.path.exists("transcript.txt"):
            with open("transcript.txt", "r", encoding="utf-8") as f:
                transcript = f.read()
                st.markdown(f"<div class='transcript-box'>🗣️ You said:<br><br>“{transcript}”</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ No speech input detected.")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.info("Say 'exit' or 'stop conversation' to end the assistant.")
