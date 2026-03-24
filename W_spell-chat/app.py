import streamlit as st
from corrector import correct_text

st.set_page_config(page_title="한글 맞춤법 채팅", page_icon="✍️")
st.title("한글 자동 맞춤법 채팅")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "문장을 입력하면 먼저 띄어쓰기 중심으로 교정해 드립니다."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("예: 오늘날씨가좋아서산책가고싶다")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    result = correct_text(prompt)

    if result["changed"]:
        reply = (
            f"원문:\n\n{result['original']}\n\n"
            f"교정:\n\n{result['corrected']}"
        )
    else:
        reply = f"교정 결과: 변경 없음\n\n문장:\n\n{result['original']}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()