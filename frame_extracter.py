import os
import random
import string
import time
from traceback import print_exc
from typing import Optional

import ffmpeg


def seconds_to_hms(seconds: int):
    return time.strftime('%H_%M_%S', time.gmtime(seconds))


def get_random_str(length: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))


class FrameExtracter:
    def __init__(self, video_file_path: str, output_folder_path: Optional[str] = None):
        self.video_file_path = video_file_path
        # set to the folder of the video file if output_folder_path is not specified
        self.output_folder_path = output_folder_path if output_folder_path is not None else os.path.dirname(self.video_file_path)

        if not os.path.isdir(self.output_folder_path):
            os.mkdir(self.output_folder_path)

        assert os.path.isfile(self.video_file_path), f'The given video file does not exist! ({self.video_file_path})'

    def extract_frame(self, timestamp: int):
        """
        Extracts a frame from the given MKV video at the specified timestamp.

        :param video_path: Path to the .mkv file
        :param output_image: Path to save the extracted frame (e.g., frame.jpg)
        :param timestamp: Time position in HH:MM:SS or seconds format
        """
        frame_file_path = os.path.join(self.output_folder_path, f'frame_{seconds_to_hms(timestamp)}_{get_random_str(5)}.png')
        try:
            (
                ffmpeg.input(self.video_file_path, ss=timestamp)  # Seek to the timestamp
                .output(frame_file_path, vframes=1)  # Extract one frame
                .run(overwrite_output=True, quiet=True)
            )
            print(f'Frame extracted at {timestamp} and saved to {frame_file_path}')
        except Exception as e:
            print(f'Error: {e}')
            print_exc()

    def extract_at_interval(self, interval_seconds: int):
        probe = ffmpeg.probe(self.video_file_path)
        video_duration = int(float(probe['format']['duration']))
        n_intervals = int(video_duration / interval_seconds)

        for i in range(n_intervals):
            self.extract_frame(timestamp=i * interval_seconds)
