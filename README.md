Video to Point Cloud Converter
==============================

Convert videos into 3D point clouds using COLMAP and visualize them in Blender.

Description
-----------

This project extracts frames from a video, runs COLMAP to create a point cloud, and saves it in PLY format. The resulting point cloud can be imported into Blender for visualization and further manipulation.

![bus!](docs/bus.gif)

> *"This isn't the best example of what this can do, but the bus scan is the best I've come up with so far. Check the [examples](docs/README.md#examples) for more context."* - zbuhrer

Features
--------

-   Extract frames from a video.
-   Generate a dense point cloud using COLMAP.
-   Save the point cloud in PLY format.
-   Visualize the point cloud in Blender.

Installation
------------

1.  Install COLMAP:

    -   COLMAP is an open-source Structure-from-Motion (SFM) software. Install it by following the instructions on the COLMAP GitHub repository. https://github.com/colmap/colmap
  
2.  Create a Python Virtual Environment:
    ```shell
    python3 -m venv venv
    ```

    Activate the virtual environment
    ```shell
    source venv/bin/activate
    ```
    (On Windows activate by using `venv\Scripts\activate`)


4.  Install Dependencies:

    -   Install the required Python packages from the `requirements.txt` file:

    ```shell
    pip install -r requirements.txt
    ```

Usage
-----

1.  Place your video file (e.g., `your_video.mp4`) in the project directory.

2.  Run the script to extract frames and create the point cloud:

    ```shell
    python video_to_pointcloud.py
    ```

3.  The extracted frames will be saved in the `frames_output` directory, and the resulting point cloud will be saved as `dense.ply`.

4.  Open Blender, import the `dense.ply` point cloud, and explore it in 3D!

License
-------

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
