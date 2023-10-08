import os
import hashlib
import shutil
#它在目录中寻找目录1中不存在的文件,但是目录二存在的图片，并将其复制到目录三.

# 函数用于计算文件的指纹（哈希值）
def calculate_blake2b_hash(file_path):
    blake2b_hash = hashlib.blake2b()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)  # 64KB缓冲区
            if not data:
                break
            blake2b_hash.update(data)
    return blake2b_hash.hexdigest()

# 函数用于遍历目录，找出所有图片和视频文件，并记录它们的文件路径和文件指纹
def find_image_and_video_files(directory):
    file_dict = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)        
            if file_size < 50 * 1024:#小于50kb跳过# Skip files smaller than 50KB (50 * 1024 bytes)
                continue
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp4', '.avi', '.mkv')):
                file_hash = calculate_file_hash(file_path)
                file_dict[file_hash] = file_path
    return file_dict

# 函数用于复制文件到目标目录，处理重名情况
def copy_file_with_unique_name(src_file, dest_directory):
    base_name = os.path.basename(src_file)
    file_name, file_ext = os.path.splitext(base_name)
    count = 1
    while True:
        dest_file_name = os.path.join(dest_directory, f"{file_name}_{count}{file_ext}")
        if not os.path.exists(dest_file_name):
            shutil.copy(src_file, dest_file_name)
            return dest_file_name
        count += 1

# 主程序
if __name__ == "__main__":
    directory1 = input("请输入第一个目录的路径：")
    directory2 = input("请输入第二个目录的路径：")
    directory3 = input("请输入第三个目录的路径：")
    #文件夹一是最大的，确保文件夹一的数据是完整和全面的，它会从目录2找自己缺少的部分。
    files_dict1 = find_image_and_video_files(directory1)
    files_dict2 = find_image_and_video_files(directory2)

    missing_files = []
    for file_hash, file_path in files_dict2.items():
        if file_hash not in files_dict1:
            missing_files.append(file_path)

    if missing_files:
        print(f"发现{len(missing_files)}个文件在第二个目录中，但不在第一个目录中。")
        for i, file_path in enumerate(missing_files, start=1):
            print(f"{i}. {file_path}")
        copy_files = input("是否要复制这些文件到第三个目录？(yes/no): ")
        if copy_files.lower() == "yes":
            for file_path in missing_files:
                dest_path = copy_file_with_unique_name(file_path, directory3)
                print(f"已将文件复制到第三个目录：{dest_path}")
        else:
            print("未执行文件复制操作。")
    else:
        print("第二个目录中的文件都存在于第一个目录中，无需复制。")
