import pyttsx3
import os

# 初始化pyttsx3引擎
engine = pyttsx3.init()

# 获取并打印当前可用的声音
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice[{i}]: {voice.name}")

# 选择特定的声音
voice_id = 0  # 修改这个值来选择不同的声音
engine.setProperty('voice', voices[voice_id].id)

# 设置音量，取值范围是0.0到1.0
engine.setProperty('volume', 0.8)  # 设置为80%的音量

# 设置语速，值越大语速越快
engine.setProperty('rate', 150)  # 设置为每分钟150个词

# 要读取的记事本文件路径
note_file_path = 'note.txt'

# 检查文件是否存在
if not os.path.isfile(note_file_path):
    print(f"文件 {note_file_path} 不存在，请检查文件路径。")
    exit()

# 读取记事本内容
with open(note_file_path, 'r', encoding='utf-8') as note_file:
    note_content = note_file.read()

# 保存声音到本地文件
output_audio_file = 'output_audio.mp3'  # 保存为mp3格式

# 保存到音频文件
engine.save_to_file(note_content, output_audio_file)

# 运行并等待朗读任务完成
engine.runAndWait()

print(f'朗读内容已保存到 "{output_audio_file}"')
