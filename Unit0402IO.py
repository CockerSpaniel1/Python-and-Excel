import os

#os.mkdir("CurrentSeason")   #建立目錄,若資料夾已存在,則丟出FileExistsError: [WinError 183] 當檔案已存在時，無法建立該檔案。: 'CurrentSeason'

#os.remove("CurrentSeason")  #會丟出 PermissionError: [WinError 5] 存取被拒。: 'CurrentSeason'

#os.rmdir("CurrentSeason") #刪除目錄,FileNotFoundError: [WinError 2] 系統找不到指定的檔案。: 'CurrentSeason'

if(os.path.exists('slogan.txt')):
    os.remove('slogan.txt')
    print("\nfile deleted!!")
else:
    print("\nNo such file!!")

print("\n------------------------------------")
folder='ADS'
if(os.path.exists(folder)):    
    print("\n",folder, ' folder already exist!!')
else:
    os.mkdir(folder)
    print(folder," folder created!!")