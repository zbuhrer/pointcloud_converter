Video to Point Cloud Converter
==============================

Convert videos into 3D point clouds using COLMAP.

Description
-----------

This project extracts frames from a video, runs COLMAP to create a point cloud, and saves it in PLY format. The resulting point cloud can be imported into anything you need for visualization and further manipulation.

![bus!](docs/bus.gif)
![tony!](docs/tonythepony.gif)

> *"I've been keeping a [journal](docs/JOURNAL.md) to provide more context as I learn how to make this."* - zbuhrer

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
