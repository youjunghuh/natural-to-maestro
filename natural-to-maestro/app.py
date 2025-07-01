import streamlit as st
from maestro_prompt import generate_maestro_yaml

st.set_page_config(page_title="자연어 → Maestro YAML 변환기", layout="wide")
st.title("🧪 자연어 → Maestro YAML 변환기")

with st.expander("예시 시나리오"):
    st.markdown("""
    **예시**
    ```
    앱을 실행하고, 로그인 화면에서 이메일과 비밀번호를 입력한 후 로그인 버튼을 누른다.
    홈 화면으로 전환되는 것을 확인한다.
    ```
    """)

natural_input = st.text_area("✅ 자연어로 테스트 시나리오를 입력해주세요", height=250)

if st.button("🧙 YAML로 변환"):
    if not natural_input.strip():
        st.warning("시나리오를 입력해주세요!")
    else:
        with st.spinner("변환 중..."):
            yaml_result = generate_maestro_yaml(natural_input)
            st.code(yaml_result, language="yaml")
            st.success("✅ 변환 완료!")