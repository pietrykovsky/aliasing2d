import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

blades = 3   # number of blades
frames = 64  # number of frames

def generate_propeller_animation(number_of_blades, number_of_frames):
    """Generate gif sequence of animated propeller."""
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(number_of_blades*theta)

    fig = plt.figure()
    ax = fig.add_subplot(polar=True)
    line, = ax.plot(theta, r)

    def update(M):
        offset = number_of_frames/2
        m=(M-offset)/2
        r = np.sin(number_of_blades*theta+m*np.pi/10)
        line.set_ydata(r)
        return line,

    anim = animation.FuncAnimation(fig, update, frames=number_of_frames)
    anim.save('prop.gif')
