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
from bokeh.core.validation import silence
from bokeh.core.validation.warnings import MISSING_RENDERERS
silence(MISSING_RENDERERS, True)

plt=reload(plt)
plt.rcParams["font.family"] = 'NanumGothic'

# 제목
st.title("역대 흥행 영화의 트렌드 분석: 시놉시스 키워드를 중심으로")
st.write("본 데이터 분석은 1980-2022년이라는 43년의 기간 동안의 한국 영화사를 돌아보고, 시대에 따른 변화를 살펴보고자 하는 목적 하에 행해졌다.")
st.write("분석에 사용된 자료는 연도별로 관객수가 50위 이내에 든 흥행 영화들에 대한 데이터로, 영화진흥위원회와 네이버 영화에서 크롤링하였다.")
st.write("우선 한국 영화의 역사를 되짚어볼 수 있는 개괄적인 자료부터 살펴보자.")

# 1번: 관객수
st.subheader("1. 연도별 평균 관객수의 변화 추이를 살펴보자.")
image1 = Image.open('data/audience_graph1.png')
st.image(image1, caption = '1980-2002년 평균 관객수(서울) 라인그래프')
st.write("우선 서울 관람객 수 데이터만 존재하는 1980-2002년부터 살펴보자. 평균 관객수는 80년대에는 계속해서 비슷한 수준에 머무르다, 90년대가 되면서 점차 가파른 상승세를 타기 시작했다.")

image2 = Image.open('data/audience_graph2.png')
st.image(image2, caption = '2003-2022년 평균 관객수(전국) 라인그래프')
st.write("전국 관람객 수 집계가 시작된 이후에도, 평균 관객수는 꾸준한 상승세에 있었다. 특히 2012년으로 넘어가면서 평균 관객수는 꾸준히 300만 이상을 기록했다.")
st.write("그러나 코로나19가 시작된 2020년에 평균 관객수는 1/4 수준으로 급감했다. 다만 2022년부터 다시 상승할 기미를 보이고 있다.")

# 2번: 연령대
st.subheader("2. 연도별 연령 등급의 비율 변화 추이를 살펴보자.")
image3 = Image.open('data/agecount_total.png')
st.image(image3, caption = '연도별 연령 등급 비율 파이차트')
st.write("시대가 지남에 따라 '청소년 관람불가' 영화의 비율이 점점 줄어들고 있는 것을 확인할 수 있다. 과거에 비해 영화의 접근성이 중요한 가치로 부상한 것으로 보인다.")

# 3번: 시놉시스 키워드
st.subheader("3. 연도별로 어떤 시놉시스 키워드가 유행했는지 알아보자.")
st.write("영화의 시놉시스에서 '일반명사'를 태깅하여, 어떤 키워드가 유행했는지를 살펴보았다.")
st.write("우선 유행한 시놉시스 키워드를 영화의 제작 국가를 기준으로 분류해 보면 다음과 같다.")
image4 = Image.open('data/word_krfo.png')
st.image(image4, caption = '국내/국외 시놉시스 키워드 워드클라우드')
st.write("국내 영화에 비해 국외 영화의 시놉시스에서는 전반적으로 '세계'라는 키워드가 많이 등장하는 것으로 보인다. 상대적으로 '스케일이 큰' 영화들이 많이 포진해 있음을 추측해볼 수 있는 대목이다.")
st.write("한편 사람을 표현하는 키워드에 있어서도 차이가 보이는데, 국내 영화는 '남자'와 '여자'가 핵심 키워드인 반면 국외 영화는 '친구'와 '인간'이 핵심 키워드이다.")
st.write("유행한 시놉시스 키워드를 연도를 기준으로 분류해 보면 다음과 같다.")
image5 = Image.open('data/word_yeartotal.png')
st.image(image5, caption = '연도별 시놉시스 키워드 워드클라우드')
st.write("우선 1980년대의 경우, 상대적으로 과거라 그런지 다른 시대에 비해 아버지, 남편, 아내, 아들 등 전통적 가족을 나타내는 키워드가 많이 등장함을 확인할 수 있다.")
st.write("다음으로 1990년대의 경우, 80년대에 비해 가족을 나타내는 키워드들의 크기가 확연히 줄어들고, 범죄 영화 등의 핵심 키워드인 '사건', '경찰'이 메인 키워드급으로 커진 것이 눈에 띈다.")
st.write("2000년대의 경우, 앞선 워드클라우드에서는 거의 보이지 않았던 '세계'와 '세상'이 점점 커지고 있는 것이 보인다.")
st.write("마지막으로 2010년대의 경우, 앞선 세 워드클라우드에서 모두 큰 비중을 차지했던 '사랑'이라는 키워드의 크기가 급감한 것이 가장 뚜렷한 특징이다. 또 2000년대에 점점 커지고 있던 '세계'와 '세상'이라는 키워드가 메인 키워드급으로 커진 것도 눈에 띈다.")

###
st.markdown("# 시대별 top50 영화의 장르 및 시놉시스 키워드 트렌드를 알아보자")

st.markdown("## 시대별 top50 영화의 장르를 알아보자")

# 저장된 csv 파일 읽어서 dataframe 만들기
genre_perc_total = pd.read_csv("data/total_genre_percentage2.csv",sep="\t", index_col=0)
genre_perc_total_df = pd.DataFrame(genre_perc_total)

with st.expander("사용된 데이터 보기(단위 : %)"):
    # st.write(genre_perc_total_df) #사용된 데이터프레임
    for_print1 = genre_perc_total_df.astype(str)
    st.write(for_print1)

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
    # st.write(txt_perc_total_df) #사용된 데이터프레임
    for_print2 = txt_perc_total_df.astype(str)
    st.write(for_print2)

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
def clean_synopsis(syn):
    return str(syn).replace('[', ' ').replace(']', ' ').replace('\'', ' ').replace('\"', ' ').replace('{', '').replace('}', '').strip()

df_syn = pd.read_excel(io='data/total_df2.xlsx', engine = 'openpyxl')

f = open('data/cooccur_idx.json')
data = json.load(f)
f.close()

word_list = [i for i in data]
st.header('키워드로 영화 시놉시스 검색하기')
st.write('키워드 중 단순 빈도와 공출현 빈도가 모두 높은 키워드 상위 30개를 바탕으로 시놉시스를 검색할 수 있다. 목록의 키워드는 단순 빈도 150 이상, 공출현 빈도 50 이상의 키워드다.')
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
