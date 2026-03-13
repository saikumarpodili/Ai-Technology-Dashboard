
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Technology Dashboard", layout="wide")

st.markdown("<h1 style='text-align:center;'>🚀 AI Technology Intelligence Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Interactive dashboard to analyze AI trends, salaries, investments and adoption.</p>", unsafe_allow_html=True)

trend_df = pd.read_csv("tech_trends_large.csv")
salary_df = pd.read_csv("ai_salary_dataset.csv")
investment_df = pd.read_csv("ai_investment_dataset.csv")
forecast_df = pd.read_csv("ai_adoption_forecast.csv")
rec_df = pd.read_csv("tech_recommendations_large.csv")

st.subheader("📈 AI Technology Trends")
fig1 = px.line(trend_df, x="date", y="popularity_score", color="technology", title="Technology Trend Over Time")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("💰 AI Salary Analysis")
fig2 = px.bar(salary_df, x="country", y="average_salary_usd", color="country", title="AI Salary by Country")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📊 AI Investment")
fig3 = px.bar(investment_df, x="country", y="investment_billion_usd", color="country", title="AI Investment by Country")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("📉 AI Adoption Forecast")
fig4 = px.line(forecast_df, x="Year", y="Adoption_Score", color="Technology", title="AI Adoption Forecast")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("🧠 AI Skill Recommendation")
tech_skill = st.selectbox("Select Technology for Skills", rec_df["technology"].unique())
skills = rec_df[rec_df["technology"] == tech_skill]["recommended_skill"]
st.write("Recommended Skills:")
for s in skills:
    st.write("-", s)

st.subheader("🤖 AI Dashboard Chatbot")
user_input = st.text_input("Ask about AI salaries, investment, trends or skills")

if user_input:
    query = user_input.lower()
    if "salary" in query:
        st.success("AI salaries are highest in the United States and Europe.")
    elif "investment" in query:
        st.success("The United States and China lead global AI investment.")
    elif "trend" in query:
        st.success("Machine Learning and Generative AI are rapidly growing technologies.")
    elif "skill" in query:
        st.success("Top AI skills include Python, Machine Learning, Deep Learning and NLP.")
    else:
        st.info("Try asking about AI salary, investment, trends or skills.")
