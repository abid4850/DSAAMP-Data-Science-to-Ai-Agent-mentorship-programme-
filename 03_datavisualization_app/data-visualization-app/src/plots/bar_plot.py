import matplotlib.pyplot as plt

def create_bar_plot(data):
    """
    Generates a bar plot from the provided data.

    Parameters:
    data (DataFrame): A pandas DataFrame containing the data to plot.

    Returns:
    None: Displays the bar plot.
    """
    # Assuming 'Category' and 'Value' are columns in the DataFrame
    plt.figure(figsize=(10, 6))
    plt.bar(data['Category'], data['Value'], color='skyblue')
    plt.title('Bar Plot')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()