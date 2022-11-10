import os
from propeller import generate_propeller_animation
from sensor import generate_aliasing_animation

if __name__ == '__main__':
    propeller_dir = 'propeller_animations'
    aliasing_dir = 'aliasing_animations'
    if not os.path.exists(propeller_dir):
        os.makedirs(propeller_dir)
    if not os.path.exists(aliasing_dir):
        os.makedirs(aliasing_dir)
    
    number_of_frames = 64
    for number_of_blades in range(3,10,2):
        filename = f'propeller_{number_of_blades}blades_{number_of_frames}frames.gif'
        propeller_path = os.path.join(propeller_dir, filename)
        generate_propeller_animation(propeller_path, number_of_blades, number_of_frames)
        aliasing_path = os.path.join(aliasing_dir, filename)
        generate_aliasing_animation(aliasing_path, propeller_path, number_of_frames)