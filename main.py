import os

import dotenv

from ci import CommandInterface

if __name__ == '__main__':
    # video_file_path = r''
    # output_folder_path = 'rilakkuma3'

    dotenv.load_dotenv()

    video_file_path = os.environ['vid']
    output_folder_path = os.environ['output']

    interval_seconds = 10
    frame_extractor = CommandInterface().interval_folder(interval_seconds, video_file_path, output_folder_path)
