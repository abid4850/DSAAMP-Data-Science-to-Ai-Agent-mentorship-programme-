# Data Visualization Application

This project is a web application that allows users to input data and generate various types of plots, including bar plots, line plots, and scatter plots. The application is built using Flask and utilizes popular data visualization libraries such as Matplotlib and Seaborn.

## Project Structure

```
data-visualization-app
├── src
│   ├── app.py                # Main entry point of the application
│   ├── data
│   │   └── input_data.csv    # Input data in CSV format
│   ├── plots
│   │   ├── bar_plot.py       # Function to create bar plots
│   │   ├── line_plot.py      # Function to create line plots
│   │   └── scatter_plot.py    # Function to create scatter plots
│   ├── utils
│   │   └── data_processing.py # Functions for data processing
│   └── templates
│       └── plot_template.html # HTML template for rendering plots
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to ignore by Git
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd data-visualization-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage

- Upload your CSV file containing the data you want to visualize.
- Choose the type of plot you want to generate (bar, line, or scatter).
- View the generated plot rendered in the web application.

## Available Plots

- **Bar Plot**: Visualizes categorical data with rectangular bars.
- **Line Plot**: Displays information as a series of data points called 'markers' connected by straight line segments.
- **Scatter Plot**: Shows the relationship between two numerical variables using dots.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to add.

## License

This project is licensed under the MIT License - see the LICENSE file for details.