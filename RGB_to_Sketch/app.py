#Import the required packages
import cv2
import os
import sys

def makeMySketch(file, verbose=False):
    # filepath = os.path.join(os.getcwd(), file)
    print(file)
    image = cv2.imread(file)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImageInv = 255 - grayImage
    grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)
    output = cv2.divide(grayImage, 255 - grayImageInv, scale = 256.0)
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
    # cv2.imshow("image", image)
    # cv2.imshow("pencilsketch", output)
    cv2.imwrite("sketch"+file, output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
	verbose = False
	#checks for verbose flag
	if (len(sys.argv) > 1):
		if (sys.argv[1].lower() == "-v"):
			verbose = True
                    
	#finds present working dir
	pwd = os.getcwd()

	formats = ('.jpg', '.jpeg')
	for file in os.listdir(pwd):
		if os.path.splitext(file)[1].lower() in formats:
			makeMySketch(file, verbose)
    # Declare that the task is completed
	print("Done")
    # input()

if __name__ == "__main__":
	main()