import os
import sys
import hashlib
#使用方法  python3 hash_files.py    /path/to/directory   /path/to/output.txt       后面是保存的记录位置，前面是便利的目录，这个程序会统计目录文件的指纹到后面这个记事本中。
# 本程序用于检查同步的文件是否正确。基本没有其他作用，这是生成的哈希表。
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
def traverse_dir(dirpath, output_filepath):
    with open(output_filepath, 'w') as f:   # 以只写方式打开输出文件
        for root, dirs, files in os.walk(dirpath):  # 遍历目录下的所有目录项
            for name in files:              # 对于每个文件
                filepath = os.path.join(root, name)
                hashvalue = hash_file(filepath)  # 计算文件哈希值
                if hashvalue is not None:
                    line = "{}\t{}\n".format(filepath, hashvalue)  # 构造输出行
                    f.write(line)               # 写入一行到输出文件
if __name__ == '__main__':

    if len(sys.argv) < 3:   # 如果命令行参数不足两个（程序名+目录+输出文件）
        print("用法: {} <目录> <输出文件>".format(sys.argv[0]))
    else:
        traverse_dir(sys.argv[1], sys.argv[2])
