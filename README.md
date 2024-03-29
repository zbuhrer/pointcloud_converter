Video to Point Cloud Converter
==============================

Convert videos into 3D point clouds using COLMAP.

Description
-----------

This project extracts frames from a video, runs COLMAP to create a point cloud, and saves it in PLY format. The resulting point cloud can be imported into anything you need for visualization and further manipulation.

![bus!](docs/bus.gif)
![tony!](docs/tonythepony.gif)

> *"I've been keeping a [journal](docs/JOURNAL.md) to provide more context as I learn how to make this."* - zbuhrer

Installation
------------

I'll elaborate on these steps in the future, but the quick 'n easy way to get this set up is as follows: 

* Install [COLMAP](https://colmap.github.io/install.html), referring to their instructions.
* Clone this project from Git:
    ```sh
    git clone https://github.com/zbuhrer/pointcloud_converter
    ```
* Create and activate a virtual environment (Linux/BSD environments):
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
* Install dependencies (while inside `venv`!):
    ```sh
    pip3 install -r requirements.txt
    ```
* Put your mp4 video file in the root of this project (rename it to `video_input.mp4`) — [refer to this documentation](docs/README.md#scanningrecording) for best practices.
* Start the application:
    ```sh
    python3 .
    ```

Your terminal window will produce a lot of output for several hours. Refer to the roadmap below if you think of something this isn't doing yet.

Roadmap
-------
* Let the user select filters to apply or ignore 
* Better logging/console output so it's more clear what it's doing 
    * Hey how about a loading bar at least? 
* System requirements documentation 
    * Need to work on a table of stats for models that I've extracted so they can be studied 
* UI? 
    * Should this be a console-only app? I've never made a GUI before, that could be fun! 


License
-------

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
