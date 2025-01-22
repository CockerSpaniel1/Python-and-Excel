'''
File Input/Output
'''

import os
print("目前的工作目錄:",os.getcwd())

print("絕對路徑：",os.path.abspath('.'))    #目前的位置
print("絕對路徑：",os.path.abspath('..'))    #上一層的位置
print("絕對路徑：",os.path.abspath('Unit0401IO.py'))    #完整的位置

print("檔案大小:",os.path.getsize('Unit0401IO.py'),'位元組')
print("是否為檔案:",os.path.isfile('Unit0401IO.py'))
print("是否為目錄:",os.path.isdir('Unit0401IO.py'))
print("檔案是否存在:",os.path.exists('Unit0401IO.py'))
print("檔案是否存在:",os.path.exists('abc.py'))

#寫入檔案
print('\n\n-------write-------------')
slogan='Enjoy science Technology\n'
wf=open('slogan.txt','w')   #寫入
wf.write(slogan)
wf.close()

print('\n\n-------append-------------')
slogan='Human Technology\n'
wf=open('slogan.txt','a')   #附加
wf.write(slogan)
wf.close()

print('\n---append number----------------------')
i=100
wf=open('slogan.txt','a')
wf.write(str(i)) #必須要先轉型為字串,TypeError: write() argument must be str, not int
wf.close()

#讀取檔案內容
print('\n---Read file----------------------')
rf=open('slogan.txt','r')   #讀取
print(rf)

for line in rf:
    print(line, end='')
rf.close()

print('\n---Read file 2----------------------')
rf=open('slogan.txt','r') 
r=rf.read()
print(r)
rf.close()

print('\n---Read file 3----------------------')
rf=open('slogan.txt','r') 
r=rf.readlines()    #list, ['Enjoy science Technology\n', 'Human Technology\n', '100']
print(r)
rf.close()

print("\n--------使用with... as----------------")
with open('slogan.txt','r') as rf:
    for line in rf:
        print(line,end='')
    #rf.close()