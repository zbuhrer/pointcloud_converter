import cv2
import os
import subprocess
# import pycolmap

def extract_frames_from_video(video_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        if i % 2 == 0: # Capture every other frame
            frame_filename = os.path.join(output_dir, f"frame_{i:04d}.jpg")
            cv2.imwrite(frame_filename, frame)

    cap.release()

def run_colmap_subprocessmode(output_dir):
    subprocess.run(["colmap", "feature_extractor", "--database_path", os.path.join(output_dir, "database.db"),
                    "--image_path", output_dir])
    subprocess.run(["colmap", "exhaustive_matcher", "--database_path", os.path.join(output_dir, "database.db")])
    subprocess.run(["colmap", "mapper", "--database_path", os.path.join(output_dir, "database.db"),
                    "--image_path", output_dir, "--output_path", os.path.join(output_dir, "sparse")])
    subprocess.run(["colmap", "model_converter", "--input_path", os.path.join(output_dir, "sparse"),
                    "--output_path", os.path.join(output_dir, "dense.ply")])


def main():
    video_path = "data/video_input.mp4"
    output_dir = "data/frames_output"
    extract_frames_from_video(video_path, output_dir)
    print(f"Frames extracted from {video_path} and saved in {output_dir}")
    run_colmap_subprocessmode(output_dir)
    # print(f"Point cloud generated and saved as {os.path.join(output_dir, 'dense.ply')}")

if __name__ == "__main__":
    main()
