# VideoToASCII

It generates and saves ASCII animation in MP4 format from a video file.

## Installation

Use the package manager [pip][pip-url] to install rvmendillo-video-to-ascii.

```bash
pip install rvmendillo-video-to-ascii
```

## Usage

```python
# Imports the VideoToASCII class from the rvmendillo_video_to_ascii package
from rvmendillo_video_to_ascii import VideoToASCII

# Instantiates the converter with a video file
app = VideoToASCII('test_video.mp4')

# Saves inverted ASCII animation for black background with a target width of 200 pixels in an MP4 file
app.save_ascii_animation('inverted_ascii_animation.mp4', target_width=200)

# Saves inverted ASCII animation for black background without an audio and with a target width of 200 pixels in an MP4 file
app.save_ascii_animation('inverted_ascii_animation_without_audio.mp4', with_audio=False, target_width=200)

# Saves ASCII animation for white background with a target width of 200 pixels in an MP4 file
app.save_ascii_animation('ascii_animation.mp4', target_width=200, inverted=False)

# Saves ASCII animation for white background without an audio and with a target width of 200 pixels in an MP4 file
app.save_ascii_animation('ascii_animation_without_audio.mp4', with_audio=False, target_width=200, inverted=False)
```

## License
[MIT][mit-license]

[pip-url]: https://pip.pypa.io/en/stable/
[mit-license]: https://choosealicense.com/licenses/mit/
