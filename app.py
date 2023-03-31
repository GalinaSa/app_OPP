import streamlit as st
import requests
from PIL import Image
import numpy as np
import pandas as pd
import time
import altair as alt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#st.set_page_config(layout="wide")

df = pd.read_csv("prediction_forecast.csv")
fig, ax = plt.subplots(figsize=(30,18))
ax.plot(df['Date'], df['Real Oil rate'], **{'color': 'limegreen', 'linestyle': '','marker': 'o', 'markersize': 8, 'label':'Real oil production'})
ax.plot(df['Date'], df['Predicted Oil rate'], **{'color': 'black', 'linewidth': 3, 'label':'Predicted oil production'})
ax.xaxis.set_visible(False)
ax.set_ylabel('Oil production [barrels]', fontsize=30)
ax.legend(fontsize="30")
plt.ylim(bottom=300)

fig2, ax = plt.subplots(figsize=(30,18))
ax.plot(df['Date'], df['Real Oil rate'], **{'color': 'limegreen', 'linestyle': '','marker': 'o', 'markersize': 8, 'label':'Real oil production'})
ax.plot(df['Date'], df['Forecasted Oil'], **{'color': 'red', 'linestyle': '','marker': 'o', 'markersize': 4, 'label':'Forecasted Oil'})
ax.plot(df['Date'], df['Predicted Oil rate'], **{'color': 'black', 'linewidth': 3, 'label':'Predicted oil production'})
ax.xaxis.set_visible(False)
ax.set_ylabel('Oil production [barrels]', fontsize=30)
ax.legend(fontsize="30")
plt.ylim(bottom=300)

st.markdown("<h2 style='text-align: center; color: black;'>PREDICT OIL</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey;'>We can predict the historical Oil Rates and also Forecast the future production! </h4>", unsafe_allow_html=True)


image = Image.open('Image_hist4.jpg')
st.image(image, use_column_width=True)

st.markdown("""
#### Please load your data:
""")
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write("filename:", uploaded_file.name)
    st.write(dataframe)
if st.button('Make Prediction'):
    time.sleep(10)

    #def get_line_chart_data():

        #df = pd.read_csv("prediction_forecast.csv")
        #return df

    #df = get_line_chart_data()
    #st.line_chart(df[['Real Oil rate', 'Predicted Oil rate']])

    tab1, tab2, tab3 = st.tabs(["🗃 Impactful features","📈 Prediction Chart", "🗃 📈 Forecast Chart"])
    tab1.subheader("List of the most impactful features")
    tab1.markdown("""
        - Pressure at the Well Head
        - Amount of gas in produced oil
        - Size of the choke
        - Temperature
    """)

    tab2.subheader("Real vs. Predicted oil")
    tab2.pyplot(fig)

    tab3.subheader("Real vs. Forecast oil")
    tab3.pyplot(fig2)


    #time.sleep(10)
    #with st.button('Done!'):
            #st.balloons()


#url = 'http://localhost:8080/predict'
url = 'https://container-opp-6kchhmx67a-ew.a.run.app/predict'


#My attemps with Altair Chart:
#df['Date'] = df.index.values
#line_chart1 = alt.Chart(df).mark_point(size=4, color='limegreen').encode(
    #alt.X("Date", title="Date", axis=alt.Axis(labels=False)),
    #alt.Y("Real Oil rate", title="Oil Production", scale=alt.Scale(domain=[1000,35000]),axis=alt.Axis(labels=False)),
    #).properties(width=800, height=400)

#line_chart2 = alt.Chart(df).mark_line(size=1, color='black').encode(
    #alt.X("Date"),
    #alt.Y("Predicted Oil rate"),
    #)
#st.altair_chart(line_chart1 + line_chart2, use_container_width=True)
