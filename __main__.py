import plyextract
from ui import gui

def main():
    video_path = "video_input.mp4"
    output_dir = "data/frames_output"
    plyextract.extract_frames_from_video(video_path, output_dir)
    plyextract.run_colmap_feature_extractor(output_dir)
    plyextract.run_colmap_sequential_matcher(output_dir)
    plyextract.run_colmap_mapper(output_dir)
    plyextract.run_colmap_model_converter(output_dir)

if __name__ == "__main__":
    main()
    # gui()