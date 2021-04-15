import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import math
import numpy as np


def gerar2d(func):
    x = np.array(range(-20, 20))

    try:
        y = eval(f'{func}')
        plt.plot(x,y)

        plt.show()
    except:
        pass

def gerar3d(func):
    try:
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        def z_function(x, y):
            return eval(f'{func}')

        x = np.linspace(-6, 6, 30)
        y = np.linspace(-6, 6, 30)

        X, Y = np.meshgrid(x, y)
        Z = z_function(X, Y)
        ax.plot_wireframe(X, Y, Z, color='green')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                        cmap='winter', edgecolor='none')
        ax.set_title('surface');

        plt.show()
    except:
        pass
