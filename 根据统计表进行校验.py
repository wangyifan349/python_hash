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

# 根据记事本文件校验文件哈希值是否正确
def verify_files(hash_filepath):
    try:
        with open(hash_filepath, 'r') as f:   # 以只读方式打开哈希值文件
            for line in f.readlines():        # 对于每一行
                parts = line.strip().split('\t')
                if len(parts) == 2:           # 如果是有效的输出行
                    filepath = parts[0]
                    expected_hashvalue = parts[1]

                    actual_hashvalue = hash_file(filepath)  # 计算当前文件的哈希值
                    if actual_hashvalue == expected_hashvalue:  # 如果哈希值匹配
                        #print("{} 哈希值校验通过".format(filepath))
                        pass
                    else:                                    # 如果哈希值不匹配
                        print("{} 哈希值校验失败".format(filepath))
    except:
        print("无法读取哈希值文件：", hash_filepath)  # 输出错误

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:   # 如果命令行参数不足一个（程序名+哈希值文件）
        print("用法: {} <哈希值文件>".format(sys.argv[0]))
    else:
        verify_files(sys.argv[1])
