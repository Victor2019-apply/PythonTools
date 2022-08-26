# 生成txt文件后，使用如下命令，即可自动下载
# cat BvUrl.txt | xargs -n1 you-get --format=dash-flv -o ./王老菊-老头环/

fhandle = open('Bv.html','r')
bvfile = open('BvUrl.txt','w+')
for line in fhandle:
    if line.find('data-aid=') != -1:
        x = line.find('"')
        y = line.find('"',x+1)
        BvID = line[x+1:y]
        url = 'https://www.bilibili.com/video/'+BvID
        bvfile.write(url + '\n')
        print(url)

bvfile.close()
fhandle.close()