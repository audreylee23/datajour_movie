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
st.title("역대 흥행 영화의 트렌드 분석")
st.write("본 데이터 분석은 1980-2022년이라는 43년의 기간 동안의 한국 영화사를 돌아보고, 시대에 따른 변화를 살펴보고자 하는 목적 하에 행해졌다.")
st.write("분석에 사용된 자료는 연도별로 관객수가 50위 이내에 든 흥행 영화들에 대한 데이터로, 영화진흥위원회와 네이버 영화에서 크롤링하였다.")
st.write("우선 한국 영화의 역사를 되짚어볼 수 있는 개괄적인 자료부터 살펴보자.")
st.markdown('***')

# 1번: 관객수
st.header("1. 연도별 평균 관객수의 변화 추이를 살펴보자.")
image1 = Image.open('data/audience_graph1.png')
st.image(image1, caption = '1980-2002년 평균 관객수(서울) 라인그래프')
st.write("우선 서울 관람객 수 데이터만 존재하는 1980-2002년부터 살펴보자. 평균 관객수는 80년대에는 계속해서 비슷한 수준에 머무르다, 90년대가 되면서 점차 가파른 상승세를 타기 시작했다.")

image2 = Image.open('data/audience_graph2.png')
st.image(image2, caption = '2003-2022년 평균 관객수(전국) 라인그래프')
st.write("전국 관람객 수 집계가 시작된 이후에도, 평균 관객수는 꾸준한 상승세에 있었다. 특히 2012년으로 넘어가면서 평균 관객수는 꾸준히 300만 이상을 기록했다.")
st.write("그러나 코로나19가 시작된 2020년에 평균 관객수는 1/4 수준으로 급감했다. 다만 2022년부터 다시 상승할 기미를 보이고 있다.")

# 2번: 연령대
st.markdown('***')
st.header("2. 연도별 연령 등급의 비율 변화 추이를 살펴보자.")
image3 = Image.open('data/agecount_total.png')
st.image(image3, caption = '연도별 연령 등급 비율 파이차트')
st.write("시대가 지남에 따라 '청소년 관람불가' 영화의 비율이 점점 줄어들고 있는 것을 확인할 수 있다. 과거에 비해 영화의 접근성이 중요한 가치로 부상한 것으로 보인다.")

# 3번: 시놉시스 키워드
st.markdown('***')
st.header("3. 워드클라우드로 시놉시스에서 유행한 키워드를 알아보자.")
st.write("영화의 시놉시스에서 '일반명사'를 태깅하여, 어떤 키워드가 유행했는지를 살펴보았다.")

st.write("우선 유행한 시놉시스 키워드를 연도를 기준으로 분류해 보면 다음과 같다.")
image5 = Image.open('data/word_yeartotal.png')
st.image(image5, caption = '연도별 시놉시스 키워드 워드클라우드')
st.write("우선 1980년대의 경우, 상대적으로 과거라 그런지 다른 시대에 비해 아버지, 남편, 아내, 아들 등 전통적 가족을 나타내는 키워드가 많이 등장함을 확인할 수 있다.")
st.write("다음으로 1990년대의 경우, 80년대에 비해 가족을 나타내는 키워드들의 크기가 확연히 줄어들고, 범죄 영화 등의 핵심 키워드인 '사건', '경찰'이 메인 키워드급으로 커진 것이 눈에 띈다.")
st.write("2000년대의 경우, 앞선 워드클라우드에서는 거의 보이지 않았던 '세계'와 '세상'이 점점 커지고 있는 것이 보인다.")
st.write("마지막으로 2010년대의 경우, 앞선 세 워드클라우드에서 모두 큰 비중을 차지했던 '사랑'이라는 키워드의 크기가 급감한 것이 가장 뚜렷한 특징이다. 또 2000년대에 점점 커지고 있던 '세계'와 '세상'이라는 키워드가 메인 키워드급으로 커진 것도 눈에 띈다. 다른 워드클라우드에서는 잘 보이지 않았던 '위기'라는 키워드가 생겨난 것도 확인할 수 있다.")

st.write("유행한 시놉시스 키워드를 영화의 제작 국가를 기준으로 분류해 보면 다음과 같다.")
image4 = Image.open('data/word_krfo.png')
st.image(image4, caption = '국내/국외 시놉시스 키워드 워드클라우드')
st.write("국내 영화에 비해 국외 영화의 시놉시스에서는 전반적으로 '세계'라는 키워드가 많이 등장하는 것으로 보인다. 상대적으로 '스케일이 큰' 영화들이 많이 포진해 있음을 추측해볼 수 있는 대목이다.")
st.write("한편 사람을 표현하는 키워드에 있어서도 차이가 보이는데, 국내 영화는 '남자'와 '여자'가 핵심 키워드인 반면 국외 영화는 '친구'와 '인간'이 핵심 키워드이다.")

#4번
st.markdown('***')
st.header("4. 연도별 시놉시스 키워드의 트렌드를 알아보자.")
st.write('앞서 시대별로 흥행 영화의 시놉시스에 자주 등장하는 단어들을 워드클라우드 형식으로 알아보았다. 실제로 특정 키워드들이 시대에 따라 등장하는 빈도가 변화하였는지를 라인그래프 형식으로 알아보자.')

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
st.write("워드클라우드에서 보였던 여러 키워드들의 증감을 하나씩 살펴보면, 실제로 특정 단어들이 꾸준히 늘어나거나 줄어들고, 또 시대를 막론하고 꾸준히 등장하는 것들을 볼 수 있다.")
st.write("가령 ‘사랑’의 비율이 1980년대 2% 정도에서 시작해 2020년대에는 0.5% 미만으로 떨어지는 모양을 살펴볼 수 있다. 또한 ‘사건’이라는 키워드는 전반적으로 증가 추세를 보이며 ‘아버지’,’결혼’, 등의 키워드는 실제로 전체적으로 줄어드는 추세를 확인할 수 있으며, ‘친구’와 같은 키워드들은 시대를 막론하고 꾸준한 빈도로 등장하고 있다.")
st.write("다중 선택 박스에서 여러 키워드를 선택하면 각각의 라인그래프를 한 번에 비교해볼 수 있다. 가령 사랑, 세계, 세상을 모두 선택하면 사랑은 줄어들고, 세계와 세상은 비슷한 추이로 증가하며 사랑과 세계&세상의 그래프가 2010년을 전후로 교차되는 것을 파악할 수 있다.")


#5번
st.markdown('***')
st.header("5. 연도별 장르의 트렌드를 알아보자.")
st.write("앞서 시대별로 많이 나타나는, 그리고 시대의 흐름에 따라 점점 많이 나타나거나 덜 나타나는 시놉시스 키워드들을 살펴보았다. 어떠한 키워드가 특정 장르를 중심으로 많이 사용될 것임을 짐작해볼 수 있다. 그렇다면 실제로 특정 장르들의 인기가 많아지거나 떨어지는 것 역시 확인할 수 있을까?")
st.write("")
st.write("다음은 시대별로 각 년도 top50 영화들 중 특정 장르들이 차지하는 비율을 계산한 뒤 이를 연도별 추이로 나타낸 라인그래프이다. 가령 다중선택 박스에서 ‘멜로/로맨스’를 선택해보면, 1980년대부터 2022년까지 top 50 영화들 중 ‘멜로/로맨스’ 장르의 영화들의 몇 %를 차지했는 지의 변화를 알 수 있다. 1980년대에 17% 정도에서 시작해 2020년에는 3% 미만으로 떨어진 것을 볼 수 있다. 여러 장르를 선택하면 각 장르마다 별개의 라인그래프들이 중첩되어 그려지기 때문에 증감을 비교해볼 수 있다.")

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

st.write("우선, 시대를 막론하고 ‘드라마’와 ‘액션’ 장르의 top 50 영화에서의 비중이 꾸준히 높다. 반면 ‘코미디’의 경우 2000년대 후반 증가했다가 다시 감소하는, 그다지 일관되지 않는 점유율의 모습을 보인다.")
st.write("‘모험’, ‘판타지’, ‘애니메이션’의 경우 시대에 따라 증가하는 추세를 확인할 수 있고, ‘멜로/로맨스’는 감소하는 것을 확인할 수 있다. ‘범죄’와 같은 경우 특정 시기에 급락했다가 다시 증가하는 모습을 볼 수 있다.")

st.subheader("제작 기술의 발달과 함께 부상한 장르")
st.write("우선, ‘모험’,’판타지’,’애니메이션’ 장르가 시간의 흐름에 따라 증가한 것은, 특수효과나 영화 촬영 기술, 제작 기술의 발달로 인해 해당 장르들의 영화 제작이 용이해지고 전반적인 퀄리티가 상승하였기 때문임을 추측해볼 수 있다. 다양한 소재와 영상미를 담을 수 있게 되며 ‘모험’ , ‘판타지’ 장르에서 관객을 사로잡는 영화들이 제작될 수 있었으며 애니메이션 제작 기술의 발달로 ‘흥행’할만한 퀄리티의 애니메이션 영화들이 제작되었을 것이다.")
st.subheader("멜로/로맨스의 쇠락")
st.write("반면 ‘멜로/로맨스’ 장르의 비율은 눈에 띄게 줄어들었다. 이는 앞서 언급한 기술발전과 함께 증가한 장르의 영화들의 영향으로 상대적인 비율 자체가 줄어든 것뿐만 아니라 해당 장르 자체에 대한 인기가 줄어들었다고도 유추해볼 수 있다.")
st.subheader("특정 장르에 자주 등장하는 키워드들 존재")
st.write("실제로 앞선 시놉시스 키워드 트렌드와 장르 트렌드 분석을 함께 살펴보면, 시대가 지남에 따라 관객들의 ‘취향’이 변화했음을 알려주는 결과들을 살펴볼 수 있었다.")
st.write("‘멜로/로맨스’ 영화들이 감소한 것은 앞서 워드클라우드와 라인그래프에서 ‘사랑’이라는 키워드가 줄어든 것(사라진 것)과 연관이 있으며 ‘모험’, ‘판타지’ 영화들이 증가한 것은 ‘세계’, ‘세상’, ‘위기’라는 키워드가 점점 커지는 것과 연관이 있을 것이다.")
st.write("또 이와 별개로 ‘스릴러’영화의 최전성기였던 1990년대의 워드클라우드에서 ‘사건’, ‘경찰’ 키워드가 급부상한 것 역시 확인할 수 있다. 즉, 특정 장르에 자주 등장하는 몇 개의 키워드들이 존재한다.")
st.write("그렇다면, 특정 장르 내에서 시놉시스 키워드의 변화는 어떠할까? 1990년대에 인기있던 ‘범죄’영화와 2010년대에 인기있는 ‘범죄’영화는 어떻게 다를까?")

#6번
st.markdown('***')
st.header("6. 주요 장르별 시놉시스 키워드의 특이한 변화 추이를 알아보자.")
st.write('앞에서는 모든 장르를 아우르는 범위에서 키워드들의 변화를 살펴보았다. 그렇다면, 특정 장르 안에서는 어떤 변화가 나타났을지 살펴보자.')

option = st.selectbox('장르를 선택해주세요.',
                     ('드라마', '액션', '범죄', '판타지', '코미디', '모험', '스릴러'))	

if option == '드라마':
    st.image('data/drama_keyword_love.jpeg')
    st.subheader('사랑')
    st.write('전체적인 로맨스 영화 비중이 작아짐에 ‘사랑’이라는 키워드 비중도 줄어들었다.')
    st.write('')

    st.image('data/drama_keyword_marriage.jpeg')
    st.subheader('결혼')
    st.write('결혼에 대해 회의적이거나 부정적인 사람들이 늘어나고, 결혼이 필수가 아니라는 관념이 사회적으로 퍼지게 되면서, 그 영향으로 ‘결혼’ 키워드 비중 또한 작아지게 되었다.')
    st.write('')

elif option == '액션':
    st.image('data/action_keyword_world_globe_agent_police.jpeg')
    st.subheader('세계, 세상, 요원, 경찰')
    st.write('영화의 스케일이 커지면서, 영화의 배경이나 주인공의 활동이 영향을 미치는 범위도 넓어졌다. 그 결과, ‘세계’, ‘세상’가 많이 등장하게 되었다. 영화 스케일의 거대화는 ‘요원’의 상승과 ‘경찰’의 하락에서도 반영되었다. 국지적 사건을 다루는 ‘경찰’은 하락하고, 국제적이고 비밀스러운 사건을 다루는 ‘요원’은 상승하게 되었다. ')
    st.write('')
    
elif option == '범죄':
    st.image('data/crime_keyword_murder_fraud.jpeg')
    st.subheader('살인 vs 사기')
    st.write('시간이 흐를수록 살인은 줄어들고, 사기의 비중이 커지는 것을 확인할 수 있다. 이 점에서, 범죄 영화에 나타나는 범죄 유형이 달라졌음을 알 수 있다. 시간이 흐르고 사회가 복잡해짐에 따라 강력범죄뿐만 아니라 화이트칼라 범죄도 영화에서 나타나고 있다.')
    st.write('')


elif option == '판타지':
    st.image('data/fantasy_keyword_world_globe.jpeg')
    st.subheader('세계, 세상')
    st.write('영화의 스케일이 점차 거대해지면서, ‘세계’, ‘세상’이 차지하는 비중이 커졌다.')
    st.write('')


elif option == '코미디':
    st.image('data/comedy_keyword_globe_world.jpeg')
    st.subheader('세계, 세상')
    st.write('영화 산업의 자본뿐만 아니라 영화 스토리 배경의 설정도 장대해지면서 ‘세계’, ‘세상’이라는 단어가 등장하는 정도가 증가하였다. 코미디 장르에서도 이와 같은 움직임을 확인할 수 있다는 점에서 영화의 ‘스케일’이 커졌음을 확인할 수 있다. ')
    st.write('')


elif option == '모험':
    st.image('data/adventure_keyword_world_globe_threat_war.jpeg')
    st.subheader('세계, 세상, 위협, 전쟁')
    st.write('영화 스토리의 스케일이 전반적으로 커지면서 거대한 세계관을 나타내는 키워드 ‘세계’, ‘세상’, ‘위협’, ’전쟁’의 비중이 늘어났다. ')
    st.write('')


elif option == '스릴러':
    st.image('data/thriller_keyword_globe_world.jpeg')
    st.subheader('세계, 세상')
    st.write('전반적인 영화업계의 스케일 성장 흐름에 따라 스릴러에서도 넓은 스케일을 보여주는 ‘세계, 세상’의 비중이 증가하였다. ')
    st.write('')

    st.image('data/thriller_keyword_question.jpeg')
    st.subheader('의문')
    st.write('‘의문’이란 키워드의 비중 증가를 통해 스릴러 영화 특징의 변화를 유추해볼 수 있다. 옛날에는 귀신, 강시 등 확실하게 정체를 아는 존재를 통해 공포심을 유발했다면, 현대로 올수록 그 존재에 대해 아무것도 알지 못 하고 확신하지 못 한다는 점을 이용해 두려움을 일깨우고 있다는 점을 유추할 수 있다.')
    st.write('')

#7번
st.markdown('***')
st.header('7. 결론')

st.write("지금까지 우리는 1980년부터 2022년까지의 영화 흐름을 살펴보면서 어떤 변화가 발생했는지 살펴보았다.")
st.write("우선 영화 시놉시스에서 유행한 키워드를 10년 단위로 나누어 살펴본 결과, 우리는 두 가지를 유추해낼 수 있었다. 첫째, 1980년대, 1990년대, 2000년대에서 모두 큰 비중을 차지했던 ‘사랑’이 2010년대에 급감한 점을 통해 로맨스의 인기가 떨어졌다는 점을 알 수 있었다. 둘째, 1980년대와 1990년대에서는 잘 보이지 않았던 ‘세상’과 ‘세계’가 2000년대를 거쳐 2020년대에 비중이 매우 커진 점을 통해 전반적인 영화의 ‘스케일’이 커졌음을 추측할 수 있다. ")
st.write("이후 우리는 연도별 시놉시스 키워드 변화를 통해 앞서 살펴보았던 ‘사랑’, ‘세상’, ‘세계’의 비중 변화를 명확하게 확인하였다. 시간이 흐를수록 ‘사랑’은 감소하였고, ‘세계’와 ‘세상’은 증가하였다. 이러한 변화는 장르의 인기 변화와도 연관이 있었다. 매해 top50영화 중 특정 장르들이 차지한 비중의 변화를 라인그래프로 살펴본 결과, 로맨스는 비중이 감소하였고, 기본적으로 ‘스케일이 큰’ 모험, 판타지 등의 비중이 증가하였다. 이는 영화 제작 기술의 발달과도 연관지어 생각해볼 수 있는 지점이다. ")
st.write("그 다음으로 우리는 주요 장르별 시놉시스 키워드의 특이한 변화 추이를 살펴보았다. 이 부분에서도 우리는 ‘세상’과 ‘세계’의 비중 증가를 통해서 영화들의 ‘스케일 거대화’를 확인할 수 있었다. 이외에도 사회 분위기나 영화 특징의 변화를 키워드 변화를 통해서 유추해낼 수 있었다. ")
st.write("이처럼 우리는 사회의 변화, 영화 산업계의 변화는 영화 장르 인기와 시놉시스 키워드의 변화를 통해 알아보았다. 지금까지 분석한 내용을 한 마디로 정리하자면 다음과 같다.")

st.subheader("너와 나만의 이야기에서 우리 모두의 이야기로!")


st.write('앞서 도출한 결론을 뒷받침하는 예시로 아래에서 키워드를 검색하여 시놉시스를 확인할 수 있다.')
st.markdown('***')

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
    st.write("키워드를 모두 포함하는 영화 시놉시스가 존재하지 않습니다.")
else:
    df_selected = df_syn.iloc[options_idx]
    df_selected = df_selected.drop_duplicates(subset=['title', 'year'])
    df_selected = df_selected.sort_values(by=['audience'], ascending=False)
    df_selected['synopsis_cleaned'] = df_selected.synopsis.apply(clean_synopsis)
    st.write(f"키워드를 모두 포함하는 영화 시놉시스가 {len(df_selected)}편 존재합니다.")

    for idx, row in df_selected.iterrows():
        st.header(row.title)
        intro = f'{row.audience :,}명이 관람한 {row.year}년의 {(idx+1) % 50}위 영화. 장르: {row.genre}'
        st.caption(intro)

        bold_synopsis = row.synopsis_cleaned
        for word in options:
            replacement = f'**{word}**'
            bold_synopsis = bold_synopsis.replace(word, replacement)
        bold_synopsis = bold_synopsis.replace('****', '')
        st.write(bold_synopsis)

    # st.dataframe(df_selected[['title', 'year', 'audience', 'synopsis_cleaned']])
