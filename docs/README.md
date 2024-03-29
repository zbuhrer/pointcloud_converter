## **From The Author**

> *I'll have to put on my personal roadmap to turn this into a formal document someday, but for now I'll leave this personal note here for usage instructions. Feel free to fork and extend, I'd be happy to collaborate. This is a fun personal project.* - zbuhrer

## How To Use 
# Scanning/Recording 

Take a video that includes frames from as many angles of the subject as possible. You can use your phone! Modern smartpones have a lot of great video features, but try to use "Pro" mode if available to make sure that all of your depth information and other important meta data is saved to your video file.  

The subject should be well lit, and remain motionless. If it is a static object, Make sure to get your camera near crevices and details. Consider your subject and the surface supporting it — whether it is a wall or the floor. 

If your subject might move or twitch, or if your environment is not ideally static, you can use slow-motion features on your camera, but this can affect capture. 

Move to the next section when you have a video file that you think you can use.

You will also need to install **COLMAP** per your operating system requirements. Refer to their documentation.

If everything has installed properly and your system can technically handle the resources required to do it, then save your `mp4` video file as "`video_input.mp4`" in the root of the app directory. 

# BUT DON'T MASH GO ON THE JAMBOX JUST YET

> *"You should really know your own hardware and have an understanding of how much this will tax your system. I have an M2 Macbook and it took about 7 hours to process 1200 frames extracted from a 1:20@30fps video. This extracts every other frame by design for optimization; this might change.*
> 
> *"What I'm trying to say here is that when you run this, it might take a long time. If your video is huge, if your volume of frames are huge, this could take hours to __days__.*
> 
> *"If you're reading this in the future from when I wrote this you're probably laughing because you can do all of this on your cellphone. Good for you."* - zbuhrer

Now:

```sh
python3 main.py
```

And sit and wait. 