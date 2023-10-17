import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# 데이터 로드 (새로운 데이터 파일)
file_path = '/Users/prost/Downloads/231017_test.csv'
df = pd.read_csv(file_path, parse_dates=['createdAt'])

# NaN 값을 제거
df.dropna(subset=['number'], inplace=True)

# number 열을 int 타입으로 변환
df['number'] = df['number'].astype(int)

st.header('DoBrain2 Dashboard')
st.write('Hello, *Prost!* :sunglasses:')

# ProfileId 선택
selected_profile = st.selectbox('Select ProfileId', df['ProfileId'].unique())
profile_filtered_df = df[df['ProfileId'] == selected_profile]

# alSessionType 선택
selected_types = st.multiselect('Select alSessionType', profile_filtered_df['alSessionType'].unique())

if len(selected_types) > 0:
    for selected_type in selected_types:
        type_data = profile_filtered_df[profile_filtered_df['alSessionType'] == selected_type]
        st.write(f'alSessionType: {selected_type}')
        
        # Altair 라이브러리를 사용하여 상호 작용이 가능한 그래프 생성
        chart = alt.Chart(type_data).mark_line().encode(
            x=alt.X('serial', scale=alt.Scale(domain=(type_data['serial'].min(), type_data['serial'].max()))),  # x축을 serial로 설정
            y='number',  # y축을 number로 설정
            tooltip=['serial', 'number', 'alSessionTypeLv', 'createdAt']  # 커서를 올렸을 때 나타나는 정보 설정
        ).interactive()  # 그래프를 상호 작용이 가능하게 설정
        
        st.altair_chart(chart, use_container_width=True)  # 그래프를 Streamlit 앱에 표시
