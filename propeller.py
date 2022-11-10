import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_propeller_animation(filename: str, number_of_blades: int, number_of_frames: int):
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

    anim = animation.FuncAnimation(fig, update, frames=number_of_frames, interval=50)
    anim.save(filename)
