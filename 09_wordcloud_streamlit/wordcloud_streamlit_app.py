import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# add title 
st.title("Data Visualization and Analysis App")
st.subheader("This is a simple data analysis application to created by Abid Hussain")

# Load the dataset
# Dropdown to select a dataset
dataset_options = ['iris', 'titanic', 'tips', 'diamonds']
selected_dataset = st.selectbox("Choose a dataset", dataset_options)

# File uploader for custom dataset
uploaded_file = st.file_uploader("Or upload your own CSV file", type=["csv","xlsx"])

# Load the selected or uploaded dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Custom dataset uploaded successfully!")
else:
    df = sns.load_dataset(selected_dataset)
    st.success(f"Loaded '{selected_dataset}' dataset from seaborn.")

st.write("Preview of the dataset:")
st.dataframe(df)

# Display the number of rows and columns
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")   

# Display the coulumn names of selected dataset with their data types
st.write("Column names and data types:", df.dtypes)

# Print the null values in the dataset
if df.isnull().sum().sum() > 0:
    st.write("Null Values:", df.isnull().sum().sort_values(ascending=False))
else:
    st.write("No null values in the dataset.")

# Display Summary Statistics
st.write("Summary Statistics", df.describe())

# Select a column for X or y axis from dataset and also select a plot types
#x_col = st.selectbox("Select a column for X-axis", df.columns)
#y_col = st.selectbox("Select a column for Y-axis", df.columns)
#plot_type = st.selectbox("Select a plot type", ["line", "bar", "scatter", "histogram", "kde"])
#
#
## Plot the data
#if plot_type == "line":
#    st.line_chart(df[x_col, y_col])
#elif plot_type == "bar":
#    st.bar_chart(df[x_col, y_col])
#elif plot_type == "scatter":
#    st.scatter_chart(df[[x_col, y_col]])
#elif plot_type == "hist":
#    st.hist(df[x_col, y_col])
#elif plot_type == "kde":
#    st.kde(df[x_col, y_col])
#else:
#    st.error("Invalid plot type selected.")

# Create a pairplot of the dataset
st.subheader("Pairplot of the dataset")
hue_column = st.selectbox("Select a column for hue", df.columns)
st.pyplot(sns.pairplot(df, hue=hue_column))

# Create a correlation heatmap
st.subheader("Correlation Heatmap")

# Select columns which are numeric and then create a correlation heatmap
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
corr_matrix = df[numeric_columns].corr()

# convert the seaborn heatmap to a Plotly heatmap
heatmap_fig = go.Figure(data=go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    colorscale='Viridis'
))
st.plotly_chart(heatmap_fig)

