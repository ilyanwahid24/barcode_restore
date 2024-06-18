import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

# Library Python yang diperlukan untuk menjalankan program.
# 1. opencv
# 2. numpy
# 3. matplotlib
# 4. time
# 5. sys

start_time = time.time()

# Deklarasi lokasi sample gambar
assets_path = "sample/"

# Deklarasi lokasi output gambar
output_path = "output/"
# name_prefix = "barcode_example"
#file_name = "barcode_example10"

# Menyimpan argumen berindex 1 dari python
file_name = sys.argv[1].split('.')[0]

# Ekstensi file yang bisa digunakan
file_extension = "." + sys.argv[1].split('.')[1]

# cv2.imread digunakan untuk membaca file gambar menggunakan function imread dari library opencv dan datanya disimpan di variable img
img = cv2.imread(f"{assets_path + file_name + file_extension}")

# Jika variable img tidak berisi data program akan berhenti
if img is None:
    exit(-1)

# Merubah format warna gambar menggunakan function cvtColor menjadi grayscale dan disimpan pada variable img_gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Membuat treshold dari gambar yang berformat greyscale
_, gray_thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)


kernel = np.ones((5, 1), np.uint8)

# Digunakan untuk mengerosi gambar
gray_eroded = cv2.erode(gray_thresh, kernel, iterations=4)

# Mereduce gambar yang sudah dierosi
reduced_h = cv2.reduce(gray_eroded, 0, cv2.REDUCE_AVG)

# Menduplikasi img
reduced_h_graph = img.copy()

# Membuat border pada gambar reduced_h_graph
reduced_h_graph = cv2.copyMakeBorder(reduced_h_graph, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))


for i in range(reduced_h.shape[1]):
    if reduced_h[0, i] > 150:
        # Membuat garis pada reduced_h_graph dengan koordinat seperti dibawah, dengan warna hitam dan ketebalan 1
        cv2.line(reduced_h_graph, (i, reduced_h_graph.shape[0] - 101), (i, reduced_h_graph.shape[0]), (255, 255, 255), 1)

# Memotong gambar hanya pada barcode yang direstorasi
cropped_img = reduced_h_graph[-100:-1]

# Menyimplan Hasil Gambar
cv2.imwrite(f"{output_path + file_name + "_edited" + file_extension}", cropped_img)

end_time = time.time()
print(f"Time to render: {end_time - start_time}s")

# Cara Penggunaan
# python main.py {nama_file}
# Contoh:
# python barcode_restoration.py barcode_example1.png