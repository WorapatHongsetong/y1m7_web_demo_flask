import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('Agg')

def sine(start: float, stop: float):
    x = np.linspace(start, stop, 200)
    y = np.sin(x)
    return x, y, "sine"

def cosine(start: float, stop: float):
    x = np.linspace(start, stop, 200)
    y = np.cos(x)
    return x, y, "cosine"

def tangent(start: float, stop: float):
    x = np.linspace(start, stop, 200)
    y = np.tan(x)
    return x, y, "tangent"

def square(start: float, stop: float):
    x = np.linspace(start, stop, 200)
    y = x ** 2
    return x, y, "square"

def sqrt(start: float, stop: float):
    x = np.linspace(start, stop, 200)
    y = np.sqrt(x)
    return x, y, "square root"

def plot(data: tuple[np.array, np.array, str], c: str="#9adfe6"):
    x, y, name = data[0], data[1], data[2]
    plt.clf()
    plt.plot(x, y, color=c, label=name)
    plt.title(f"Ploting function on {round(float(np.min(x)), 4), round(float(np.max(x)), 4)}")
    plt.legend()
    plt.savefig('./static/images/plot.jpeg', format='jpeg')

def plot_s(which_plot: list[str], start: float, stop: float, c: str="#9adfe6"):
    x = np.linspace(start, stop, 200)

    fig, axes = plt.subplots(len(which_plot), 1, figsize=(10, 8))

    for i, name in enumerate(which_plot):
        if name == 'sin':
            y = np.sin(x)
        elif name == 'cos':
            y = np.cos(x)
        elif name == 'tan':
            y = np.tan(x)
        elif name == 'square':
            y = x ** 2
        elif name == 'sqr':
            y = np.sqrt(x)

        axes[i].plot(x, y, label=name)
        axes[i].set_title(f"Ploting function on {round(float(np.min(x)), 4), round(float(np.max(x)), 4)}")
        axes[i].grid(True)
        axes[i].legend().set_visible(True)

    plt.tight_layout()
    plt.savefig('./static/images/plot.jpeg', format='jpeg')


if __name__ == "__main__":
    data = cosine(-10, 10)
    plot(data, c="#000")