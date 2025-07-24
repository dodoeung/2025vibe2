import streamlit as st
import random

st.set_page_config(page_title="귀여운 가위바위보 게임", page_icon="🧸", layout="centered")

# 점수 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "win_count" not in st.session_state:
    st.session_state.win_count = 0
if "lose_count" not in st.session_state:
    st.session_state.lose_count = 0
if "draw_count" not in st.session_state:
    st.session_state.draw_count = 0
if "rules_checked" not in st.session_state:
    st.session_state.rules_checked = False

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
    .rule-box {
        background-color: #fffaf0;
        border-radius: 15px;
        padding: 20px;
        font-size: 18px;
        line-height: 1.6;
        color: #444;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.05);
    }
    .rule-box h3 {
        color: #e91e63;
        text-align: center;
        font-size: 24px;
        margin-bottom: 10px;
    }
    .rule-box ul {
        list-style: none;
        padding-left: 0;
    }
    .rule-box li::before {
        content: "🌟 ";
    }
    </style>
    <h1 class="title">🐰 컴퓨터와 귀여운 가위바위보 ✨</h1>
""", unsafe_allow_html=True)

# 규칙 설명
if not st.session_state.rules_checked:
    with st.container():
        st.markdown("""
        <div class="rule-box">
            <h3>🎯 게임 규칙 안내</h3>
            <ul>
                <li>✂️🐱 <b>가위로 이기면</b> +2점</li>
                <li>✊🐻 <b>바위로 이기면</b> +1점</li>
                <li>✋🦊 <b>보로 이기면</b> +3점</li>
                <li>❌ <b>지면</b> 무기와 상관없이 -1점</li>
                <li>🤝 <b>비기면</b> 점수 변동 없음</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("✅ 규칙 확인하고 게임 시작!"):
            st.session_state.rules_checked = True
    st.stop()  # 버튼 누르기 전에는 아래 실행 안되도록

# 게임 로직
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


