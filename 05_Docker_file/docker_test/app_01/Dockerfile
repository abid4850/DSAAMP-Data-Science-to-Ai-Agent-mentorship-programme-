# Dockerfile

# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Streamlit specific configs (preventing it from asking for credentials etc.)
ENV STREAMLIT_HOME="/app"
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Run the Streamlit app
CMD ["streamlit", "run", "your_app.py"]


# CMD bash
# source .venv/Scripts/activate
# streamlit run app.py
# python -m venv .venv
# pip freeze > reqrirements.txt
# docker build -t my-streamlit-app .


