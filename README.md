# 🎬 Color Bone Video Player

This project allows you to play any YouTube video directly in your terminal as **24-bit color Bone art** without downloading the file. It streams the video in real-time using Python, OpenCV, and `yt-dlp`.

---

## 🚀 Features

* **Real-time YouTube Streaming:** Play videos instantly via URL without any manual downloads.
* **TrueColor (24-bit) Support:** Unlike traditional black-and-white Bone  players, this reads the original RGB channels of each pixel and renders them perfectly in the terminal.
* **Flicker-Free Rendering:** Uses advanced ANSI escape codes instead of standard screen-clearing commands (`cls`/`clear`) for a smooth viewing experience.
* **Aspect Ratio Correction:** Accounts for the vertical stretching of terminal fonts to prevent the video from looking distorted.

---

## 🛠️ Installation & Setup

To run this project, make sure you have **Python 3** installed on your system.

### 1. Install Required Dependencies
Open your terminal or CMD and run the following command to install the necessary libraries:

```bash
pip install opencv-python yt-dlp
```
## 2. Clone the Repository
Clone the repository using Git and navigate into the project directory:
```bash
git clone [https://github.com/your_username/bone-videoplayer.git](https://github.com/your_username/bone-videoplayer.git)
cd bone-videoplayer
```

### 💻 Usage
To start the player, execute the main script index.py using Python:
```bash
python index.py
```
Once the script is running, the terminal will prompt you to enter a YouTube link. Simply paste your URL and press Enter
If you want stop press ctrl + C
### have a fun :)
