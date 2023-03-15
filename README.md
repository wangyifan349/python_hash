该项目包含两个Python脚本，分别为hash_file.py和verify_files.py。


hash_file.py
该脚本用于计算单个文件的SHA256哈希值，并将结果输出到命令行。用户可使用该脚本计算单个文件的哈希值，以进行文件完整性校验、文件比较等操作。


verify_files.py
该脚本用于校验指定目录下所有文件的哈希值是否与给定的哈希表文件一致。用户可使用该脚本对整个目录结构下的文件进行逐一校验，以保证文件的完整性和安全性。


在使用该脚本时，需要提供目标目录路径和哈希表文件路径。哈希表文件应使用制表符分隔每个文件名和其对应的哈希值。程序将读取哈希表文件中的每一行，并对其中指定的文件进行哈希计算。若计算出的哈希值与哈希表中给定的值不匹配，则程序将输出错误信息，提示文件的哈希值可能已被篡改。


通过使用该工具，用户可以方便地对存储在计算机上的重要文件进行快速的完整性校验，保障数据的安全性。
