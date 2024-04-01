import cv2
from tqdm import tqdm
import os, time, subprocess

def extract_frames_from_video(video_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cap = cv2.VideoCapture(video_path)
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    pbar = tqdm(total=total_frames, desc="Extracting frames")

    # Extract every fourth frame in normal order
    for i in range(0, total_frames, 4):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(output_dir, f'frame_{i}.jpg'), frame)
        pbar.update(4)

    # Extract every third frame in reverse order
    for i in range(total_frames - 1, 0, -3):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(output_dir, f'frame_{i}_rev.jpg'), frame)
        pbar.update(3)
    pbar.close()
    print(f"Frames extracted from {video_path} and saved in {output_dir}")
    cap.release()


def extract_frames_from_video_old(video_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        if i % 2 == 0: 
            frame_filename = os.path.join(output_dir, f"frame_{i:04d}.jpg")
            cv2.imwrite(frame_filename, frame)    
            cap.release()

def run_colmap_feature_extractor(output_dir):
    try:
        start_time = time.time()  
        subprocess.run(["colmap", "feature_extractor", "--database_path", os.path.join(output_dir, "database.db"), "--image_path", output_dir])
        end_time = time.time()  
        elapsed_time = end_time - start_time
        print(f"Feature extraction completed in {elapsed_time:.2f} seconds")
    except subprocess.CalledProcessError as e:
        print(f"Error during feature extraction: {e}")

def run_colmap_sequential_matcher(output_dir):
    try:
        subprocess.run(["colmap", "sequential_matcher", "--database_path", os.path.join(output_dir, "database.db")])
        print("Sequential matching completed")
    except subprocess.CalledProcessError as e:
        print(f"Error matching sequentially: {e}")

def run_colmap_mapper(output_dir):
    sparse_dir = os.path.join(output_dir, "sparse")
    if not os.path.exists(sparse_dir):
        try:
            os.makedirs(sparse_dir) 
            print(f"Created sparse directory: {sparse_dir}")
        except OSError as e:
            print(f"Error creating sparse directory: {e}")
            return
    try:
        subprocess.run(["colmap", "mapper", "--database_path", os.path.join(output_dir, "database.db"), "--image_path", output_dir, "--output_path", sparse_dir])
        print(f"Sparse reconstruction saved in {sparse_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error mapping sparse reconstruction: {e}")

def run_colmap_model_converter(output_dir):
    try:
        subprocess.run(["colmap", "model_converter", "--input_path", os.path.join(output_dir, "sparse"), "--output_path", os.path.join(output_dir, "dense.ply"), "--ouput_type", "PLY"])
        print(f"Point cloud generated and saved as {os.path.join(output_dir, 'dense.ply')}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating point cloud: {e}")