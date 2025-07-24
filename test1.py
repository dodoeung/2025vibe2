import streamlit as st
from PIL import Image
import os

# 페이지 설정
st.set_page_config(page_title="기분별 음식 추천", page_icon="🍱", layout="wide")

# 스타일
st.markdown("""
    <style>
    html, body {
        background: linear-gradient(to right, #ffe8ec, #e0f7fa);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: #ff4081;
        text-shadow: 2px 2px #ffd1dc;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #555;
        margin-bottom: 30px;
    }
    .recommend-box {
        background-color: #ffffffcc;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 2px 4px 20px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 출력
st.markdown('<div class="title">🌈 오늘의 기분에 따라 음식 추천받기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">기분을 골라보세요! 귀여운 음식과 함께하는 감성 추천🍓</div>', unsafe_allow_html=True)

# 기분-음식 데이터
feeling_data = {
    "🧠 뇌가 과열된 날": {
        "food": "비빔냉면",
        "desc": "매콤하고 시원한 냉면으로 머릿속 열을 식혀보아요!",
        "img": "1684ba00-8529-4d03-88d7-4b5a0889132e.png"
    },
    "🐢 느리게 살고 싶은 날": {
        "food": "수플레 팬케이크",
        "desc": "폭신폭신 천천히 즐기는 힐링 디저트!",
        "img": "289484d6-0b8b-4080-a882-6465ec3c6cf2.png"
    },
    "🛸 현실도피 하고 싶은 날": {
        "food": "타코야끼",
        "desc": "지구를 떠나 일본 야시장에 온 듯한 기분~",
        "img": "654d9f2b-24a7-4ce9-8c4c-14437a2edff7.png"
    },
    "🎢 감정이 널뛰는 날": {
        "food": "떡볶이",
        "desc": "단짠맵 감정도 같이 롤러코스터 타자!",
        "img": "b5e13f19-90a4-4626-84d7-8dc7fd836eb4.png"
    },
    "🧚 공상에 빠진 날": {
        "food": "마카롱",
        "desc": "달콤하고 동화 같은 색감의 판타지 간식",
        "img": "5e626b7a-5b22-4c0f-869b-3b08ee5a25f0.png"
    },
    "🤹 아무 것도 하기 싫은 날": {
        "food": "라면",
        "desc": "물만 부으면 완성! 간편하고 따뜻한 위로",
        "img": "fb2e7779-c9b6-45c6-be01-0b2f8467fd14.png"
    }
}

# 기분 선택 UI
feeling = st.selectbox("지금 당신의 기분은?", list(feeling_data.keys()))

# 결과 출력
if feeling:
    data = feeling_data[feeling]
    
    # 박스 스타일 설명
    st.markdown(f"""
        <div class="recommend-box">
            <h2 style='color:#ff4081;'>🍽 오늘의 추천: {data['food']}</h2>
            <p style='font-size:18px;'>💬 {data['desc']}</p>
        </div>
    """, unsafe_allow_html=True)

    # 이미지 출력
    image_path = os.path.join(".", data["img"])
    if os.path.exists(image_path):
        st.image(Image.open(image_path), use_column_width=False, width=300)
    else:
        st.warning(f"⚠️ 이미지 파일이 존재하지 않아요: {data['img']}")



