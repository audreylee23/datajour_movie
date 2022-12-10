# 기본 import
import streamlit as st
import pandas as pd
import json

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
