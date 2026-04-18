import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Poll Results Visualizer",
    layout="wide"
)

st.title("📊 Poll Results Visualizer Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/poll_data.csv")

df = load_data()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filter Data")

age_filter = st.sidebar.multiselect(
    "Select Age Group",
    df["Age"].unique(),
    default=df["Age"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Age"].isin(age_filter)) &
    (df["Gender"].isin(gender_filter))
]

# -----------------------------
# KPI METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Responses", len(filtered_df))
col2.metric("Average Satisfaction", round(filtered_df["Satisfaction"].mean(), 2))
col3.metric("Most Preferred Tool", filtered_df["Tool"].mode()[0])

# -----------------------------
# DATA PREVIEW
# -----------------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)

# -----------------------------
# BAR CHART
# -----------------------------
st.subheader("📊 Tool Preference")

fig1, ax1 = plt.subplots()
sns.countplot(x="Tool", data=filtered_df, ax=ax1)
st.pyplot(fig1)

# -----------------------------
# PIE CHART
# -----------------------------
st.subheader("🥧 Tool Share")

tool_counts = filtered_df["Tool"].value_counts()

fig2, ax2 = plt.subplots()
tool_counts.plot.pie(autopct='%1.1f%%', ax=ax2)
ax2.set_ylabel("")
st.pyplot(fig2)

# -----------------------------
# DEMOGRAPHIC ANALYSIS
# -----------------------------
st.subheader("👥 Tool Preference by Gender")

pivot = pd.crosstab(filtered_df["Tool"], filtered_df["Gender"])

st.bar_chart(pivot)

# -----------------------------
# SATISFACTION DISTRIBUTION
# -----------------------------
st.subheader("⭐ Satisfaction Distribution")

fig3, ax3 = plt.subplots()
sns.histplot(filtered_df["Satisfaction"], bins=5, kde=True, ax=ax3)
st.pyplot(fig3)

# -----------------------------
# WORD CLOUD (Optional)
# -----------------------------
if "Feedback" in filtered_df.columns:
    st.subheader("📝 Feedback Word Cloud")

    text = " ".join(filtered_df["Feedback"].dropna().astype(str))

    if text:
        wordcloud = WordCloud(width=800, height=400).generate(text)
        fig4, ax4 = plt.subplots()
        ax4.imshow(wordcloud)
        ax4.axis("off")
        st.pyplot(fig4)
    else:
        st.write("No feedback available.")

# -----------------------------
# INSIGHTS SECTION
# -----------------------------
st.subheader("📌 Key Insights")

top_tool = filtered_df["Tool"].value_counts().idxmax()

st.success(f"🏆 Most Preferred Tool: {top_tool}")

st.info("📈 Use filters to explore different demographics.")







