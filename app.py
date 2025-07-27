
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px

st.set_page_config(page_title="Centinal FLM Dashboard", layout="wide")

st.title("📊 Centinal FLM Investigation Dashboard")

# Simulate summary metrics
open_cases = 37
avg_loss = 18200
confirmed_loss = 674000
recovery_rate = 0.42

# Top metric columns
col1, col2, col3, col4 = st.columns(4)
col1.metric("Open Investigations", f"{open_cases}")
col2.metric("Avg. Loss per Case", f"£{avg_loss:,.0f}")
col3.metric("Confirmed Fraud Loss", f"£{confirmed_loss:,.0f}")
col4.metric("Recovery Rate", f"{recovery_rate*100:.0f}%")

st.markdown("---")

# Simulated Losses by Department
departments = ['Finance', 'Procurement', 'HR', 'Operations']
loss_values = [180000, 290000, 95000, 109000]
dept_df = pd.DataFrame({'Department': departments, 'Loss (£)': loss_values})

bar_fig = px.bar(dept_df, x='Department', y='Loss (£)', title="Fraud Losses by Department (£)", color='Department',
                 text='Loss (£)', color_discrete_sequence=px.colors.qualitative.Pastel)
bar_fig.update_layout(showlegend=False)
st.plotly_chart(bar_fig, use_container_width=True)

# Simulated Cumulative Fraud Loss over Time
dates = [datetime.now() - timedelta(days=i*30) for i in range(5)][::-1]
losses = np.cumsum(np.random.randint(50000, 100000, size=5))
time_df = pd.DataFrame({'Month': [d.strftime("%b %Y") for d in dates], 'Cumulative Loss (£)': losses})

line_fig = px.line(time_df, x='Month', y='Cumulative Loss (£)', title="Cumulative Fraud Loss Over Time",
                   markers=True)
st.plotly_chart(line_fig, use_container_width=True)

# Simulated Case Status
case_status = ['Open', 'Closed', 'Under Review', 'Referred']
status_counts = [37, 22, 8, 5]
status_df = pd.DataFrame({'Status': case_status, 'Count': status_counts})

pie_fig = px.pie(status_df, names='Status', values='Count', title="Case Status Distribution",
                 color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(pie_fig, use_container_width=True)

st.markdown("---")
st.caption("Demo data only – Centinal FLM module prototype.")
