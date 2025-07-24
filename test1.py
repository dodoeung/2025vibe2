import streamlit as st
import random

st.set_page_config(page_title="기분별 음식 추천", page_icon="🍱", layout="wide")

# 스타일 추가
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #fff1eb, #ace0f9);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        font-size: 48px;
        font-weight: 900;
        text-align: center;
        color: #ff69b4;
        text-shadow: 2px 2px #ffc0cb;
    }
    .highlight {
        background-color: #ffffffcc;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 4px 4px 20px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌈 오늘의 기분으로 음식 추천받기 🍙</div>', unsafe_allow_html=True)
st.write("")

# 신박한 기분 목록
feelings = {
    "🧠 뇌가 과열된 날": ("비빔냉면", "https://i.imgur.com/VoW5E7f.png", "매콤하고 시원한 냉면으로 머리를 식혀요!"),
    "🐢 느리게 살고 싶은 날": ("수플레 팬케이크", "https://i.imgur.com/Gmcz6hx.png", "폭신하고 달콤한 게 천천히 즐기기 딱 좋아요~"),
    "🛸 현실도피 하고 싶은 날": ("타코야끼", "https://i.imgur.com/BlOqES0.png", "지구를 잠시 떠나 일본 야시장 느낌~"),
    "🎢 기분이 널뛰는 날": ("떡볶이", "https://i.imgur.com/1d13cGx.png", "단짠단짠 매운맛으로 감정을 같이 널뛰자!"),
    "🧚 공상에 빠진 날": ("마카롱", "https://i.imgur.com/b4kL0re.png", "알록달록 상상의 나라로~"),
    "🤹 아무 것도 하기 싫은 날": ("컵라면", "https://i.imgur.com/SKP7Hym.png", "그냥 물만 부으면 끝. 최고.")
}

selected_feeling = st.selectbox("지금 당신의 기분은...?", list(feelings.keys()))

if selected_feeling:
    food, img_url, comment = feelings[selected_feeling]

    st.markdown(f"""
    <div class="highlight">
        <h2>🍽 추천 음식: {food}</h2>
        <img src="{img_url}" width="300">
        <p style='font-size:20px;'>💬 {comment}</p>
    </div>
    """, unsafe_allow_html=True)

# 캐릭터 이미지 (공통)
st.image("https://i.imgur.com/E6z5CM5.png", caption="🍓 푸딩요정이 함께해요!", width=200)

