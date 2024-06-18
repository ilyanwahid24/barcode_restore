import os


sample_path = 'sample'
output_path = 'output'

def file_list(path):
    return os.listdir(path)

sample_list = sorted(file_list(sample_path))
output_list = sorted(file_list(output_path))

exit = False
while(not exit):
    print("Below are the list of the sample pictures")
    for i in sample_list:
        print(f"{sample_list.index(i) + 1} {i}")
    selected_sample = int(input("Select the files by its number: ")) - 1
    