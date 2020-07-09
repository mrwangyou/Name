import os

# path = r"C:\Users\mrwan\Desktop\final_data"  # 文件夹目录
path = r"C:\Users\mrwan\Desktop\test_data"  # 测试用
files = os.listdir(path)  # 得到文件夹下的所有文件名称
for file in files:  # 遍历文件夹
    dataFinal = ''
    position = path + '\\' + file  # 构造绝对路径，"\\"，其中一个'\'为转义符
    with open(position, "r", encoding='utf-8') as f:  # 打开文件
        dataRaw = f.read()  # 读取文件
        wnn = 1
        while wnn:
            print(wnn)
            head = dataRaw.find('微博内容：') + 5
            tail = dataRaw.find('点赞数：')
            data = dataRaw[head: tail]
            dataRaw = dataRaw[tail + 4: -1]
            if dataRaw.find('微博内容：') == -1:  # 后面没有新微博的话停止这个用户的数据读取
                print('stop')
                wnn = 0
                continue
            if (data[0: 2] == '//') or \
               (data[0: 5] == '转发微博\n' and len(data) == 5) or \
               (data[0: 7] == 'Repost\n' and len(data) == 7):  # 纯转发的删删掉
                print('pure repost')
                continue
            if data.find(r"//<a href='/n/") != -1:  # 转发别人的内容删删掉
                data = data[0: data.find(r"//<a href='/n/")]
            data = data.replace(r"<br />", " ")  # 先处理转行

            # 处理所有a标签的（我真是仏了）
            head = data.find(r"<a ")
            while head != -1:
                tail = data.find(r"</a>") + 4
                subData = data[head: tail]
                print(subData)
                if subData[0: 16] == r"<a href=" + r"/status/":  # 先删掉展开全文
                    print('123')
                    data = data.replace(subData, '')
                    head = data.find(r"<a ")
                    continue
                if subData[0: 12] == r"<a href='/n/":  # 处理at
                    print('1234')
                    data = data.replace(subData, ' ttttt ')
                    head = data.find(r"<a ")
                    continue
                if subData.find('#') != -1:  # 处理hashtags
                    print('12345')
                    tepData = subData[subData.find('#') + 1:]
                    subText = tepData[0: tepData.find('#')]
                    data = data.replace(subData, ' ' + subText + ' ggggg ')
                    head = data.find(r"<a ")
                    continue
                print('123456')
                data = data.replace(subData, ' uuuuu ')
                head = data.find(r"<a ")

            # 处理表情
            head = data.find(r"<span ")
            while head != -1:
                tail = data.find(r"</span>") + 7
                subData = data[head: tail]
                data = data.replace(subData, ' eeeee ')

            dataFinal = dataFinal + data + '\n'


    newFile = file
    newFile = newFile.strip('weibo')
    newPos = path + '\\' + newFile
    with open(newPos, "w", encoding='utf-8') as f:
        if dataFinal != '':  # 保证不会写回空时出错（好像本身也不会出错的样子）
            f.write(dataFinal)
