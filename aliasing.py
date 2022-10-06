import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# number of blades
n = 3 
theta = np.linspace(0, 2*np.pi, 1000)
r = np.sin(n*theta)

fig = plt.figure()
ax = fig.add_subplot(polar=True)
line, = ax.plot(theta, r)

def update(M):
    m=M/2
    r = np.sin(n*theta+m*np.pi/10)
    line.set_ydata(r)
    return line,
anim = animation.FuncAnimation(fig, update, interval=20)
plt.show()
