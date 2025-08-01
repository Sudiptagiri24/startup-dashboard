import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='StartUp Analysis')

# Load and preprocess data
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year


def load_overall_analysis():
    st.title('Overall Analysis')
    col1, col2, col3, col4 = st.columns(4)

    total = round(df['amount'].sum())
    max_funding = round(df.groupby('startup')['amount'].max().sort_values(ascending=False).iloc[0])
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    total_startup = df['startup'].nunique()

    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')
    with col3:
        st.metric('Avg', str(avg_funding) + ' Cr')
    with col4:
        st.metric('Funded Startups', str(total_startup))

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])

    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)

    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'], temp_df['amount'])
    plt.xticks(rotation='vertical')
    st.pyplot(fig5)


def load_investor_details(investor):
    st.title(investor)
    investor_df = df[df['investors'].str.contains(investor, na=False)]

    st.subheader('Most Recent Investments')
    st.dataframe(investor_df[['date', 'startup', 'vertical', 'city', 'round', 'amount']].sort_values(by='date',
                                                                                                     ascending=False).head())

    col1, col2 = st.columns(2)

    with col1:
        big_series = investor_df.groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col2:
        vertical_series = investor_df.groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        round_series = investor_df.groupby('round')['amount'].sum()
        st.subheader('Rounds')
        fig2, ax2 = plt.subplots()
        ax2.pie(round_series, labels=round_series.index, autopct="%0.01f%%")
        st.pyplot(fig2)

    with col4:
        city_series = investor_df.groupby('city')['amount'].sum()
        st.subheader('Cities')
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series, labels=city_series.index, autopct="%0.01f%%")
        st.pyplot(fig3)

    st.subheader('YoY Investment')
    year_series = investor_df.groupby('year')['amount'].sum()
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.pyplot(fig4)


# Sidebar UI
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select StartUp', sorted(df['startup'].dropna().unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis (Coming Soon)')

elif option == 'Investor':
    all_investors = sorted(set(sum(df['investors'].dropna().str.split(','), [])))
    selected_investor = st.sidebar.selectbox('Select Investor', all_investors)
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
