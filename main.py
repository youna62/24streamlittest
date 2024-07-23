import streamlit as st

# MBTI 설명 데이터
mbti_descriptions = {
    "ISTJ": "현실적이고 책임감이 강하며 신뢰할 수 있는 관리자 타입.",
    "ISFJ": "친절하고 성실하며 헌신적인 보호자 타입.",
    "INFJ": "창의적이고 통찰력이 있으며 영감을 주는 조언자 타입.",
    "INTJ": "분석적이고 전략적이며 독립적인 사색가 타입.",
    "ISTP": "논리적이고 실용적이며 문제 해결을 잘하는 장인 타입.",
    "ISFP": "온화하고 예술적이며 호기심 많은 예술가 타입.",
    "INFP": "이상적이고 충실하며 공감 능력이 뛰어난 중재자 타입.",
    "INTP": "이론적이고 논리적이며 호기심 많은 철학자 타입.",
    "ESTP": "활동적이고 모험적이며 에너지가 넘치는 촉매제 타입.",
    "ESFP": "사교적이고 긍정적이며 삶을 즐기는 연예인 타입.",
    "ENFP": "열정적이고 창의적이며 사람을 끌어들이는 활동가 타입.",
    "ENTP": "영리하고 호기심이 많으며 창의적인 발명가 타입.",
    "ESTJ": "실용적이고 조직적이며 리더십이 강한 경영자 타입.",
    "ESFJ": "친절하고 사교적이며 헌신적인 돌보는 자 타입.",
    "ENFJ": "카리스마 있고 열정적이며 타인을 돕는 것을 즐기는 주도자 타입.",
    "ENTJ": "결단력 있고 효율적이며 리더십이 뛰어난 지휘관 타입."
}

# MBTI 궁합 데이터 (단순화된 예시)
best_matches = {
    "ISTJ": "ESTP 또는 ESFP",
    "ISFJ": "ESFP 또는 ESTP",
    "INFJ": "ENFP 또는 ENTP",
    "INTJ": "ENFP 또는 ENTP",
    "ISTP": "ESFJ 또는 ESTJ",
    "ISFP": "ENFJ 또는 ESFJ",
    "INFP": "ENTJ 또는 ENFJ",
    "INTP": "ENTJ 또는 ENFJ",
    "ESTP": "ISFJ 또는 ISTJ",
    "ESFP": "ISFJ 또는 ISTJ",
    "ENFP": "INFJ 또는 INTJ",
    "ENTP": "INFJ 또는 INTJ",
    "ESTJ": "ISFP 또는 ISTP",
    "ESFJ": "ISFP 또는 INFP",
    "ENFJ": "INFP 또는 INTP",
    "ENTJ": "INFP 또는 INTP"
}

# 스트림릿 애플리케이션
def main():
    st.title("MBTI 성향 및 궁합 테스트")

    name = st.text_input("이름을 입력하세요:")
    mbti = st.selectbox("MBTI 타입을 선택하세요:", list(mbti_descriptions.keys()))

    if name and mbti:
        st.subheader(f"{name}님의 MBTI 성향")
        st.write(mbti_descriptions[mbti])

        st.subheader(f"{name}님과 가장 잘 맞는 타입")
        st.write(best_matches[mbti])

if __name__ == "__main__":
    main()
