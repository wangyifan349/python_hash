import os
import hashlib

# 计算文件的SHA256哈希值
def hash_file(filepath):
    try:
        with open(filepath, 'rb') as f:     # 以二进制只读方式打开文件
            hasher = hashlib.sha256()       # 创建SHA256哈希值计算器
            buffer = f.read(4096)           # 读取文件内容到缓冲区
            while len(buffer) > 0:
                hasher.update(buffer)       # 更新哈希值计算器
                buffer = f.read(4096)       # 继续读取文件内容到缓冲区
            return hasher.hexdigest()       # 返回哈希值字符串
    except:
        print("无法对文件进行哈希计算：", filepath)  # 输出错误信息
        return None

# 遍历目录，并将每个文件的哈希值保存到指定的文本文件中
def traverse_dir(dirpath):
    output_filepath = os.path.join(os.getcwd(), "hash_values.txt") # 生成输出文件路径
    with open(output_filepath, 'w') as f:   # 以只写方式打开输出文件
        for root, dirs, files in os.walk(dirpath):  # 遍历目录下的所有目录项
            for name in files:              # 对于每个文件
                filepath = os.path.join(root, name)
                hashvalue = hash_file(filepath)  # 计算文件哈希值
                if hashvalue is not None:
                    line = "{}\t{}\n".format(filepath, hashvalue)  # 构造输出行
                    f.write(line)               # 写入一行到输出文件
                    print("{} 的哈希值为：{}".format(filepath, hashvalue)) # 输出计算位置和哈希值

if __name__ == '__main__':
    dirpath = input("请输入要遍历的目录路径：")#开始接受一个路径
    if not os.path.exists(dirpath) or not os.path.isdir(dirpath): # 检查路径是否存在并且是否为目录
        print("输入的路径不存在或者不是一个目录。")
    else:
        traverse_dir(dirpath)
