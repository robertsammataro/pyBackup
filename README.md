pyBackup v1.0 Pre-Release  
Lightweight Program to Back Up Your Files!  
Build Date: 13 October 2020  

Introduction:  
pyBackup is a Lightweight program that allows you to back up your documents
any directory you choose!

PRERELEASE NOTE:  
- pyBackup is currently in development. Currently the software uses the
  command prompt for interfacing and ignores '.dat' '.ini' and '.drivedownload'
  files. These are developer-specific constraints for testing and will be
  removed upon release v1.0

KNOWN ISSUES:  
  - Windows Defender will automatically flag pyBackup.exe as a Trojan virus.
    Add an exception in Windows Defender to allow pyBackup to run or instead
    you may run the python script in the Python environment of your choice.
    Please reference the 'Additional Software' section of this README to
    ensure you have the necessary modules installed.



System Requirements:                 
- 2GB Memory                          
- Windows XP Service Pack 3 or Later  
- 8.5 MB Available Storage            


Additional Software:
pyBackup.exe will run without the need for any additional software. For those
looking to view the raw Python file, ensure you have installed the following
modules to ensure compatibility:
  - shutil


How to use:
  - After launch, enter the location of your source directory. pyBackup will
    automatically include all files and subfolders within the source directory
  - Next, enter your target directory. pyBackup will create an identical
    directory in the destination folder. If pyInstaller detects a file already
    exists in the target directory and is the same size as its equivelent in
    the source directory, it will skip copying that file.

Connect to a Home Network:
  - To have pyBackup send files to a home network or NAS server, first ensure
    that the desired server is mapped to a network drive. To do this, navigate
    to the target folder on your network and right click and select 'Map to
    Network Drive'. Once this step is complete, you can begin your target
    directory with the letter you assigned to the network drive.


Specs for Nerds:


  Written in Python 3.7.7  
  EXE compiled with PyInstaller v4.0  


  (C) 2020 Robert Sammataro  
  robertsammataro@gmail.com  
  github.com/robertsammataro
