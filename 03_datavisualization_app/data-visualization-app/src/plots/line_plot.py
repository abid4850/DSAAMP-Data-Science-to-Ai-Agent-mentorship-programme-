import matplotlib.pyplot as plt

def create_line_plot(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['x'], data['y'], marker='o')
    plt.title('Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.tight_layout()
    plt.show()