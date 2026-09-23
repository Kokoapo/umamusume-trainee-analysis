import streamlit as st
import pandas as pd
import plotly.express as plx
import kagglehub

path = kagglehub.dataset_download("kokoapo/umamusume-trainees")
df = pd.read_csv(path + "/data.csv")

st.write(df.head())

#############################
#############################
#############################

st.write("# Last Released Trainees")

last_en_trainee = df.loc[df['Release Date (EN)'].idxmax()]
last_jp_trainee = df.loc[df['Release Date (JP)'].idxmax()]

left_column, right_column = st.columns(2)
with left_column:
    st.write("## JP")
    st.write(last_jp_trainee[['Name','Character','Release Date (JP)','Rarity']])

with right_column:
    st.write("## EN")
    st.write(last_en_trainee[['Name','Character','Release Date (EN)','Rarity']])

#############################
#############################
#############################

st.write("# Globally Released Trainees")

count_en_release = df['Release Date (EN)'].count()
count_jp_release = df['Release Date (JP)'].count() - count_en_release
count_no_release = len(df) - count_jp_release - count_en_release

pie_data = {
    'Category': ['EN Release', 'JP Release', 'NO Release'],
    'Values': [count_en_release, count_jp_release, count_no_release]
}
pie_data_df = pd.DataFrame(pie_data)
fig = plx.pie(pie_data_df, 'Category', 'Values')

st.plotly_chart(fig)

#############################
#############################
#############################

st.write("# Release Frequency")

freq_days_jp = pd.to_datetime(df['Release Date (JP)'], format='%Y-%m-%d').sort_values().diff().dt.days.mean()
freq_days_en = pd.to_datetime(df['Release Date (EN)'], format='%Y-%m-%d').sort_values().diff().dt.days.mean()

left_column, right_column = st.columns(2)

with left_column:
    st.write("## JP Server")
    st.write(f"{round(freq_days_jp)} days")

with right_column:
    st.write("## EN Server ")
    st.write(f"{round(freq_days_en)} days")

freq_diff_target = count_jp_release/(1/freq_days_en - 1/freq_days_jp)
st.write(f"I will take approximately {round(freq_diff_target)} days so EN Server reaches JP Server")

#############################
#############################
#############################

st.write("# Rarity Stars Count")

count_rarity = df['Rarity'].value_counts()

fig = plx.bar(count_rarity)
st.plotly_chart(fig)

#############################
#############################
#############################

st.write("# Stats Total %")

count_speed = df['Speed%'].sum()
count_stamina = df['Stamina%'].sum()
count_power = df['Power%'].sum()
count_guts = df['Guts%'].sum()
count_wit = df['Wit%'].sum()

bar_data = {
    'Category': ['Speed', 'Stamina', 'Power', 'Guts', 'Wit'],
    'Value': [count_speed, count_stamina, count_power, count_guts, count_wit]
}
bar_data_df = pd.DataFrame(bar_data)

fig = plx.bar(bar_data_df, x='Category', y='Value')
st.plotly_chart(fig)

#############################
#############################
#############################

st.write("# A Rank Aptitude Distribution")

left_column, middle_column, right_column = st.columns(3)

with left_column:
    count_turf = df['Turf'].value_counts()['A']
    count_dirt = df['Dirt'].value_counts()['A']
    pie_data = {
        'Category': ['Turf', 'Dirt'],
        'Values': [count_turf, count_dirt]
    }
    pie_data_df = pd.DataFrame(pie_data)
    fig = plx.pie(pie_data_df, 'Category', 'Values')
    st.plotly_chart(fig)

with middle_column:
    count_sprint = df['Sprint'].value_counts()['A']
    count_mile = df['Mile'].value_counts()['A']
    count_middle = df['Middle'].value_counts()['A']
    count_long = df['Long'].value_counts()['A']
    pie_data = {
        'Category': ['Sprint', 'Mile', 'Middle', 'Long'],
        'Values': [count_sprint, count_mile, count_middle, count_long]
    }
    pie_data_df = pd.DataFrame(pie_data)
    fig = plx.pie(pie_data_df, 'Category', 'Values')
    st.plotly_chart(fig)

with right_column:
    count_front = df['Front'].value_counts()['A']
    count_pace = df['Pace'].value_counts()['A']
    count_late = df['Late'].value_counts()['A']
    count_end = df['End'].value_counts()['A']
    pie_data = {
        'Category': ['Front', 'Pace', 'Late', 'End'],
        'Values': [count_front, count_pace, count_late, count_end]
    }
    pie_data_df = pd.DataFrame(pie_data)
    fig = plx.pie(pie_data_df, 'Category', 'Values')
    st.plotly_chart(fig)
