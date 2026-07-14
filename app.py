import streamlit as st
from groq import Groq

# ----------------------------
# 페이지 설정
# ----------------------------
st.set_page_config(
    page_title="🧠 좌뇌 · 우뇌 사고 시뮬레이터",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------
# CSS
# ----------------------------
st.markdown("""
<style>

body{
    background:#FFF9FC;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#ff4d88;
}

.sub{
    text-align:center;
    font-size:18px;
    color:gray;
}

.card{
    border-radius:25px;
    padding:25px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
    min-height:500px;
}

.left{
    background:#DDEEFF;
}

.right{
    background:#F3E4FF;
}

.both{
    background:#E5FFE8;
}

h2{
    text-align:center;
}

</style>
""",unsafe_allow_html=True)

st.markdown("<div class='title'>🧠 좌뇌 · 우뇌 사고 시뮬레이터</div>",unsafe_allow_html=True)

st.markdown("<div class='sub'>같은 질문을 서로 다른 사고방식으로 생각해 보아요 🌸</div>",unsafe_allow_html=True)

st.divider()

client=Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

question=st.text_input(
    "💭 궁금한 것을 적어보세요!",
    placeholder="예) 사람은 왜 꿈을 꿀까?"
)

# ----------------------------
# GPT
# ----------------------------

def ask(question):

    prompt=f"""

다음 질문에 대해

1. 좌뇌
2. 우뇌
3. 통합

세 가지 관점으로 대답해라.

========================

질문

{question}

========================

좌뇌 특징

- 언어의 범주화
- 가상의 자아 생성
- 스토리텔링과 합리화
- 과거와 미래에 집착

우뇌 특징

- 패턴의 인식과 직관
- 현재에 머물기
- 연결성과 입체감
- 비언어적 소통

========================

중요한 규칙

- 반드시 한국어만 사용한다.
- 한자를 절대 사용하지 않는다.
- 어려운 단어보다 쉬운 표현을 사용한다.
- 한국어를 제외한 다른 언어를 사용하지 않는다.
- 학생도 이해할 수 있게 설명한다.
- 따뜻하고 자연스럽게 말한다.
- 최대한 간단하게 설명한다.

출력 형식

### 좌뇌

...

### 우뇌

...

### 통합

...

"""

    response=client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.7
    )

    return response.choices[0].message.content

# ----------------------------

if st.button("✨ 답변 보기",use_container_width=True):

    if question=="":

        st.warning("질문을 입력해주세요 😊")

    else:

        with st.spinner("🧠 생각하는 중..."):

            answer=ask(question)

        left=""
        right=""
        both=""

        section=""

        for line in answer.split("\n"):

            if "좌뇌" in line:
                section="left"
                continue

            elif "우뇌" in line:
                section="right"
                continue

            elif "통합" in line:
                section="both"
                continue

            if section=="left":
                left+=line+"\n"

            elif section=="right":
                right+=line+"\n"

            elif section=="both":
                both+=line+"\n"

        col1,col2,col3=st.columns(3)

        with col1:

            st.markdown("""
<div class='card left'>
<h2>🩵 좌뇌</h2>
""",unsafe_allow_html=True)

            st.write(left)

            st.markdown("</div>",unsafe_allow_html=True)

        with col2:

            st.markdown("""
<div class='card right'>
<h2>💜 우뇌</h2>
""",unsafe_allow_html=True)

            st.write(right)

            st.markdown("</div>",unsafe_allow_html=True)

        with col3:

            st.markdown("""
<div class='card both'>
<h2>💚 통합</h2>
""",unsafe_allow_html=True)

            st.write(both)

            st.markdown("</div>",unsafe_allow_html=True)

st.divider()

st.caption("🌸 Left Brain · Right Brain Simulator")
