import streamlit as st
from modules.analyzer import analyze_logs

def main():
    st.title("AI 기반 보안 로그 분석")
    
    # 1) 로그 입력받기
    user_input = st.text_area("분석할 보안 로그를 입력하세요 (또는 업로드)")

    # 2) 분석 버튼
    if st.button("분석하기"):
        if user_input.strip():
            # GPT 분석 로직 호출
            summary, risk_level, recommendation = analyze_logs(user_input)

            # 결과 표시
            st.subheader("분석 결과 요약")
            st.write(summary)
            st.write(f"**위협 등급**: {risk_level}")
            st.write(f"**권장 대응**: {recommendation}")
        else:
            st.warning("로그가 입력되지 않았습니다.")

if __name__ == "__main__":
    main()
