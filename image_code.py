# 기본 import
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from bokeh.plotting import figure
import random
from konlpy.tag import Komoran
tagger = Komoran()
from collections import Counter
from wordcloud import WordCloud
import networkx as nx
import re

from importlib import reload
plt=reload(plt)

plt.rcParams["font.family"] = 'NanumGothic'

# 제목
st.title("영화 데이터 분석")


# 1번: 관객수
st.subheader("1. 연도별 평균 관객수를 알아보자.")

from PIL import Image

image11 = Image.open('data/audience_graph1.png')
st.image(image11, caption = '1980-2002년 평균 관객수(서울) 라인그래프')

st.write("평균 관람객 수는 80년대에는 계속해서 비슷한 수준에 머무르다, 90년대가 되면서 점차 가파른 상승세를 타기 시작했다.")

image12 = Image.open('data/audience_graph2.png')
st.image(image12, caption = '2003-2022년 평균 관객수(전국) 라인그래프')

st.write("전국 관람객 수 집계가 시작된 2003년부터도 평균 관람객 수는 꾸준한 상승세를 탔고, 특히 2012년으로 넘어가면서 꾸준히 300만 이상을 기록했다.")
st.write("코로나19가 시작된 2020년에 평균 관객수는 1/4 수준으로 급감했으나, 2022년부터 다시 상승세를 타고 있다.")


# 2번: 연령대
st.subheader("2. 연도별 연령대 순위를 알아보자.")

image1 = Image.open('data/agecount_80.png')
st.image(image1, caption = '80년대 연령등급 파이차트')

image2 = Image.open('data/agecount_90.png')
st.image(image2, caption = '90년대 연령등급 파이차트')

image3 = Image.open('data/agecount_00.png')
st.image(image3, caption = '00년대 연령등급 파이차트')

image4 = Image.open('data/agecount_10.png')
st.image(image4, caption = '10년대 연령등급 파이차트')

st.write("시대가 지남에 따라 '청소년 관람불가' 영화들의 비율이 점점 줄어드는 것이 눈에 띈다.")

# 4번: 시놉시스 키워드
st.subheader("4. 연도별 유행 시놉시스 키워드를 알아보자.")

st.write("1980년-2022년 동안 국내 영화에서 유행한 시놉시스 키워드는 다음과 같다.")
image5 = Image.open('data/word_kr.png')
st.image(image5, caption = '국내 키워드 워드클라우드')

st.write("1980년-2022년 동안 국외 영화에서 유행한 시놉시스 키워드는 다음과 같다.")
image6 = Image.open('data/word_fo.png')
st.image(image6, caption = '국외 키워드 워드클라우드')

st.write("국내 영화에 비해 국외 영화의 시놉시스에서는 전반적으로 '세계'라는 키워드가 많이 등장하는 것으로 보여진다.")


st.write("1980-1999년 동안 유행했던 시놉시스 키워드는 다음과 같다.")
image7 = Image.open('data/word_80.png')
st.image(image7, caption = '80년대 키워드 워드클라우드')
st.write("상대적으로 과거라 그런지, 다른 시대에 비해 아버지, 남편, 아내, 아들 등 가족을 나타내는 키워드가 많이 등장함을 확인할 수 있다.")

st.write("1990-1999년 동안 유행했던 시놉시스 키워드는 다음과 같다.")
image8 = Image.open('data/word_90.png')
st.image(image8, caption = '90년대 키워드 워드클라우드')
st.write("80년대에 비해 가족을 나타내는 키워드들의 크기가 확연히 줄어들고, 범죄 영화 등의 핵심 키워드인 '사건'이 메인 키워드급으로 커진 것이 눈에 띈다.")

st.write("2000-2009년 동안 유행했던 시놉시스 키워드는 다음과 같다.")
image9 = Image.open('data/word_00.png')
st.image(image9, caption = '00년대 키워드 워드클라우드')
st.write("앞선 워드클라우드에서는 거의 보이지 않았던 '세계'와 '세상'이 점점 커지고 있는 것이 보인다.")

st.write("2010-2022년 동안 유행했던 시놉시스 키워드는 다음과 같다.")
image10 = Image.open('data/word_10.png')
st.image(image10, caption = '10년대 키워드 워드클라우드')
st.write("앞선 세 워드클라우드에서 모두 큰 비중을 차지했던 '사랑'이라는 키워드의 크기가 급감한 것이 가장 뚜렷한 특징이다. 또 2000년대에 점점 커지고 있던 '세계'와 '세상'이라는 키워드가 이제 메인 키워드급으로 커진 것도 눈에 띈다.")