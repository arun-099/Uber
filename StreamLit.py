import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
st.markdown("")
# st.sidebar.title("Select Visual Charts")
import requests 
url = "https://github.com/arun-099/Uber/blob/main/Case%20Preso%20-%20Data_Unfiltered.csv"
s = requests.get(url).content

data_original = pd.read_csv(s)
data = data_original.dropna()

st.sidebar.markdown("Select the Charts/Plots accordingly:")
all_columns_names= data.columns.tolist()
  
#st.markdown(type(data.groupby(['Region','Site'])['HC'].sum().to_frame()))

st.title('Uber Dashboad')

df = data.groupby(['Region','Site'])['HC'].sum().to_frame()

chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Bar Chart', 'Line Chart'))
#st.sidebar.checkbox("Show Uber analysis", True, key = 1)
selected_group = st.sidebar.selectbox('Select Type',
                                       options = ['Region', 'Site'])
selected_status = st.sidebar.selectbox('Select Column',
                                       options = ['HC', 'Production Hours', 'Inflow', 'Solves', '# of CSAT Surveys', 'CSAT Score', '# of 1sat surveys', 'Scheduled Hours', 'Non Productive Hours', 'Idle Time'])
fig = go.Figure()

#print(type(data))

if chart_visual == 'Bar Chart':
    if selected_group == 'Region':
        # if selected_status == 'Global':
        #     #data.groupby(['Region','Site'])['HC'].sum().plot.bar()
        #     #st.bar_chart(data.groupby(['Region','Site'])['HC'].sum())
        #     #st.bar_chart(df)
        #     data = data[2:5]
        #     chart_data = pd.DataFrame(
        #     data,
        #     columns=["Region", "Site"])

        #     st.bar_chart(chart_data)

        #     st.markdown(type(chart_data))

        if selected_status == all_columns_names[4]:
            st.bar_chart(data.groupby('Region')[all_columns_names[4]].sum())
        if selected_status == all_columns_names[5]:
            st.bar_chart(data.groupby('Region')[all_columns_names[5]].sum())
        if selected_status == all_columns_names[6]:
            st.bar_chart(data.groupby('Region')[all_columns_names[6]].sum())
        if selected_status == all_columns_names[7]:
            st.bar_chart(data.groupby('Region')[all_columns_names[7]].sum())
        
        if selected_status == all_columns_names[9]:
            st.bar_chart(data.groupby('Region')[all_columns_names[9]].sum())
        if selected_status == all_columns_names[10]:
            st.bar_chart(data.groupby('Region')[all_columns_names[10]].sum())
        if selected_status == all_columns_names[11]:
            st.bar_chart(data.groupby('Region')[all_columns_names[11]].sum())
        
        
        if selected_status == all_columns_names[16]:
            st.bar_chart(data.groupby('Region')[all_columns_names[16]].sum())
        if selected_status == all_columns_names[17]:
            st.bar_chart(data.groupby('Region')[all_columns_names[17]].sum())
        if selected_status == all_columns_names[18]:
            st.bar_chart(data.groupby('Region')[all_columns_names[18]].sum())

    if selected_group == 'Site':
        if selected_status == all_columns_names[4]:
            st.bar_chart(data.groupby('Site')[all_columns_names[4]].sum())
        if selected_status == all_columns_names[5]:
            st.bar_chart(data.groupby('Site')[all_columns_names[5]].sum())
        if selected_status == all_columns_names[6]:
            st.bar_chart(data.groupby('Site')[all_columns_names[6]].sum())
        if selected_status == all_columns_names[7]:
            st.bar_chart(data.groupby('Site')[all_columns_names[7]].sum())

        if selected_status == all_columns_names[9]:
            st.bar_chart(data.groupby('Site')[all_columns_names[9]].sum())
        if selected_status == all_columns_names[10]:
            st.bar_chart(data.groupby('Site')[all_columns_names[10]].sum())
        if selected_status == all_columns_names[11]:
            st.bar_chart(data.groupby('Site')[all_columns_names[11]].sum())
        
        
        if selected_status == all_columns_names[16]:
            st.bar_chart(data.groupby('Site')[all_columns_names[16]].sum())
        if selected_status == all_columns_names[17]:
            st.bar_chart(data.groupby('Site')[all_columns_names[17]].sum())
        if selected_status == all_columns_names[18]:
            st.bar_chart(data.groupby('Site')[all_columns_names[18]].sum())
 

if chart_visual == 'Line Chart':
    if selected_group == 'Region':
        if selected_status == all_columns_names[4]:
            st.line_chart(data.groupby('Region')[all_columns_names[4]].sum())
        if selected_status == all_columns_names[5]:
            st.line_chart(data.groupby('Region')[all_columns_names[5]].sum())
        if selected_status == all_columns_names[6]:
            st.line_chart(data.groupby('Region')[all_columns_names[6]].sum())
        if selected_status == all_columns_names[7]:
            st.line_chart(data.groupby('Region')[all_columns_names[7]].sum())
        
        if selected_status == all_columns_names[9]:
            st.line_chart(data.groupby('Region')[all_columns_names[9]].sum())
        if selected_status == all_columns_names[10]:
            st.line_chart(data.groupby('Region')[all_columns_names[10]].sum())
        if selected_status == all_columns_names[11]:
            st.line_chart(data.groupby('Region')[all_columns_names[11]].sum())
        
        
        if selected_status == all_columns_names[16]:
            st.line_chart(data.groupby('Region')[all_columns_names[16]].sum())
        if selected_status == all_columns_names[17]:
            st.line_chart(data.groupby('Region')[all_columns_names[17]].sum())
        if selected_status == all_columns_names[18]:
            st.line_chart(data.groupby('Region')[all_columns_names[18]].sum())

    if selected_group == 'Site':
        if selected_status == all_columns_names[4]:
            st.line_chart(data.groupby('Site')[all_columns_names[4]].sum())
        if selected_status == all_columns_names[5]:
            st.line_chart(data.groupby('Site')[all_columns_names[5]].sum())
        if selected_status == all_columns_names[6]:
            st.line_chart(data.groupby('Site')[all_columns_names[6]].sum())
        if selected_status == all_columns_names[7]:
            st.line_chart(data.groupby('Site')[all_columns_names[7]].sum())
        
        if selected_status == all_columns_names[9]:
            st.line_chart(data.groupby('Site')[all_columns_names[9]].sum())
        if selected_status == all_columns_names[10]:
            st.line_chart(data.groupby('Site')[all_columns_names[10]].sum())
        if selected_status == all_columns_names[11]:
            st.line_chart(data.groupby('Site')[all_columns_names[11]].sum())
        
        
        if selected_status == all_columns_names[16]:
            st.line_chart(data.groupby('Site')[all_columns_names[16]].sum())
        if selected_status == all_columns_names[17]:
            st.line_chart(data.groupby('Site')[all_columns_names[17]].sum())
        if selected_status == all_columns_names[18]:
            st.line_chart(data.groupby('Site')[all_columns_names[18]].sum())



#st.plotly_chart(fig, use_container_width=True)

# all_columns_names= data.columns.tolist()
# selected_column_names = st.multiselect("select column to plot",all_columns_names)


# with Interactive:
#     fig = go.Figure
#     for name,group in data.groupby(selected_column_names[0]):
#         trace =go.Histogram()
#         trace.name = name 
#         trace.x = group[selected_column_names[1]]
#         fig.add_trace(trace)
#     fig.show()
