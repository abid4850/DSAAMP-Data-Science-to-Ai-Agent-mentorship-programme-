from flask import Flask, request, render_template
import pandas as pd
from utils.data_processing import load_data, clean_data
from plots.bar_plot import create_bar_plot
from plots.line_plot import create_line_plot
from plots.scatter_plot import create_scatter_plot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('plot_template.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    data = load_data(file)
    cleaned_data = clean_data(data)
    
    plot_type = request.form.get('plot_type')
    
    if plot_type == 'bar':
        plot = create_bar_plot(cleaned_data)
    elif plot_type == 'line':
        plot = create_line_plot(cleaned_data)
    elif plot_type == 'scatter':
        plot = create_scatter_plot(cleaned_data)
    else:
        return "Invalid plot type"
    
    return plot

if __name__ == '__main__':
    app.run(debug=True)