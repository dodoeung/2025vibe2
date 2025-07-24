import streamlit as st
import random

st.set_page_config(page_title="귀여운 가위바위보 게임", page_icon="🎀", layout="centered")

# 💖 스타일링
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        color: #ff69b4;
        font-family: "Comic Sans MS", cursive, sans-serif;
    }
    .emoji {
        font-size: 60px;
        text-align: center;
        margin-bottom: 20px;
    }
    .result {
        text-align: center;
        font-size: 30px;
        margin-top: 30px;
    }
    .win {
        color: #4CAF50;
        animation: pop 0.5s ease-in-out;
    }
    .lose {
        color: #e91e63;
        animation: shake 0.3s ease-in-out;
    }
    .choice-label {
        font-size: 18px;
        text-align: center;
        margin-top: 10px;
        color: #555;
    }
    @keyframes pop {
        0%   { transform: scale(1); }
        50%  { transform: scale(1.5); }
        100% { transform: scale(1); }
    }
    @keyframes shake {
        0% { transform: translateX(0px); }
        25% { transform: translateX(-5px); }
        50% { transform: translateX(5px); }
        75% { transform: translateX(-5px); }
        100% { transform: translateX(0px); }
    }
    </style>
    <h1 class="title">🐰 컴퓨터와 귀여운 가위바위보 ✨</h1>
""", unsafe_allow_html=True)

# 선택지
choices = {
    "✂️ 가위": "scissors",
    "🪨 바위": "rock",
    "📄 보": "paper"
}

# 사용자 선택
user_choice_label = st.radio("👉 하나 골라줘!", list(choices.keys()), index=0)

if st.button("대결 시작! 💫"):
    user_choice = choices[user_choice_label]
    computer_choice = random.choice(list(choices.values()))

    # 명확한 이모지와 텍스트 매핑
    pretty_map = {
        "rock": "🪨 바위",
        "paper": "📄 보",
        "scissors": "✂️ 가위"
    }

    # 결과 판정
    if user_choice == computer_choice:
        result_text = "😐 비겼어요!"
        result_class = ""
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_text = "🎈 <span class='win'>WIN!</span> 당신이 이겼어요! 🎉"
        result_class = "win"
        st.balloons()
    else:
        result_text = "😭 <span class='lose'>LOSE...</span> 컴퓨터가 이겼어요!"
        result_class = "lose"

    # 결과 출력
    st.markdown(f"""
        <div class="emoji">
            당신 👉 {pretty_map[user_choice]} &nbsp; VS &nbsp; {pretty_map[computer_choice]} 👈 컴퓨터
        </div>
        <div class="result {result_class}">{result_text}</div>
    """, unsafe_allow_html=True)
