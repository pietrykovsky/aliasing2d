from PIL import Image, ImageSequence

def generate_aliasing_animation(filename: str, path: str, number_of_frames: int):
    """Generate gif aliasing animation from given path to a gif file."""
    with Image.open(path) as gif:
        frames = []
        size = width, height = 256, 256
        lower = offset = height // number_of_frames
        prev = None
        for frame in ImageSequence.Iterator(gif):
            w, h = frame.size
            box = ((w - h)//2, 0, (w+h)//2, h)
            frame = frame.crop(box) # cut frame into square
            frame = frame.resize(size)  
            if prev is not None:
                box = (0, 0, width, lower)
                frame_crop = prev.crop(box)
                frame.paste(im=frame_crop, box=box)
                lower += offset
            frames.append(frame)
            prev = frame

        frames[0].save(filename, save_all=True, append_images=frames[1:])