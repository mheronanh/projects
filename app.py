import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import plotly.graph_objects as go
from supabase import create_client, Client
import json

@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

@st.cache_data(ttl=15)
def run_query():
    return supabase.table("mytable").select("*").order("kebisingan", desc=True).limit(4).execute()

def convert_dict_to_df(data):
    df = pd.DataFrame.from_dict(data)
    return df

st.title("Real-Time / Live Data Science Dashboard")

placeholder = st.empty()
while True:
    supabase = init_connection()
    rows = run_query()
    rows = rows.model_dump_json()
    rows = json.loads(rows)
    if len(rows['data']) == 4:
        with placeholder.container():
            df = convert_dict_to_df(rows['data'])
            st.write(df)
    time.sleep(5)
