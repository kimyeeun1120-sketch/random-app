import random
import streamlit as st
import pandas as pd

# 1. 데이터 구조 (리스트)
food_list = ["딱딱한 사료", "파프리카", "당근"]
age_group_list = ["1~7세", "8~15세", "16~20세"]


# 2. 함수 (def) - snake_case 규칙 준수
def check_dog_food(food_name, age_group):
    # 3. 조건문 (if-elif-else)으로 연령대 및 음식 적합도 판별
    if age_group == "1~7세":
        guide_msg = "성견 시기(1~7세)는 치아와 소화력이 튼튼해 다양한 음식을 잘 섭취할 수 있습니다."
        if food_name == "딱딱한 사료":
            score = 95
        elif food_name == "파프리카":
            score = 90
        else:
            score = 90

    elif age_group == "8~15세":
        guide_msg = "노령견 시기(8~15세)는 치아와 잇몸이 약해지기 시작하므로 부드러운 음식이 좋습니다."
        if food_name == "딱딱한 사료":
            score = 40
        elif food_name == "파프리카":
            score = 85
        else:
            score = 80

    else:  # 16~20세
        guide_msg = "초고령견 시기(16~20세)는 소화 기능과 치아가 매우 약하므로 유동식이나 익힌 음식이 필수입니다."
        if food_name == "딱딱한 사료":
            score = 20
        elif food_name == "파프리카":
            score = 75
        else:
            score = 85

    return score, guide_msg


# --- Streamlit 웹 화면 구성 ---
st.title("🐶 강아지 연령에 따라 권장하는 음식 가이드")
st.write("반려견의 나이와 음식을 선택하면 섭취 가능 여부와 이유를 알려드립니다.")

# 사용자 입력 받기 (드롭다운 & 슬라이더)
selected_food = st.selectbox("1. 음식을 선택하세요:", food_list)
selected_age = st.select_slider("2. 강아지 연령대를 선택하세요:", options=age_group_list)

# 분석하기 버튼 클릭 시 실행
if st.button("분석하기"):
    # 함수 호출
    food_score, message = check_dog_food(selected_food, selected_age)

    st.subheader(f"📋 [{selected_age}] 맞춤 분석 결과")
    st.info(message)

    # 강조 수치(Metric) 표시
    st.metric(label=f"선택한 음식({selected_food}) 섭취 적합도", value=f"{food_score}점")

    # 4. 반복문 (for)을 활용해 연령대별 음식 권장 목록 표 데이터 생성
    table_data = []
    for item in food_list:
        if selected_age == "1~7세":
            if item == "딱딱한 사료":
                status, reason = "권장", "치석 제거와 턱 근육 발달에 도움됨"
            elif item == "파프리카":
                status, reason = "권장", "수분과 비타민 보충에 좋음 (씨 제거 필수)"
            else:
                status, reason = "권장", "베타카로틴이 풍부해 눈 건강에 좋음"

        elif selected_age == "8~15세":
            if item == "딱딱한 사료":
                status, reason = "비권장", "약해진 치아와 잇몸에 무리가 갈 수 있음"
            elif item == "파프리카":
                status, reason = "권장", "항산화 성분이 풍부해 노화 방지에 도움됨"
            else:
                status, reason = "주의", "소화를 위해 잘게 썰거나 익혀서 급여 권장"

        else:  # 16~20세
            if item == "딱딱한 사료":
                status, reason = "위험", "치아 손상 및 소화 불량 위험이 매우 높음"
            elif item == "파프리카":
                status, reason = "주의", "껍질을 벗기고 아주 잘게 다져서 소량 급여"
            else:
                status, reason = "권장", "푹 익혀서 으깨 주면 소화가 잘되고 영양 보충됨"

        table_data.append({
            "음식명": item,
            "권장 여부": status,
            "이유": reason
        })

    # 테이블(표) 형태로 출력
    st.write(f"### 🥗 {selected_age} 강아지 음식별 권장 가이드")
    df = pd.DataFrame(table_data)
    st.table(df)

    # random 라이브러리 활용: 오늘의 추천 급여 팁
    random_tip = random.choice([
        "새로운 음식을 줄 때는 소량만 먼저 급여해 알레르기 반응을 확인하세요.",
        "강아지에게 음식을 줄 때는 간을 하지 않은 자연 상태 그대로 주어야 합니다.",
        "물을 자주 마실 수 있도록 깨끗한 물을 항상 옆에 두세요."
    ])
    st.success(f"💡 오늘의 건강 팁: {random_tip}")
