from frame_extracter import FrameExtracter

if __name__ == '__main__':
    video_file_path = r''
    output_folder_path = 'rilakkuma3'

    interval_seconds = 10
    frame_extractor = FrameExtracter(video_file_path, output_folder_path)
    frame_extractor.extract_at_interval(interval_seconds)
