import os
from typing import Optional

import fire

from frame_extracter import FrameExtracter


class CommandInterface(object):
    def frame(
        self,
        seconds: int,
        video_file_path: str,
        output_folder_path: Optional[str] = None,
    ):
        frame_extractor = FrameExtracter(video_file_path, output_folder_path)
        frame_extractor.extract_frame(seconds)

    def interval(
        self,
        interval_seconds: int,
        video_file_path: str,
        output_folder_path: Optional[str] = None,
    ):
        frame_extractor = FrameExtracter(video_file_path, output_folder_path)
        frame_extractor.extract_at_interval(interval_seconds)

    def interval_folder(
        self,
        interval_seconds: int,
        video_folder_path: str,
        output_folder_path: Optional[str] = None,
    ):
        for file in os.listdir(video_folder_path):
            if not (file.endswith('.mkv') or file.endswith('.mp4')):
                continue

            print(f'converting {file}...')
            file_path = os.path.join(video_folder_path, file)
            self.interval(interval_seconds, file_path, output_folder_path)


if __name__ == '__main__':
    fire.Fire(CommandInterface)
