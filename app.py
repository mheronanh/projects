import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import plotly.graph_objects as go

data = "data kebisingan(1)-rows.csv"

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(data, delimiter=";")

st.title("Real-Time / Live Data Science Dashboard")

df = get_data()
placeholder = st.empty()
i = 4
while i < 636:
    with placeholder.container():
        st.dataframe(df[i-4:i]) 
        z = df.iloc[(i-4):i, 1:5].values
        st.write(z)
        fig = go.Figure(data=
            go.Contour(
                z = z,
                contours = dict(
                    coloring ='heatmap',
                    showlabels = True,
                    labelfont = dict(
                        size = 10,
                        color = 'white',
                    )
                )
            ))
        for j in range(4):
            for k in range(4):
                fig.add_annotation(x=j, y=k, text=str(z[j,k]), showarrow=False, font_size=16, font_color='black', bgcolor='white', opacity=0.75 )
        fig.update_layout(margin=dict(l=10, r=10, b=10, pad=10), plot_bgcolor='white')
        st.plotly_chart(fig, theme="streamlit")
        i += 4
        time.sleep(1)
print("Done")

