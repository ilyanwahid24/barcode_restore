import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
assets_path = "sample/"
output_path = "output/"
file_name = "barcode_example10"
file_extension = ".png"

img = cv2.imread(f"{assets_path + file_name + file_extension}")
if img is None:
    exit(-1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, gray_thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 1), np.uint8)
gray_eroded = cv2.erode(gray_thresh, kernel, iterations=4)

reduced_h = cv2.reduce(gray_eroded, 0, cv2.REDUCE_AVG)

reduced_h_graph = img.copy()
reduced_h_graph = cv2.copyMakeBorder(reduced_h_graph, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

for i in range(reduced_h.shape[1]):
    if reduced_h[0, i] > 150:
        cv2.line(reduced_h_graph, (i, reduced_h_graph.shape[0] - 101), (i, reduced_h_graph.shape[0]), (255, 255, 255), 1)

cropped_img = reduced_h_graph[-100:-1]
# original_img_shape = img.shape
# print(original_img_shape)
# edited_img_shape = reduced_h_graph.shape
# print(edited_img_shape)
# plt.imshow(cropped_img)
cv2.imwrite(f"{output_path + file_name + "_edited" + file_extension}", cropped_img)
# plt.show()
# cv2.imshow("final_img", cropped_img)
# cv2.destroyAllWindows()
# cv2.waitKey(0)
end_time = time.time()
print(f"Time to render: {end_time - start_time}s")