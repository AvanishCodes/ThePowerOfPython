#Import the required packages
import qrcode as qr

def extract(text, result):
    # filepath = os.path.join(os.getcwd(), file)
    print(text)
    data = text
    result = result + ".png"
    img = qr.make(data)
    img.save(result)


text = input("Enter the text you want to convert QR : ")
result = input("Enter the name of the OutPut File : ")
extract(text, result)
print("Done")
# input()