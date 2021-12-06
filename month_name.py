import calendar
import os

YEAR = '_2021'

def DirectoryNameFormat(monthNo, startSrt, endStr):
    if (monthNo<1 or monthNo>12):
        raise IndexError("monthNo out of range")
    m = ''
    m += startSrt
    m += str(monthNo)
    m += '_'
    m += calendar.month_name[monthNo]
    m += endStr
    return m

def CreateAListOfMonthsNames(year):
    month =  [DirectoryNameFormat(i, '0', year) for i in range(1,10)]
    month += [DirectoryNameFormat(i, '',  year) for i in range(10,13)]
    return month

def CreateADirectory(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print(path)
        
def CreateDirectoriesFromAList(l):
    for i in l:
        CreateADirectory(i)
    
def CreateADirectoryForEachMonth(year):
    monthNames = CreateAListOfMonthsNames(year)
    CreateDirectoriesFromAList(monthNames)
    
def Main():
    CreateADirectoryForEachMonth(YEAR)
    print('end')
    
if __name__ == '__main__':
    Main()
    

     
     

