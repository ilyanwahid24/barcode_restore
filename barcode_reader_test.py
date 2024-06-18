import cv2
from pyzbar.pyzbar import decode

sample_path = "sample/"
output_path = "output/"

image = cv2.imread(output_path + "multiple_pic_sample4.jpeg")

detected_barcodes = decode(image)
for barcode in detected_barcodes:
    (x, y, w, h) = barcode.rect
    if barcode.data != "":
        print(barcode.data)
        print(barcode.type)

# print(barcode.data != "")
print(detected_barcodes)