import matplotlib.pyplot as plt

def create_scatter_plot(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['x'], data['y'], color='blue', alpha=0.5)
    plt.title('Scatter Plot')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.grid(True)
    plt.savefig('scatter_plot.png')
    plt.show()