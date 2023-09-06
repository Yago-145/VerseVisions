import cv2
from moviepy.editor import VideoFileClip, AudioFileClip

def add_music_text(video_path, audio_path, lyrics, lyric_frames, out_dir):
   
    cap = cv2.VideoCapture(video_path)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'{out_dir}/video_with_text.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    frame_count = 0
    line_count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            
            if frame_count in lyric_frames:
                line_count = lyric_frames.index(frame_count)

            if line_count < len(lyrics):
                cv2.putText(frame, lyrics[line_count], (20, 480), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 28, 237), 1, cv2.LINE_AA)
            
            out.write(frame)
            frame_count += 1
        else:
            break

    cap.release()
    out.release()

    video = VideoFileClip(f"{out_dir}/video_with_text.mp4")
    audio = AudioFileClip(audio_path)

    if video.duration > audio.duration:
        video = video.subclip(0, audio.duration)

    video = video.set_audio(audio)

    video.write_videofile(f"{out_dir}/final_video.mp4")

    return
