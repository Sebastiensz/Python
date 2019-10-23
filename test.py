def extract_frames_for_video_at_intervals(video_path, interval, out_directory_path):

    clip = mpy.VideoFileClip(video_path)

    iterations = int(clip.duration / interval)

    time_counter = 0

    i=0

    for iteration in range(iterations):

        time_counter += interval

        i=i+1

        print("Exporting image at {0} seconds...".format(str(time_counter)))

        #file_name = "Video_{0}.png".format(str(time_counter))

        file_name = "Video_{0}.png".format(i)

        out_path = os.path.join(out_directory_path, file_name)

        clip.save_frame(out_path, (time_counter))

        if i==500:

            break

        else:

            pass 
