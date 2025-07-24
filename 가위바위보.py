import streamlit as st
import random

st.set_page_config(page_title="귀여운 가위바위보 게임", page_icon="🧸", layout="centered")

# 점수 저장용 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "win_count" not in st.session_state:
    st.session_state.win_count = 0
if "lose_count" not in st.session_state:
    st.session_state.lose_count = 0
if "draw_count" not in st.session_state:
    st.session_state.draw_count = 0

# 스타일
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
        font-size: 28px;
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
    .score-box {
        text-align: center;
        background-color: #fff0f5;
        padding: 15px;
        border-radius: 12px;
        margin-top: 20px;
        font-size: 20px;
        font-weight: bold;
        color: #ff4081;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    @keyframes pop {
        0%   { transform: scale(1); }
        50%  { transform: scale(1.4); }
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
    "✂️🐱 가위 (고양이 가위)": "scissors",
    "✊🐻 바위 (곰돌이 주먹)": "rock",
    "✋🦊 보 (여우 손바닥)": "paper"
}

user_choice_label = st.radio("👉 하나 골라줘!", list(choices.keys()), index=0)

if st.button("대결 시작! 💫"):
    user_choice = choices[user_choice_label]
    computer_choice = random.choice(list(choices.values()))

    cute_map = {
        "scissors": "✂️🐱 가위",
        "rock": "✊🐻 바위",
        "paper": "✋🦊 보"
    }

    result_text = ""
    result_class = ""
    score_change = 0

    if user_choice == computer_choice:
        result_text = "😐 비겼어요!"
        st.session_state.draw_count += 1
    elif (user_choice == "rock" and computer_choice == "scissors"):
        result_text = "🎈 <span class='win'>WIN!</span> 바위로 이겼어요! +1점 🎉"
        score_change = 1
        result_class = "win"
        st.session_state.win_count += 1
        st.balloons()
    elif (user_choice == "scissors" and computer_choice == "paper"):
        result_text = "🎈 <span class='win'>WIN!</span> 가위로 이겼어요! +2점 🎉"
        score_change = 2
        result_class = "win"
        st.session_state.win_count += 1
        st.balloons()
    elif (user_choice == "paper" and computer_choice == "rock"):
        result_text = "🎈 <span class='win'>WIN!</span> 보로 이겼어요! +3점 🎉"
        score_change = 3
        result_class = "win"
        st.session_state.win_count += 1
        st.balloons()
    else:
        result_text = "😭 <span class='lose'>LOSE...</span> 컴퓨터가 이겼어요! -1점"
        score_change = -1
        result_class = "lose"
        st.session_state.lose_count += 1

    # 점수 업데이트
    st.session_state.score += score_change

    # 결과 출력
    st.markdown(f"""
        <div class="emoji">
            당신 👉 {cute_map[user_choice]} &nbsp; VS &nbsp; {cute_map[computer_choice]} 👈 컴퓨터
        </div>
        <div class="result {result_class}">{result_text}</div>
    """, unsafe_allow_html=True)

# 점수판
st.markdown(f"""
    <div class="score-box">
        🧾 점수판<br>
        🏆 총 점수: {st.session_state.score}점<br>
        ✅ 승리: {st.session_state.win_count}회 &nbsp;&nbsp; ❌ 패배: {st.session_state.lose_count}회 &nbsp;&nbsp; 🤝 비김: {st.session_state.draw_count}회
    </div>
""", unsafe_allow_html=True)

