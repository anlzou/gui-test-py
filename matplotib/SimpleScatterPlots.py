import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

from mpl_toolkits import mplot3d


#单点散点图
def plots_1():
    x = np.linspace(0,10,30)
    y = np.sin(x)

    plt.plot(x,y,'o',color = 'red')
    plt.show()

#多点散点图
def plots_2():
    rng = np.random.RandomState(0)
    for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
        plt.plot(rng.rand(5), rng.rand(5), marker,label="marker='{0}'".format(marker))
    plt.legend(numpoints=1)
    plt.xlim(0, 1.8);
    plt.show()

# 泡泡图
def plots_3():
    rng = np.random.RandomState(0)
    x = rng.randn(100)
    y = rng.randn(100)
    colors = rng.rand(100)
    sizes = 1000 * rng.rand(100)

    plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,cmap='viridis')
    plt.colorbar();  # show color scale
    plt.show()

#饼图
def plots_4():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, (ax1, ax2) = plt.subplots(2)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
    ax1.axis('equal')
    ax2.pie(sizes, autopct='%1.2f%%', shadow=True, startangle=90, explode=explode,
            pctdistance=1.12)
    ax2.axis('equal')
    ax2.legend(labels=labels, loc='upper right')

    plt.show()

#3维散点图
def threeDPlots():
    # 绘制三角螺旋线
    import matplotlib.pyplot as plt
    import numpy as np

    ax = plt.axes(projection='3d')

    # 三维线的数据
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

    # 三维散点的数据
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

    plt.show()

#画圆
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
#三维等高线图
def threeDPolts_2():
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # 调整观察角度和方位角。这里将俯仰角设为60度，把方位角调整为35度
    ax.view_init(60, 35)
    plt.show()


if __name__ == '__main__':
    #plots_1()
    #plots_2()
    # plots_3()
    # plots_4()
    # threeDPlots()
    threeDPolts_2()