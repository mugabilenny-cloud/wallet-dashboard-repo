import streamlit as st
import pandas as pd
from supabase import create_client

supabase = create_client("URL", "KEY")

st.header("Account") # 
st.subheader("Ronald Richards") # 

c1, c2 = st.columns(2)
c1.metric("Wallet Balance", "$12,390.50") # 
c2.metric("Accredited Balance", "6,590.50") # 

st.write("### Activity History") # 
data = supabase.table("shipments").select("*").execute()
df = pd.DataFrame(data.data)
if not df.empty:
    st.table(df[['shipment_no', 'status', 'price_range']])
