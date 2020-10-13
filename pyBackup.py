import os
import shutil

def fileCrawler(inp):
    
    #Creates root destination folder if non existant
    if(os.path.exists(out) == False):
        os.makedirs(out)

    #Gets the current subfolder being analyzed from input
    stretchDir = inp.split(original_input)[-1]
    fileList = []
    dirList = []
    
    
    for file in os.listdir(inp):
        if os.path.isfile(inp+'\\'+file):
            if '.ini' not in file and '.drivedownload' not in file and '.dat' not in file:# <--- Args to not include these files
                fileList.append(file)
        elif os.path.isdir(inp+'\\'+file):
            dirList.append(file)
                

        
    for file in fileList:
            
        if(os.path.exists(out+'\\'+stretchDir) == False):
            os.makedirs(out+'\\'+stretchDir)
        
        if(os.path.exists(out+'\\'+stretchDir+"\\"+file)):
            if(os.path.getsize(out+'\\'+stretchDir+"\\"+file) != os.path.getsize(inp+"\\"+file)):
                shutil.copy(inp+"\\"+file, out+stretchDir)
                print(out+'\\'+stretchDir+"\\"+file, "Scanned and Updated")
            
            else:
                print((out+'\\'+stretchDir+"\\"+file),"Scanned but not Copied")
        else:
            shutil.copy(inp+"\\"+file, out+stretchDir)
            print(out+'\\'+stretchDir+"\\"+file, "Scanned and Backed Up")
            
                
    for file in dirList:
        fileCrawler(inp+"\\"+file)
                
                

if __name__ == '__main__':
    
    print('''  _____       ____             _                
 |  __ \     |  _ \           | |               
 | |__) |   _| |_) | __ _  ___| | ___   _ _ __  
 |  ___/ | | |  _ < / _` |/ __| |/ / | | | '_ \ 
 | |   | |_| | |_) | (_| | (__|   <| |_| | |_) |
 |_|    \__, |____/ \__,_|\___|_|\_|\__,_| .__/ 
         __/ |                           | |    
        |___/                            |_|
        
©2020 Robert Sammataro

''')
    
    
    
    #THESE LINES CONTROL WHERE YOU ARE COPYING TO/FROM
    print("Please enter source directory")
    inp = input()
    print("\nPlease enter target directory")
    out = input()
    
    
    original_input = inp
    fileCrawler(original_input)
    quit()
