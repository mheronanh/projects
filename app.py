import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import plotly.graph_objects as go
from supabase import create_client, Client

@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

@st.cache_data(ttl=15)
def run_query():
    return supabase.table("mytable").select("*").order("kebisingan",desc=True)

st.title("Real-Time / Live Data Science Dashboard")

while True:
    supabase = init_connection()
    rows = run_query()
    st.write(rows)
    time.sleep(5)
