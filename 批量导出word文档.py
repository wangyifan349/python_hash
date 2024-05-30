import os  # 导入操作系统接口模块
import shutil  # 导入高级文件操作模块
import platform  # 导入平台检测模块
import psutil  # 导入系统和进程实用程序模块

def get_unique_filename(directory, filename):
    """
    如果目标目录中已存在同名文件，则为文件名添加数字后缀以确保唯一性。
    """
    base, extension = os.path.splitext(filename)  # 分离文件名和扩展名
    counter = 1  # 初始化计数器
    new_filename = filename  # 初始化新文件名

    while os.path.exists(os.path.join(directory, new_filename)):  # 检查文件是否存在
        new_filename = f"{base}_{counter}{extension}"  # 生成新的文件名
        counter += 1  # 增加计数器

    return new_filename  # 返回唯一的文件名

def find_external_drive():
    """
    自动检测系统中连接的外部驱动器。
    """
    system = platform.system()  # 获取操作系统类型
    external_drive = None  # 初始化外部驱动器变量

    if system == 'Windows':  # 如果是Windows系统
        partitions = psutil.disk_partitions()  # 获取所有磁盘分区
        for partition in partitions:  # 遍历每个分区
            if 'removable' in partition.opts:  # 检查是否为可移动驱动器
                external_drive = partition.mountpoint  # 获取驱动器挂载点
                break  # 找到后退出循环
    elif system in ['Darwin', 'Linux']:  # 如果是macOS或Linux系统
        potential_dirs = ['/Volumes', '/media']  # 定义可能的挂载目录
        for dir in potential_dirs:  # 遍历每个目录
            if os.path.exists(dir):  # 检查目录是否存在
                for item in os.listdir(dir):  # 列出目录中的所有项
                    item_path = os.path.join(dir, item)  # 获取项的完整路径
                    if os.path.ismount(item_path):  # 检查是否为挂载点
                        external_drive = item_path  # 获取外部驱动器路径
                        break  # 找到后退出循环
            if external_drive:  # 如果已找到外部驱动器
                break  # 退出外层循环

    return external_drive  # 返回外部驱动器路径

# 定义要遍历的目录
directories_to_search = [
    os.path.expanduser('~/Documents'),  # 我的文档目录
    os.path.expanduser('~/Downloads'),  # 下载目录
    os.path.expanduser('~/Desktop')  # 桌面目录
]

# 查找外部驱动器
external_drive = find_external_drive()  # 调用函数查找外部驱动器
if not external_drive:  # 如果未找到外部驱动器
    print("未找到外部驱动器。请确保驱动器已连接。")  # 打印提示信息
else:
    target_directory = os.path.join(external_drive, 'word_files')  # 定义目标目录路径

    # 确保目标目录存在
    if not os.path.exists(target_directory):  # 如果目标目录不存在
        os.makedirs(target_directory)  # 创建目标目录

    # 遍历指定的目录
    for directory in directories_to_search:  # 遍历每个指定的目录
        for root, dirs, files in os.walk(directory):  # 遍历目录中的所有文件和子目录
            for file in files:  # 遍历每个文件
                if file.endswith('.docx'):  # 如果文件是Word文档
                    source_file_path = os.path.join(root, file)  # 获取源文件路径
                    unique_filename = get_unique_filename(target_directory, file)  # 获取唯一的文件名
                    target_file_path = os.path.join(target_directory, unique_filename)  # 获取目标文件路径
                    shutil.copy2(source_file_path, target_file_path)  # 复制文件到目标目录
                    print(f'已复制 {source_file_path} 到 {target_file_path}')  # 打印复制信息

    print('所有Word文档已复制完成。')  # 打印完成信息
