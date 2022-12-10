

# 기본 import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from importlib import reload
from bokeh.plotting import figure
from bokeh.palettes import Dark2_5 as palette
import itertools
import json


st.markdown("# 시대별 top50 영화의 장르 및 시놉시스 키워드 트렌드를 알아보자")

st.markdown("## 시대별 top50 영화의 장르를 알아보자")

# 저장된 csv 파일 읽어서 dataframe 만들기
genre_perc_total = pd.read_csv("data/total_genre_percentage2.csv",sep="\t", index_col=0)
genre_perc_total_df = pd.DataFrame(genre_perc_total)

with st.expander("사용된 데이터 보기(단위 : %)"):
    st.write(genre_perc_total_df) #사용된 데이터프레임

selected_genre = st.radio("보고 싶은 장르 선택", ('드라마','액션','코미디','스릴러','멜로/로맨스','모험','범죄','판타지','SF','애니메이션','가족','공포',
            '미스터리','전쟁','뮤지컬'))
fig1 = figure(
    title= '시대별 '+ selected_genre +' 추이 그래프',
    x_axis_label = "years",
    y_axis_label = "percentage(%)"
)
fig1.line(genre_perc_total_df.index,genre_perc_total_df[selected_genre], legend_label = selected_genre, line_width = 1, line_color = "blue")
fig1.height = 400
st.bokeh_chart(fig1, use_container_width=True)

# multiselect
selected_genre_list = st.multiselect('다중선택 박스에서 추이를 함께 보고 싶으신 장르를 모두 선택하세요.', ['드라마','액션','코미디','스릴러','멜로/로맨스','모험','범죄','판타지','SF','애니메이션','가족','공포',
            '미스터리','전쟁','뮤지컬'])

fig2 = figure(
    title= '시대별 인기 장르 추이 그래프',
    x_axis_label = "years",
    y_axis_label = "percentage(%)"
)
colors = itertools.cycle(palette) # 항목마다 다른 색으로 라인이 그려질 수 있게 합니다
for i in range(len(selected_genre_list)): 
    fig2.line(genre_perc_total_df.index, genre_perc_total_df[selected_genre_list[i]],legend_label = selected_genre_list[i], line_width = 1, line_color = next(colors))

fig2.height = 400
st.bokeh_chart(fig2, use_container_width=True)

st.markdown("## 시대별 top50 영화의 시놉시스 트렌드를 알아보자")

# 저장된 csv 파일 읽어서 dataframe 만들기
txt_perc_total = pd.read_csv("data/total_txt_percentage2.csv",sep="\t", index_col=0)
txt_perc_total_df = pd.DataFrame(txt_perc_total)
with st.expander("사용된 데이터 보기(단위 : %)"):
    st.write(txt_perc_total_df) #사용된 데이터프레임

# multiselect
selected_txt_list = st.multiselect('다중선택 박스에서 추이를 함께 보고 싶으신 장르를 모두 선택하세요.', ['사랑', '사건', '친구', '사실', '아버지', '여자', '아들', '남자', 
             '발견', '세계', '세상', '아내', '인간', '죽음', '경찰', '마음', '생활', '조직', '결혼','가족'])

fig3 = figure(
    title= '시놉시스에 해당 단어가 등장한 빈도 변화',
    x_axis_label = "years",
    y_axis_label = "percentage(%)"
)
colors = itertools.cycle(palette) # 항목마다 다른 색으로 라인이 그려질 수 있게 합니다
for i in range(len(selected_txt_list)):
    fig3.line(txt_perc_total_df.index, txt_perc_total_df[selected_txt_list[i]],legend_label = selected_txt_list[i], line_width = 1, line_color = next(colors))

fig3.height = 400
st.bokeh_chart(fig3, use_container_width=True)


###

plt=reload(plt)

plt.rcParams["font.family"] = 'NanumGothic'

# 제목
st.title("영화 데이터 분석")


# 1번: 관객수
st.subheader("1. 연도별 평균 관객수를 알아보자.")


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



###

def clean_synopsis(syn):
    return str(syn).replace('[', ' ').replace(']', ' ').replace('\'', ' ').replace('\"', ' ').replace('{', '').replace('}', '').strip()

df_syn = pd.read_excel(io='data/total_df2.xlsx', engine = 'openpyxl')

f = open('data/cooccur_idx.json')
data = json.load(f)
f.close()

word_list = [i for i in data]
st.header('키워드로 영화 시놉시스 검색하기')
options = st.multiselect('키워드를 선택해주세요.', word_list)
options_idx = []

if len(options) >= 1:
    options_idx = [j[0] for j in data[options[0]]]
    for i in options:
        next = [j[0] for j in data[i]]
        options_idx = [j for j in next if j in options_idx]
        if len(options_idx) == 0:
            break

if len(options_idx) == 0:
    st.markdown("키워드를 모두 포함하는 영화 시놉시스가 존재하지 않습니다.")
else:
    df_selected = df_syn.iloc[options_idx]
    df_selected = df_selected.drop_duplicates(subset=['title', 'year'])
    df_selected = df_selected.sort_values(by=['audience'], ascending=False)
    df_selected['synopsis_cleaned'] = df_selected.synopsis.apply(clean_synopsis)
    st.markdown(f"키워드를 모두 포함하는 영화 시놉시스가 {len(df_selected)}편 존재합니다.")

    for idx, row in df_selected.iterrows():
        st.subheader(row.title)
        intro = f'{row.audience :,}명이 관람한 {row.year}년의 {(idx+1) % 50}위 영화'
        st.caption(intro)

        bold_synopsis = row.synopsis_cleaned
        for word in options:
            replacement = f'**{word}**'
            bold_synopsis = bold_synopsis.replace(word, replacement)
        bold_synopsis = bold_synopsis.replace('****', '')
        st.write(bold_synopsis)

    # st.dataframe(df_selected[['title', 'year', 'audience', 'synopsis_cleaned']])
