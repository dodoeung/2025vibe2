import streamlit as st
from datetime import datetime
import random

# 별자리 계산 함수
def get_zodiac_sign(month, day):
    zodiac_signs = [
        ("염소자리", (12, 22), (1, 19), "🐐"),
        ("물병자리", (1, 20), (2, 18), "🏺"),
        ("물고기자리", (2, 19), (3, 20), "🐟"),
        ("양자리", (3, 21), (4, 19), "🐏"),
        ("황소자리", (4, 20), (5, 20), "🐂"),
        ("쌍둥이자리", (5, 21), (6, 21), "👯‍♀️"),
        ("게자리", (6, 22), (7, 22), "🦀"),
        ("사자자리", (7, 23), (8, 22), "🦁"),
        ("처녀자리", (8, 23), (9, 22), "👰"),
        ("천칭자리", (9, 23), (10, 23), "⚖️"),
        ("전갈자리", (10, 24), (11, 22), "🦂"),
        ("사수자리", (11, 23), (12, 21), "🏹"),
    ]
    for sign, start, end, emoji in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign, emoji
    return "알 수 없음", ""

# 적극적 + 따뜻한 조언 문구 모음
advice_list = [
    "오늘은 웃는 얼굴이 사랑을 부를 거예요 😊",
    "적극적으로 다가가면 운명의 문이 열릴지도 몰라요 💌",
    "마음을 표현할 용기가 사랑을 부르게 될 거예요 🗣️",
    "먼저 인사해보세요. 모든 인연은 작은 용기에서 시작돼요 🙋‍♀️",
    "지금의 당신은 사랑을 받을 자격이 충분해요 💖",
    "진심은 반드시 닿아요. 솔직해지는 걸 두려워하지 마세요 🌈",
    "사랑은 준비된 사람에게 찾아와요. 당신은 충분히 준비됐어요 🕊️",
    "사랑받고 싶다면 먼저 사랑을 나눠보세요 🤲",
    "사랑은 기다림이 아니라, 선택이에요. 당신이 움직일 차례에요 🚶‍♀️",
    "작은 관심이 큰 인연이 될 수 있어요 👀",
    "지금 행동하면 내일은 다르게 펼쳐질 거예요 🗓️",
    "호감은 표현될 때 꽃을 피워요 🌸",
    "잠시의 용기가 오랫동안의 행복을 가져다줄 수 있어요 🧡",
    "오늘의 노력은 내일의 설렘으로 돌아올 거예요 ✨",
    "사랑은 운명도 있지만, 태도이기도 해요 💪",
    "적극적인 당신에게 행운이 따라붙어요 🍀",
    "당신 안의 매력을 세상에 보여줄 때가 왔어요 🌟",
    "사랑에 있어 망설임은 기회를 놓치게 해요 – 오늘은 행동할 날이에요 🔥",
    "작은 칭찬이 관계의 시작일 수 있어요. 시작해보세요 💬",
    "당신의 오늘 행동이 내일의 인연을 바꿔줄 거예요 🧭"
]

# 궁합 가능한 별자리
zodiac_compatibility = [
    ("염소자리", "황소자리"),
    ("물병자리", "쌍둥이자리"),
    ("물고기자리", "게자리"),
    ("양자리", "사자자리"),
    ("황소자리", "처녀자리"),
    ("쌍둥이자리", "천칭자리"),
    ("게자리", "물고기자리"),
    ("사자자리", "양자리"),
    ("처녀자리", "염소자리"),
    ("천칭자리", "쌍둥이자리"),
    ("전갈자리", "물고기자리"),
    ("사수자리", "사자자리"),
]

# --- Streamlit App ---

st.set_page_config(page_title="생일로 보는 러브 운명", page_icon="💘", layout="centered")

st.markdown("""
    <h1 style="text-align:center; color:#e91e63;">🎀 생일로 보는 러브 운명 💘</h1>
    <p style="text-align:center; font-size:18px;">당신의 생일 속에 숨어 있는 오늘의 연애 기운을 확인해보세요!</p>
""", unsafe_allow_html=True)

name = st.text_input("당신의 이름을 입력해주세요 💁‍♀️", "")
birth_date = st.date_input("생년월일을 선택해주세요 📅")

if st.button("✨ 러브 운명 확인하기 ✨"):
    if name:
        birth_month = birth_date.month
        birth_day = birth_date.day
        birth_year = birth_date.year

        # 별자리 계산
        user_zodiac, emoji = get_zodiac_sign(birth_month, birth_day)

        # 연애운 점수 생성
        score_seed = int(f"{birth_month}{birth_day}{birth_year}")
        random.seed(score_seed)
        love_score = random.randint(60, 100)

        # 조언 문구
        advice = random.choice(advice_list)

        # 궁합 별자리
        match = next((z for z in zodiac_compatibility if z[0] == user_zodiac), ("궁합 없음", "없음"))

        st.markdown("---")
        st.markdown(f"""
        <div style='text-align:center;'>
            <h2>{emoji} <strong>{user_zodiac}</strong>의 {name}님 💖</h2>
            <p style="font-size:22px;">오늘의 연애운 점수는...</p>
            <h1 style="color:#ff4081;">💘 {love_score}점 💘</h1>
            <p style="font-size:20px;">🔮 {advice}</p>
            <p style="font-size:18px;">💕 오늘의 찰떡궁합: <strong>{match[1]}</strong>자리</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("이름을 입력해주세요! 💡")

