from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB, VideoWriter_fourcc, VideoWriter, destroyAllWindows
from rvmendillo_image_to_ascii import ImageToASCII
from PIL import Image
from numpy import array
from moviepy.editor import VideoFileClip, AudioFileClip
from os import remove, rename

class VideoToASCII:
    def __init__(self, video_path):
        self.video_path = video_path
        self.codec = VideoWriter_fourcc(*'MJPG')
    
    def save_ascii_animation(self, filename='ascii_animation.mp4', target_width=100, with_audio=True, inverted=True):
        video_input = VideoCapture(self.video_path)
        colored_ascii_images = []
        while True:
            available, frame = video_input.read()
            if not available:
                break
            converter = ImageToASCII(frame, from_array=True)
            if inverted:
                colored_ascii_image = converter.generate_colored_ascii_image(target_width)
            else:
                colored_ascii_image = converter.generate_colored_ascii_image(target_width, inverted=False)
            colored_ascii_images.append(colored_ascii_image)
        colored_ascii_pixels = [self.convert_image_to_pixels(colored_ascii_image) for colored_ascii_image in colored_ascii_images]
        width, height = colored_ascii_images[0].size
        filename = filename[:-4] + '_without_audio.mp4'
        frames_per_second = VideoFileClip(self.video_path).fps
        ascii_animation = VideoWriter(filename, self.codec, frames_per_second, (width, height))
        for colored_ascii_pixel in colored_ascii_pixels:
            ascii_animation.write(colored_ascii_pixel)
        self.release_resources(video_input, ascii_animation)
        video_output = VideoFileClip(filename)
        if not with_audio:
            video_output.ipython_display()
            remove(filename)
            filename = filename[:-18] + '.mp4'
            rename('__temp__.mp4', filename)
            return
        audio_output = VideoFileClip(self.video_path).audio
        video_with_audio_output = self.combine_video_with_audio(video_output, audio_output)
        video_with_audio_output.ipython_display()
        remove(filename)
        filename = filename[:-18] + '.mp4'
        rename('__temp__.mp4', filename)
            
    def convert_image_to_pixels(self, image):
        pixels = cvtColor(array(image), COLOR_BGR2RGB)
        return pixels
    
    def release_resources(self, video_input, video_writer):
        video_input.release()
        video_writer.release()
        destroyAllWindows()
    
    def combine_video_with_audio(self, video, audio):
        video_with_audio = video.set_audio(audio)
        return video_with_audio
