import streamlit as st

st.set_page_config(page_title="어버이날 편지", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #fff5e6;
    }
    </style>
""", unsafe_allow_html=True)

st.image("https://cdn.pixabay.com/photo/2017/03/21/06/47/carnation-2163802_1280.jpg", use_column_width=True)

st.markdown("<h1 style='text-align: center; color: #d6336c;'>어버이날 편지</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>사랑하는 부모님께</h2>", unsafe_allow_html=True)

st.markdown("""
<div style='font-size: 18px; line-height: 1.9; padding: 20px; background-color: #fff; border-radius: 12px; box-shadow: 2px 2px 8px rgba(0,0,0,0.1);'>
항상 저를 위해 노력하고 따뜻하게 챙겨주셔서 감사해요.<br><br>

아빠 항상 저를 위해 피곤하실 때도 같이 놀아주셔서 감사해요. 또 재미있는 말로 우리 가족을 항상 웃게 해줘서 감사해요. 아빠가 있어 든든해요.<br><br>

엄마도 저를 위해 매일 광주에서 정읍까지 출퇴근하시고, 항상 제가 공부에 집중할 수 있도록 도와주셔서 감사해요. 그리고 분명히 피곤하실 텐데도 집안일까지 해주셔서 감사해요.<br><br>

이 도움과 감사함을 다 갚을 수 있을지는 모르겠지만, 열심히 공부해서 부모님의 기쁨이 되도록 할게요.<br><br>

항상 감사하고 사랑합니다.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: right; font-size: 16px; color: gray;'>
2025/5/6<br>
엄마아빠를 <b style='color:crimson;'>매우매우매우 아주아주아주 너무너무너무</b> 사랑하는 아들 이태경 올림
</p>
""", unsafe_allow_html=True)
