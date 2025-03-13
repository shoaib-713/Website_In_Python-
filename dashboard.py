import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page title and layout
st.set_page_config(page_title="Simple Data Dashboard", layout="wide")

# Title of the dashboard
st.title("📊 Simple Data Dashboard")

# Upload CSV file
st.sidebar.header("Upload Your CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Show basic statistics
    st.write("### Data Summary")
    st.write(df.describe())

    # Select column for visualization
    st.sidebar.header("Visualization Options")
    selected_column = st.sidebar.selectbox("Choose a column to visualize", df.select_dtypes(include=['number']).columns)

    if selected_column:
        # Histogram
        st.write(f"### Distribution of {selected_column}")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

        # Boxplot
        st.write(f"### Boxplot of {selected_column}")
        fig, ax = plt.subplots()
        sns.boxplot(y=df[selected_column], ax=ax)
        st.pyplot(fig)
else:
    st.write("📂 Please upload a CSV file to get started.")

# Footer
st.sidebar.write("Developed with ❤️ using Streamlit")
