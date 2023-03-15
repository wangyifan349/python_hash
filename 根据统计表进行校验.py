import os
import hashlib

def hash_file(filepath):
    try:
        with open(filepath, 'rb') as f:                 # 以二进制只读方式打开文件
            hasher = hashlib.sha256()                   # 创建SHA256哈希值计算器
            buffer = f.read(4096)                       # 读取文件内容到缓冲区
            while len(buffer) > 0:
                hasher.update(buffer)                   # 更新哈希值计算器
                buffer = f.read(4096)                   # 继续读取文件内容到缓冲区
            return hasher.hexdigest()                   # 返回哈希值字符串
    except FileNotFoundError:                          # 如果无法找到文件，请记得完整同步下来!!!!
        print("无法找到文件:", filepath)              # 输出错误信息
        return None
    except:                                             # 如果出现其他异常
        print("无法对文件进行哈希计算:", filepath)       # 输出错误信息
        return None

# 校验文件哈希值是否正确
def verify_files(filepath, hash_filepath):
    if not os.path.isfile(filepath):                   # 如果文件夹路径不正确或文件不存在
        print("路径不正确或文件不存在:", filepath)      # 输出错误信息
        return

    if not os.path.isfile(hash_filepath):              # 如果哈希表文件不正确或文件不存在
        print("路径不正确或文件不存在:", hash_filepath) # 输出错误信息
        return

    with open(hash_filepath, "r") as f:                 # 以只读方式打开哈希表文件
        for line in f:                                  # 对于每一行
            parts = line.strip().split("\t")             # 分割文件名和哈希值
            if len(parts) == 2:                         # 如果是有效的输出行
                filename = os.path.join(filepath, parts[0])              # 拼接文件路径
                expected_hashvalue = parts[1]                                # 获取期望的哈希值
                actual_hashvalue = hash_file(filename)                     # 计算当前文件的哈希值

                if actual_hashvalue is None:                                # 如果哈希值计算失败
                    continue                                                # 跳过当前文件

                if actual_hashvalue == expected_hashvalue:                  # 如果哈希值匹配
                    pass                                                    # 不做任何操作
                else:                                                       # 如果哈希值不匹配
                    print("{} 哈希值校验失败".format(filename))          # 输出错误信息

if __name__ == "__main__":
    filepath = input("请输入要检查的文件夹路径: ")         # 获取要检查的文件夹路径
    hash_filepath = input("请输入哈希表文件路径: ")        # 获取哈希表文件路径
    verify_files(filepath, hash_filepath)                 # 校验文件哈希值是否正确
