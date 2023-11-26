import streamlit as st
import pandas as pd
import numpy as np
from streamlit import components
import subprocess

# 'bike_map.py'를 실행하여 'bike_map.html' 파일을 생성합니다.
subprocess.call(["python", "bike_map.py"])
# 데이터 로드
# 대여소 수요량 데이터와 거치된 자전거의 수 데이터를 로드해야합니다.
# 이 예제에서는 'demand.csv'와 'bikes.csv'라는 두 개의 CSV 파일을 사용한다고 가정합니다.
# demand_data = pd.read_csv("demand.csv")
bikes_data = pd.read_csv("실시간데이터.csv")

# 데이터 전처리
# 대여소별 수요량과 거치된 자전거의 수를 결합합니다.
# 이 예제에서는 'station' 컬럼이 대여소의 이름을 나타낸다고 가정합니다.
# data = pd.merge(demand_data, bikes_data, on="station")

# 거치된 자전거가 부족한 대여소를 찾습니다.
# 이 예제에서는 수요량이 거치된 자전거의 수보다 많은 대여소를 '부족한 대여소'로 정의한다고 가정합니다.
st.title("광진구 따릉이 대여소별 수요량 예측")
# shortage_stations = data[data["demand"] > data["bikes"]]
shortage_stations = bikes_data[bikes_data["주차된 자전거 수"] < 2]
if shortage_stations.empty:
    st.write("현재 자전거가 부족한 대여소는 없습니다.")
else:
    st.write("다음 대여소에서 자전거가 부족합니다:")
    st.table(shortage_stations[["대여소이름", "주차된 자전거 수"]])  # 대여소 이름과 주차된 자전거 수만 표시

# HTML 파일을 읽습니다.
with open("bike_map.html", "r", encoding="utf-8") as f:
    html_string = f.read()

# HTML 코드를 Streamlit 앱에 삽입합니다.
components.v1.html(html_string, width=800, height=600)
