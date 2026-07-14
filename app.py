import streamlit as st
from openai import OpenAI

# -----------------------
# 페이지 설정
# -----------------------
st.set_page_config(
    page_title="좌뇌 · 우뇌 사고 시뮬레이터",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main{
    background-color:#f8f9fc;
}

.card{
    border-radius:20px;
    padding:20px;
    color:black;
    min-height:500px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
}

.left{
    background:#dbeafe;
}

.right{
    background:#f3e8ff;
}

.both{
    background:#dcfce7;
}

.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🧠 좌뇌 · 우뇌 사고 시뮬레이터</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>같은 질문을 세 가지 사고방식으로 분석합니다.</div>", unsafe_allow_html=True)

st.divider()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input(
    "질문을 입력하세요",
    placeholder="예) 사람은 왜 사랑을 할까?"
)

# -----------------------
# GPT 함수
# -----------------------

def ask(prompt):

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content

# -----------------------
# 버튼
# -----------------------

if st.button("✨ 생성하기", use_container_width=True):

    if question=="":

        st.warning("질문을 입력해주세요!")

    else:

        with st.spinner("AI가 사고 중입니다..."):

            left = ask(f"""
너는 인간의 좌뇌처럼 사고한다.

좌뇌 특징

1. 언어와 범주화
2. 논리적 분석
3. 원인과 결과
4. 과거와 미래 분석
5. 합리적인 설명

질문

{question}
""")

            right = ask(f"""
너는 인간의 우뇌처럼 사고한다.

우뇌 특징

1. 직관
2. 현재 순간
3. 감정
4. 연결성
5. 비언어적 의미

질문

{question}
""")

            both = ask(f"""
너는 좌뇌와 우뇌가 동시에 작동하는 상태이다.

좌뇌

- 분석
- 논리
- 언어

우뇌

- 직관
- 감정
- 연결

두 사고를 모두 사용하여 가장 균형 잡힌 답변을 작성하라.

질문

{question}
""")

        col1,col2,col3 = st.columns(3)

        with col1:

            st.markdown("""
<div class="card left">
<h2>🧠 좌뇌</h2>
""",unsafe_allow_html=True)

            st.write(left)

            st.markdown("</div>",unsafe_allow_html=True)

        with col2:

            st.markdown("""
<div class="card right">
<h2>🎨 우뇌</h2>
""",unsafe_allow_html=True)

            st.write(right)

            st.markdown("</div>",unsafe_allow_html=True)

        with col3:

            st.markdown("""
<div class="card both">
<h2>⚖️ 통합</h2>
""",unsafe_allow_html=True)

            st.write(both)

            st.markdown("</div>",unsafe_allow_html=True)

st.divider()

st.caption("Made with ❤️ using Streamlit + OpenAI")
