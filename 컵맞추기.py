import streamlit as st
import random
import time

st.set_page_config(page_title="🍬 컵 속 사탕 찾기 대작전!", layout="centered")
st.title("🍬 컵 속 사탕 찾기 대작전!")

# 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'candy_pos' not in st.session_state:
    st.session_state.candy_pos = None
if 'shuffled' not in st.session_state:
    st.session_state.shuffled = False
if 'streak' not in st.session_state:
    st.session_state.streak = 0  # 연속 정답 수

# 현재 난이도 = 컵 섞는 횟수
def get_shuffle_count():
    base = 3
    extra = min(st.session_state.streak, 5) * 2  # 최대 5단계까지 증가
    return base + extra  # 3~13회 섞기

# 게임 시작
if st.button("🎲 게임 시작!"):
    st.session_state.candy_pos = random.randint(0, 2)
    st.session_state.shuffled = False
    st.experimental_rerun()

# 셔플 애니메이션
if st.session_state.candy_pos is not None and not st.session_state.shuffled:
    st.markdown("🔄 컵을 섞는 중... (난이도 단계: **" + str(st.session_state.streak + 1) + "**)")

    cups = ['🥤', '🥤', '🥤']
    shuffle_times = get_shuffle_count()

    for i in range(shuffle_times):
        random.shuffle(cups)
        st.markdown("".join(cups))
        time.sleep(0.3)
    st.session_state.shuffled = True
    st.experimental_rerun()

# 컵 선택
if st.session_state.shuffled:
    st.markdown("👇 사탕이 들어있는 컵을 골라보세요!")
    col1, col2, col3 = st.columns(3)

    def check_choice(choice_idx):
        if choice_idx == st.session_state.candy_pos:
            st.success("정답! 🎉 사탕을 찾았어요!")
            st.session_state.score += 1
            st.session_state.streak += 1
        else:
            st.error("앗! 틀렸어요 😢")
            st.session_state.score -= 1
            st.session_state.streak = 0  # 틀리면 연속 정답 초기화
        st.session_state.candy_pos = None
        st.session_state.shuffled = False

    with col1:
        if st.button("1번 컵 🥤"):
            check_choice(0)
    with col2:
        if st.button("2번 컵 🥤"):
            check_choice(1)
    with col3:
        if st.button("3번 컵 🥤"):
            check_choice(2)

# 점수판
st.markdown("### 🍭 현재 점수:")
score = st.session_state.score
if score > 0:
    st.markdown("**🍬 " * score + f"→ 총 {score}점**")
elif score < 0:
    st.markdown("**💔 " * abs(score) + f"→ 총 {score}점**")
else:
    st.markdown("_아직 점수가 없어요. 도전해보세요!_")

# 리셋 버튼
if st.button("🔄 점수 초기화"):
    st.session_state.score = 0
    st.session_state.streak = 0
    st.success("점수가 초기화되었습니다!")
