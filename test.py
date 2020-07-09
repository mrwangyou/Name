import os

path = r"C:\Users\mrwan\Desktop\test_data"  # 测试用
files = os.listdir(path) #得到文件夹下的所有文件名称
txts = ""
for file in files: #遍历文件夹
    position = path + '\\' + file
    print(position)
    with open(position, "r", encoding='utf-8') as f:    #打开文件
        lines = f.readlines()   #读取文件中的一行
        for line in lines:
            # txts.append(line)
            txts = txts + line
        f.close()
    # with open(position, "w", encoding='utf-8') as f:
    #     f.write(txts)
print(txts[0: 5])
