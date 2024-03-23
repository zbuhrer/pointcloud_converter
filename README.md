Video to Point Cloud Converter
==============================

Convert videos into 3D point clouds using COLMAP and visualize them in Blender.

Description
-----------

This project provides a Python script that extracts frames from a video, runs COLMAP to create a point cloud, and saves it in PLY format. The resulting point cloud can be imported into Blender for visualization and further manipulation.

Features
--------

-   Extract frames from a video.
-   Generate a dense point cloud using COLMAP.
-   Save the point cloud in PLY format.
-   Visualize the point cloud in Blender.

Installation
------------

1.  Install COLMAP:

    -   COLMAP is an open-source Structure-from-Motion (SFM) software. Install it by following the instructions on the COLMAP GitHub repository.
2.  Create a Python Virtual Environment (optional but recommended):

    ```
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    ```

3.  Install Dependencies:

    -   Install the required Python packages from the `requirements.txt` file:

    ```
    pip install -r requirements.txt

    ```

Usage
-----

1.  Place your video file (e.g., `your_video.mp4`) in the project directory.

2.  Run the script to extract frames and create the point cloud:

    ```
    python video_to_pointcloud.py

    ```

3.  The extracted frames will be saved in the `frames_output` directory, and the resulting point cloud will be saved as `dense.ply`.

4.  Open Blender, import the `dense.ply` point cloud, and explore it in 3D!

License
-------

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
