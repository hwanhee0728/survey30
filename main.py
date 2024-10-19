import streamlit as st
from PIL import Image
import pandas as pd
import os
import datetime

# 로컬에서는 아래 내용이 있어야 함
# from dotenv import load_dotenv  
# load_dotenv()  

# 데이터 저장 함수
def save_data(new_data):
    try:
        existing_data = pd.read_excel("survey_01.xlsx")
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    except FileNotFoundError:
        updated_data = new_data

    updated_data.to_excel("survey_01.xlsx", index=False)
    st.success("설문 응답이 저장되었습니다.")

# 엑셀 파일 다운로드를 위한 함수
def download_excel():
    filename = 'survey_01.xlsx'
    with open(filename, "rb") as file:
        btn = st.download_button(
                label="설문 결과 다운로드",
                data=file,
                file_name=filename,
                mime="application/vnd.ms-excel"
            )

admin_key = os.getenv('ADMIN') 

def app():

    st.header(":parachute: KMLA Campus 360 :::Survey::: :yum:")
    image = Image.open('survey01.png')
    image = image.resize((200, 200))
    st.image(image)
    
    # KMLA Map 링크 추가
    if st.button('KMLA 지도를 보려면 클릭하세요'):
        # 버튼 클릭 시 이미지 표시
        map_image = Image.open('kmlamap.png')
        st.image(map_image, caption="KMLA 지도", use_column_width=True)

    # 사용자 입력 양식
    with st.form(key='survey_form'):
        st.write(":mega: KMLA Campus 360 개발 설문조사 (28기 구환희, 권휘우, 조재후)")
        st.markdown("<p style='font-size:14px; color:blue;'>안녕하세요! 민사고안에서 360도 파노라마 사진을 볼 수 있는 로드뷰와 항공뷰를 제작하고 있습니다.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:14px; color:blue;'>(:::::네이버 거리뷰/항공뷰 같은:::::) 공유하고 싶은 멋진 장소, 아름다운 장소, 의미있는 장소/설치물, </p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:14px; color:blue;'>내가 좋아하는 산책길 등을 알려주시면, 제작에 도움이 많이 될것 같습니다.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:14px; color:blue;'>답변주신 분들께는 선별을 통해 감사의 :::::답례:::::를 드리겠습니다!!! 많은 호응 부탁드려요!</p>", unsafe_allow_html=True)
        st.write("")
        name = st.text_area(":one: 이름 (학생일 경우 기수 포함)")
        st.write("")
        recommend01 = st.text_area(":two: :::로드뷰::: 멋진 장소, 의미있는/도움되는 장소, 산책길 등을 추천해 주실래요? (추천사유 포함)")
        st.write("")
        recommend02 = st.text_area(":three: :::항공뷰::: 드론 360도 파노라마 뷰을 보고 싶은 장소를 말씀해주실래요? (추천사유 포함)")
        st.write("")
        recommend03 = st.text_area(":four: :::컨텐츠::: 로드뷰/항공뷰 웹페이지에서 추가서비스하면 좋을 컨텐츠가 있을까요? (예: 민사고 날씨)")
        st.write("")
        recommend04 = st.text_area(":five: :::기타::: 기타 의견이 있다면 자유롭게 적어주세요!")
        st.write("")
        st.write(":smile::smile::smile:아래 '저장하기' 클릭해 주세요! 감사합니다!!!")
        submit_button = st.form_submit_button(label='저장하기')

        # 제출 버튼이 눌렸을 때의 처리
        if submit_button:
            current_time = datetime.datetime.now() 
            new_data = pd.DataFrame({
                "이름": [name],
                "추천1": [recommend01],
                "추천2": [recommend02],
                "추천3": [recommend03],
                "추천4": [recommend04],                
                "응답 시간": [current_time] 
            })
            # 파일에 데이터 저장
            save_data(new_data)        

    # 엑셀 다운로드
    password = st.text_input(":lock: 관리자", type="password")
    if password:
        if password == admin_key:
            # 비밀번호가 맞으면 다운로드 버튼 표시
            st.success("비밀번호 확인 완료")
            download_excel()
        else:
            st.error("에러")

if __name__ == "__main__":
    app()
