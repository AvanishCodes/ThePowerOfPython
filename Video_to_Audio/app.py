#Import the required packages
import moviepy.editor as moved
import os
import sys

def extract(file, verbose=False):
    # filepath = os.path.join(os.getcwd(), file)
    print(file)
    video = moved.VideoFileClip(file)
    audio = video.audio
    newFileName = str(file)[:-4] + ".mp3"
    print(newFileName)
    audio.write_audiofile(newFileName)


def main():
	verbose = False
	#checks for verbose flag
	if (len(sys.argv) > 1):
		if (sys.argv[1].lower() == "-v"):
			verbose = True
                    
	#finds present working dir
	pwd = os.getcwd()

	formats = ('.mp4', '.mkv')
	for file in os.listdir(pwd):
		if os.path.splitext(file)[1].lower() in formats:
			extract(file, verbose)
    # Declare that the task is completed
	print("Done")
    # input()

if __name__ == "__main__":
	main()