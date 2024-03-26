## **From The Author**

> I'll have to put on my personal roadmap to turn this into a formal document someday, but for now I'll leave this personal note here for usage instructions. Feel free to fork and extend, I'd be happy to collaborate. This is a fun personal project.
>
> @zbuhrer

## How To Use 
# Scanning/Recording 

Take a video that includes frames from as many angles of the subject as possible. You can use your phone! Modern smartpones have a lot of great video features, but try to use "Pro" mode if available to make sure that all of your depth information and other important meta data is saved to your video file.  

The subject should be well lit, and remain motionless. If it is a static object, Make sure to get your camera near crevices and details. Consider your subject and the surface supporting it — whether it is a wall or the floor. 

If your subject might move or twitch, or if your environment is not ideally static, you can use slow-motion features on your camera, but this can affect capture. 

Move to the next section when you have a video file that you think you can use.

# Using This App

First create a virtual environment.

```sh
python3 -m venv venv
```

Then install requirements. 

```sh
pip3 install -r requirements
```

You will also need to install **COLMAP** per your operating system requirements. Refer to their documentation.

If everything has installed properly and your system can technically handle the resources required to do it, then you can save your `mp4` video file as "`video_input.mp4`"

 you can simply execute the `main.py` script from the root of the project with your `Python`  environment of choice 

