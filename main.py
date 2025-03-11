import os

import dotenv

from frame_extracter import FrameExtracter

if __name__ == '__main__':
    # video_file_path = r''
    # output_folder_path = 'rilakkuma3'

    dotenv.load_dotenv()

    video_file_path = os.environ['vid']
    output_folder_path = os.environ['output']

    interval_seconds = 10
    frame_extractor = FrameExtracter(video_file_path, output_folder_path)
    frame_extractor.extract_at_interval(interval_seconds)
