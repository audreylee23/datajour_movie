# 기본 import
import streamlit as st
import pandas as pd
from bokeh.plotting import figure

from bokeh.palettes import Dark2_5 as palette
import itertools

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

