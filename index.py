import cv2
import os
import time
import sys
from yt_dlp import YoutubeDL

# CHARACTERS
BONE_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def get_youtube_stream_url(youtube_url):
    """Getting URL"""
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'quiet': True,
        'no_warnings': True
    }
    print("Looking YouTube video")
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info['url']

def scale_image(image, new_width=100):
    """aspect settings"""
    (original_height, original_width) = image.shape[:2]
    aspect_ratio = original_height / original_width
    new_height = int(new_width * aspect_ratio * 0.55)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def main():
    # Kullanıcıdan YouTube linkini iste
    youtube_url = input("Paste your Youtube Link; ").strip()
    
    if not youtube_url:
        print("Its wrong link")
        return

    try:
        stream_url = get_youtube_stream_url(youtube_url)
        cap = cv2.VideoCapture(stream_url)
        
        if not cap.isOpened():
            print("ERROR; Video cant play")
            return

        fps = cap.get(cv2.CAP_PROP_FPS) if cap.get(cv2.CAP_PROP_FPS) else 30
        frame_delay = 1.0 / fps

        print("\nStarting... for stop do ctrl + C")
        time.sleep(1)

        # clear terminal and 
        os.system('cls' if os.name == 'nt' else 'clear')

        while cap.isOpened():
            start_time = time.time()
            ret, frame = cap.read()
            
            if not ret:
                break

            # small video for terminal
            resized_frame = scale_image(frame, new_width=100)
            h, w, _ = resized_frame.shape
            
            bone_frame = ""
            for y in range(h):
                for x in range(w):
                    # colors
                    b, g, r = resized_frame[y, x]
                    
                    # brightness of characters
                    brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
                    char = BONE_CHARS[brightness // 25]
                    
                    # color
                    bone_frame += f"\033[38;2;{r};{g};{b}m{char}"
                bone_frame += "\n"
            
            # for settings
            sys.stdout.write("\033[H" + bone_frame + "\033[0m")
            sys.stdout.flush()

            # FPS
            elapsed_time = time.time() - start_time
            if frame_delay > elapsed_time:
                time.sleep(frame_delay - elapsed_time)

    except KeyboardInterrupt:
        print("\nVideo stopped.")
    except Exception as e:
        print(f"\n an error: {e}")
    finally:
        if 'cap' in locals():
            cap.release()
        print("\033[0m\nProgram closed.") # clear colors

if __name__ == "__main__":
    main()
