# #python Excel VBA
import win32com.client as win32

xl=win32.Dispatch('Excel.Application') #開啟Excel


xl.Workbooks.Open(Filename=r'C:\mypy\myproject\Unit1206VBA.xlsm') #開啟巨集

xl.Application.Run("cpc")

result = xl.Application.Run("budget", "Google", 1000)  # 執行巨集
print(result)

xl.Application.Quit()
del xl



