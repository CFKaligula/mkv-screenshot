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


if __name__ == '__main__':
    fire.Fire(CommandInterface)
