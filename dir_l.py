import datetime
import os

dircount = 0
filecount = 0
filesizesum = 0
pwd = os.path.abspath('.')
print(' %s 的目录\n\n'%pwd)
for file in os.listdir('.'):
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y/%m/%d  %H:%M')
    flag = '<DIR>' if os.path.isdir(file) else ''
    if flag == '<DIR>':
        dircount+=1
    else:
        filecount+=1
    filesize = os.path.getsize(file)
    filesizesum += filesize
    print('%s\t%5s%10s %10s' %(modified_time,flag,filesize,file))
print('\t\t\t%d 个文件\t%d 字节'%(filecount,filesizesum))
print('\t\t\t%d 个目录\t'%(dircount))
    
