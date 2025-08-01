import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide', page_title='Startup Funding Dashboard')

# Load and preprocess data
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Utility function to set custom styles
st.markdown("""
    <style>
        .main {background-color: #0e1117;}
        h1, h2, h3, .stMarkdown h5 {color: #cccccc;}
    </style>
""", unsafe_allow_html=True)

# Custom metric card styling
def styled_metric(title, value, icon=""):
    st.markdown(f"""
        <div style="background-color:#1f1f1f;padding:20px;border-radius:12px;text-align:center;box-shadow:0 0 10px #000;">
            <h5 style="color:#cccccc;margin-bottom:10px;">{icon} {title}</h5>
            <h2 style="color:#ffffff;margin:0;">{value}</h2>
        </div>
    """, unsafe_allow_html=True)

def load_overall_analysis():
    st.title('📈 Overall Startup Funding Analysis')
    col1, col2, col3, col4 = st.columns(4)

    total = round(df['amount'].sum())
    max_funding = round(df.groupby('startup')['amount'].max().sort_values(ascending=False).iloc[0])
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    total_startup = df['startup'].nunique()

    with col1:
        styled_metric('Total Funding', f'{total} Cr', '💰')
    with col2:
        styled_metric('Max Single Investment', f'{max_funding} Cr', '🚀')
    with col3:
        styled_metric('Avg Investment per Startup', f'{avg_funding} Cr', '📊')
    with col4:
        styled_metric('Total Funded Startups', f'{total_startup}', '🏢')

    st.markdown("---")
    st.subheader('🗓️ Month-on-Month Funding Trend')
    selected_option = st.radio('Choose Metric', ['Total Amount', 'Investment Count'], horizontal=True)

    if selected_option == 'Total Amount':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(data=temp_df, x='x_axis', y='amount', marker='o', ax=ax)
    ax.set_xlabel('Month-Year')
    ax.set_ylabel('Amount')
    plt.xticks(rotation=45)
    st.pyplot(fig)

def load_investor_details(investor):
    st.title(f'📌 Investor Analysis: {investor}')
    investor_df = df[df['investors'].str.contains(investor, na=False)]

    if investor_df.empty:
        st.warning("No data found for the selected investor.")
        return

    st.subheader('🕔 Most Recent Investments')
    st.dataframe(investor_df[['date', 'startup', 'vertical', 'city', 'round', 'amount']].head())

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('💸 Top 5 Investments')
        big_series = investor_df.groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        if not big_series.empty:
            fig, ax = plt.subplots()
            sns.barplot(x=big_series.values, y=big_series.index, ax=ax)
            st.pyplot(fig)
        else:
            st.info("No big investments to show.")

    with col2:
        st.subheader('📍 Sector-Wise Distribution')
        vertical_series = investor_df.groupby('vertical')['amount'].sum()
        if not vertical_series.empty:
            fig1, ax1 = plt.subplots()
            ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
            st.pyplot(fig1)
        else:
            st.info("No sector data available.")

    col3, col4 = st.columns(2)
    with col3:
        st.subheader('🏷️ Investment Rounds')
        round_series = investor_df.groupby('round')['amount'].sum()
        if not round_series.empty:
            fig2, ax2 = plt.subplots()
            ax2.pie(round_series, labels=round_series.index, autopct="%0.01f%%")
            st.pyplot(fig2)
        else:
            st.info("No round data available.")

    with col4:
        st.subheader('🌆 Investment by City')
        city_series = investor_df.groupby('city')['amount'].sum()
        if not city_series.empty:
            fig3, ax3 = plt.subplots()
            ax3.pie(city_series, labels=city_series.index, autopct="%0.01f%%")
            st.pyplot(fig3)
        else:
            st.info("No city data available.")

    st.subheader('📅 Year-on-Year Investment Trend')
    year_series = investor_df.groupby('year')['amount'].sum()
    if not year_series.empty:
        fig4, ax4 = plt.subplots()
        sns.lineplot(x=year_series.index, y=year_series.values, marker='o', ax=ax4)
        st.pyplot(fig4)
    else:
        st.info("No yearly investment data available.")

# Sidebar UI
st.sidebar.title('🧭 Navigation')
option = st.sidebar.radio('Choose Analysis Mode', ['Overall Analysis', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'Investor':
    all_investors = sorted(set(sum(df['investors'].dropna().str.split(','), [])))
    selected_investor = st.sidebar.selectbox('Select Investor', all_investors)
    if st.sidebar.button('Analyze Investor'):
        load_investor_details(selected_investor)

# Note: StartUp analysis section can be added later
