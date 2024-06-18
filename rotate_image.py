import cv2

image_filename = "pic_sample1.jpeg"
image = cv2.imread('sample/' + image_filename,  cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_flipped = cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('output/rotated_' + image_filename, image_flipped)