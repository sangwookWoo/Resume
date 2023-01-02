import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
from PIL import Image


filePath, fileName = os.path.split(__file__)
def main():
    
    # 페이지 기본 설정
    st.set_page_config(
        page_title = "😊우상욱입니다",
        layout = 'centered'
    )
        
    st.header("🎉우상욱 | 데이터를 사랑하는 엔지니어")
    st.markdown("저에게 가장 재밌는 일은 **데이터에 관한 문제**를 해결하는 일입니다😊")
    image = Image.open(os.path.join(filePath,'data','우상욱사진2.png'))
    st.markdown('* * *')
    col1, col2 = st.columns(2)
    with col1:
        st.image(image)
    with col2:
        st.markdown('**👨‍🎓Education**<br>- 동국대학교 경영학부(경영정보학과) 졸업예정<br>- 엔코아 플레이데이터 20기<br>Data Engineering Track(23.01~23.06)', unsafe_allow_html= True)
        st.markdown('**📞Contact**<br>**Phone** : 010-6659-6977<br>**Email** : wjddm3@naver.com', unsafe_allow_html= True)
        st.markdown('**🌏Social**<br>**Blog** : 개설 예정<br>**GitHub** : https://github.com/sangwookWoo', unsafe_allow_html=True)
        st.markdown('**👔Career**<br>**- 데이터누리**<br>22.04 ~ 22.12(8개월, 데이터비즈팀, 인턴)<br>**- 서울산업진흥원**<br>21.07 ~ 22.12(6개월, 창업육성팀, 학생인턴)', unsafe_allow_html= True)
    st.markdown('* * *')
    
    
    st.subheader('📒Introduce')
    st.markdown('> **데이터 엔지니어를 하고자 하는 이유는?**', unsafe_allow_html = True)
    st.markdown('[데이터 인프라 구축을 통해, 고객과 기업 모두에게 더 나은 데이터를 제공하려는 목표]')
    st.write('데이터 전문 회사에서 인턴으로 일하면서, **데이터인프라 설계**가 데이터 비즈니스에서 중요하다는 것을 깨달았습니다. 인공지능 모델에 들어갈 데이터 뿐만 아니라, 기업 내외부 이용자에게 전달되는 데이터까지, **잘 구축된 데이터 파이프라인 내에서 정제, 가공 그리고 전달** 하는 것이 **정확한 데이터**를 만드는 가장 효율적인 방식이라는 것을 알게 되었습니다. 데이터에 대해서 몰랐던 지식을 배우면서 데이터를 조금 더 효율적으로 다루는 경험들은 저에게 너무나도 설레는 경험들입니다. 팀원들과 함께 데이터 인프라를 구축하고 데이터를 최선의 상태로 만드는 일에 함께하고 싶습니다.')
    
    st.markdown('> **저는 이런 것들을 경험하길 기대합니다**', unsafe_allow_html = True)
    st.markdown('- 학습한 내용을 바탕으로 **데이터 인프라 구축**, 설계하고 유지보수하는 경험', unsafe_allow_html = True)
    st.markdown('- 팀원들과 **협업, 토론**을 통해 실제 서비스를 개선하고 성능을 향상시키는 경험', unsafe_allow_html = True)
    st.markdown('- 데이터파이프라인의 **스케줄과 의존도**를 이해하고, 이를 적절히 유지보수 하는 경험', unsafe_allow_html = True)
    st.markdown('- 사용자가 사용하기 가장 편리한 방식으로 **빅데이터를 정제 및 가공**하는 경험', unsafe_allow_html = True)
    st.button('더 자세한 자기소개서 보기(업데이트 예정)')
    
    
    st.markdown('* * *')
    st.subheader('⚒️Skill Set')
    image = Image.open(os.path.join(filePath,'data','skill.png'))
    st.image(image)
    
    
    
    st.markdown('* * *')
    st.subheader('💾Work Experience')
    
    st.markdown('자세한 내용은 링크를 들어가시면 볼 수 있습니다(업데이트 예정입니다!)😊')
    st.markdown('> **데이터누리**(2022.04 ~ 2022.12 인턴, 8개월)')
    st.markdown('- 빅데이터 전처리 자동화 및 처리 내역 레포트 추출(로그 기반) 프로그램 개발')
    st.markdown('- 라벨링 데이터 AI 모델 맞춤 가공 + 데이터 오류 수정')
    st.markdown('- 데이터 라벨링, 크라우드 워커 전용 보조프로그램 개발')
    st.markdown('- 고객사 요청 데이터 크롤링 프로그램 개발(Selenium)')
    st.markdown('- 빅데이터 플랫폼 적재')
    
    st.markdown('> **서울산업진흥원**(2021.07 ~ 2021.12 인턴, 6개월)')
    st.markdown('- 해당 부분은 직무와 연관성이 높진 않지만, 저를 소개하기 적합할 것 같아 문서를 올립니다😊')
    st.markdown('- 진로가 바뀌게 된 계기 : 작성 예정')
    with open(os.path.join(filePath, 'data', '서울산업진흥원.pdf'), "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="인턴쉽 보고서 다운로드",
                        data=PDFbyte,
                        file_name="서울산업진흥원_우상욱.pdf",
                        mime='application/octet-stream')
    
    st.markdown('* * *')
    st.subheader('✍️Personal Experience')
    st.markdown('- 2022 POSTECH OIBC CHALLENGE 태양광 발전량 예측경진대회 : 참가상')
    st.markdown('📖Blog : 작성 예정', unsafe_allow_html= True)
    st.markdown('- 국가 위기대응 프로젝트(공공데이터 API 활용 웹개발)')
    st.markdown('📖Blog : 작성 예정<br>🔍Website : https://sangwookwoo-disaster2-web-news-qp8onx.streamlit.app/<br>💻GitHub : 작성 예정', unsafe_allow_html= True)

    st.markdown('* * *')
    st.subheader('😤앞으로 목표')
    st.markdown('1. 기록해서 이 웹페이지를 완성하기', unsafe_allow_html= True)
    st.markdown('2. 플레이데이터에서 배운 내용들을 모두 이 페이지와 블로그에 담기', unsafe_allow_html= True)
    
if __name__ == "__main__":
    main()