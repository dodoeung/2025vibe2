import streamlit as st
from datetime import datetime, date
import random

# 별자리 계산 함수
def get_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "물병자리", "🏺"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "물고기자리", "🐟"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "양자리", "🐏"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "황소자리", "🐂"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "쌍둥이자리", "👯‍♀️"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "게자리", "🦀"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "사자자리", "🦁"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "처녀자리", "👰"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "천칭자리", "⚖️"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "전갈자리", "🦂"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "사수자리", "🏹"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "염소자리", "🐐"
    else:
        return "알 수 없음", ""

# 별자리 성격 설명
zodiac_traits = {
    "물병자리": "독창적이고 자유로운 영혼이에요. 연애에서도 특별한 감성을 추구하죠.",
    "물고기자리": "감수성 풍부하고 다정해요. 상대를 깊이 이해하고 배려할 줄 알아요.",
    "양자리": "열정적이고 직진형! 마음이 생기면 바로 표현하는 타입이에요.",
    "황소자리": "신중하고 안정적인 스타일. 한 번 마음 주면 오래 가요.",
    "쌍둥이자리": "매력적이고 유쾌해요. 대화와 소통을 중시하는 스타일!",
    "게자리": "따뜻하고 감성적인 스타일. 가정적이고 배려심 깊어요.",
    "사자자리": "자신감 넘치고 카리스마 있어요. 연애에서도 주도적인 편이에요.",
    "처녀자리": "섬세하고 현실적인 연애를 추구해요. 계획적인 사랑을 좋아하죠.",
    "천칭자리": "로맨틱하고 센스 있어요. 조화를 중요시하는 스타일이에요.",
    "전갈자리": "강렬하고 진지한 사랑을 추구해요. 독점욕도 살짝 있는 편!",
    "사수자리": "자유롭고 쿨한 연애를 즐겨요. 유쾌한 에너지가 넘쳐요.",
    "염소자리": "책임감 있고 진중한 스타일. 신뢰를 기반으로 한 사랑을 중요시해요.",
}

# 찰떡궁합
zodiac_compatibility = {
    "물병자리": ("쌍둥이자리", "자유로운 두 사람, 서로의 생각을 자극해요!"),
    "물고기자리": ("게자리", "서로의 감성을 따뜻하게 보듬어주는 궁합이에요."),
    "양자리": ("사자자리", "열정이 폭발하는 불꽃 케미!"),
    "황소자리": ("처녀자리", "안정과 현실을 함께 추구하는 든든한 궁합이에요."),
    "쌍둥이자리": ("천칭자리", "센스와 소통이 넘치는 찰떡궁합!"),
    "게자리": ("물고기자리", "감성의 깊이를 함께 나누는 이상적인 짝이에요."),
    "사자자리": ("양자리", "에너지와 자신감이 잘 맞아요!"),
    "처녀자리": ("염소자리", "현실적이면서도 믿음직한 조합이에요."),
    "천칭자리": ("쌍둥이자리", "대화가 끊이지 않는 소울메이트 궁합!"),
    "전갈자리": ("물고기자리", "감정의 깊이를 이해해주는 이상적인 파트너예요."),
    "사수자리": ("사자자리", "유쾌하고 자유로운 여행 같은 연애!"),
    "염소자리": ("황소자리", "신뢰와 안정이 바탕인 단단한 사랑이에요."),
}

# 조언 문구
advice_list = [
    "오늘은 웃는 얼굴이 사랑을 부를 거예요 😊",
    "적극적으로 다가가면 운명의 문이 열릴지도 몰라요 💌",
    "마음을 표현할 용기가 사랑을 부르게 될 거예요 🗣️",
    "먼저 인사해보세요. 모든 인연은 작은 용기에서 시작돼요 🙋‍♀️",
    "지금의 당신은 사랑을 받을 자격이 충분해요 💖",
    "진심은 반드시 닿아요. 솔직해지는 걸 두려워하지 마세요 🌈",
    "사랑은 준비된 사람에게 찾아와요. 당신은 충분히 준비됐어요 🕊️",
    "사랑은 기다림이 아니라, 선택이에요. 당신이 움직일 차례에요 🚶‍♀️",
    "잠시의 용기가 오랫동안의 행복을 가져다줄 수 있어요 🧡",
    "오늘의 노력은 내일의 설렘으로 돌아올 거예요 ✨",
]

# 고백 팁
confession_tips = [
    "진심을 담은 짧은 문자로 마음을 전해보세요. 너무 길 필요 없어요 💌",
    "따뜻한 커피 한 잔 건네며 자연스럽게 고백해보세요 ☕",
    "산책하며 조용한 순간에 조심스럽게 이야기해보세요 🌙",
    "‘사실 너 좋아해’ 라고 담백하게 말해보세요 🎯",
    "대화 중 진지한 눈빛으로 분위기 전환해보세요 🎭",
    "‘요즘 네 생각 자주 나더라’로 슬쩍 시작해보세요 💬",
    "서툴러도 괜찮아요. 진심이면 충분해요 🫶",
    "‘용기내서 말해보려 해… 좋아해’ ✨",
    "손글씨 메시지 카드에 고백을 담아보세요 ✍️",
    "눈 마주치고 짧게, '나 너 좋아해.' ❤️",
]

# Streamlit 시작
st.set_page_config(page_title="생일로 보는 러브 운명", page_icon="💘", layout="centered")

st.markdown("""
    <h1 style="text-align:center; color:#e91e63;">🎀 생일로 보는 러브 운명 💘</h1>
    <p style="text-align:center; font-size:18px;">당신의 생일 속에 숨어 있는 오늘의 연애 기운과 고백 운명을 확인해보세요!</p>
""", unsafe_allow_html=True)

name = st.text_input("💁‍♀️ 당신의 이름을 입력해주세요", "")
birth_date = st.date_input(
    "🎂 생년월일을 선택해주세요",
    value=date(2000, 1, 1),
    min_value=date(1950, 1, 1),
    max_value=date.today()
)

if st.button("✨ 러브 운명 확인하기 ✨"):
    if name and birth_date:
        try:
            month = birth_date.month
            day = birth_date.day
            year = birth_date.year

            sign, emoji = get_zodiac_sign(month, day)
            trait = zodiac_traits.get(sign, "사랑스러운 성격이에요 💗")
            compat_sign, compat_desc = zodiac_compatibility.get(sign, ("", ""))
            seed_str = f"{month:02}{day:02}{year}"
            random.seed(int(seed_str))
            love_score = random.randint(65, 99)
            advice = random.choice(advice_list)
            confession = random.choice(confession_tips)

            st.markdown("---")
            st.markdown(f"""
                <div style='text-align:center;'>
                    <h2>{emoji} <strong>{sign}</strong>의 {name}님 💖</h2>
                    <p style="font-size:18px;">✨ {trait}</p>
                    <h1 style="color:#ff4081; margin-top:24px;">💘 오늘의 연애운 점수: <strong>{love_score}점</strong></h1>
                    <p style="font-size:20px; margin-top:16px;">🔮 조언: {advice}</p>
                    <p style="font-size:18px; margin-top:24px;">💕 찰떡궁합 별자리: <strong>{compat_sign}</strong></p>
                    <p style="font-size:16px; color:#666;">{compat_desc}</p>
                    <div style='margin-top:32px;'>
                        <h3>💌 고백 TIP</h3>
                        <p style="font-size:18px;">{confession}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"문제가 발생했어요: {e}")
    else:
        st.warning("이름과 생년월일을 모두 입력해주세요 😊")




