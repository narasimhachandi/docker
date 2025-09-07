# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Home route
# @app.route('/')
# def home():
#     return "Hello, Karunya!!!!!!! I LOVE YOUUUUUU!!!!"

# # Example API route
# @app.route('/api/greet', methods=['GET'])
# def greet():
#     name = request.args.get("name", "World")
#     return f"Hello, {name}!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)


import streamlit as st
import time

st.set_page_config(page_title="For Karunya 💖", page_icon="💍", layout="centered")

# Custom CSS for glowing heart effect
st.markdown(
    """
    <style>
    .heart {
        color: red;
        font-size: 100px;
        text-align: center;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    .big-text {
        font-size: 36px !important;
        text-align: center;
        color: #FF4081;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page content
st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)
st.markdown("<p class='big-text'>Hello, Karunya 💕</p>", unsafe_allow_html=True)

st.write("")

st.subheader("I have something very important to ask you...")

if "step" not in st.session_state:
    st.session_state.step = 0

if st.session_state.step == 0:
    if st.button("Click to Continue 💌"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.markdown("### 🌹 From the day I met you, my life has been brighter... ")
    st.markdown("### 💖 Karunya, you mean the world to me...")
    st.markdown("### 💍 Will you be mine forever?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💖 YES, Forever!"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        st.button("😳 Let me think...")

elif st.session_state.step == 2:
    st.balloons()
    st.snow()
    st.markdown("<div class='big-text'>🎉 Yayyy!!! I love you, Karunya 💕 Forever & Always 💍</div>", unsafe_allow_html=True)
    st.markdown("<div class='heart'>💞💞💞</div>", unsafe_allow_html=True)
    st.success("You just made me the happiest person alive! 💖")
