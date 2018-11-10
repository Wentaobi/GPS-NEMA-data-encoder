# --encoding: utf-8--
"""
Author: AD OEM team
This script is to process Ottoview logging file,
For more detail, please contact Wentao
"""
import tkinter as tk
from tkinter import filedialog
import os
import time
# import re

# Initialization
path = os.chdir("/home/user/Desktop/check")
# check 'Wentao_delete_same_error.txt' exists or not
if os.path.exists("ErrorTest.txt"):
    os.remove("ErrorTest.txt")
else:
    print("The file does not exists 1")

# check 'error.txt' exist or not
if os.path.exists('Wentao_delete_same_error.txt'):
    os.remove('Wentao_delete_same_error.txt')
else:
    print("The file does not exists 2")

# Variables declaration

DIR = '/home/user/Desktop/check' 
filename1 = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) 

#for filename in os.listdir("/home/user/Desktop/2017.09.27.14.11.56_ces-sq5-four"):
#    print filename
#filename1 = []
#root = tk.Tk()
#root.withdraw()
#file_path = filedialog.askopenfilenames()
file_time = (time.ctime(os.stat(DIR).st_ctime))

# Choose file in GUI
#for f in file_path:
#    fo = f.split('/')
#    filename1.append((fo[-1]))
#print(len(filename1), filename1)
# Print all of file
#file_name1 = 
# index for search
n = 0
m = 0
rb = 0
errors_file = 0
save_file = open("ErrorTest.txt", "w")

# search error message in file content
for file in os.listdir("/home/user/Desktop/check"):
    (filepath, tempfilename) = os.path.split(file)
    (filename, extension) = os.path.splitext(tempfilename)
    #print(extension)
    if extension == "":
        n = n + 1
        errorfile = "Error" + filename
        # print("Useful files: %d" % n, file)
        print("file:" + str(n), file)
        with open(file) as f:
            save_file.write("===============================================================================================================" + "\n")
            save_file.write(str(file) + "\n" + "\n")
            errorfile = []
            content = f.readlines()
            """
            # if "ERROR" in content:
            #     errors_file = errors_file + 1
            #     print(errors_file)
            """
            # Find error txt
            content = [x.strip() for x in content]
            for lines in content:
                # print(lines)
                if "ERROR" in lines:
                    errorfile.append(lines)
                    feature = lines.split()[5]
                    # print(str(lines.split()[6:-1]))
                    save_file.write(str(" ".join(lines.split()[7:-1])).upper() + "\n")
                else:
                    pass
            # save_file.write(str(file) + " " +"===================================================================================" + "\n")
            # save_file.write("===============================================================================================================" + "\n")

    else:
        m = m + 1
        if extension == "rb":
            rb = rb + 1
        else:
            rb = m
        # for debugging
        # print("Useless files: %d" % m, file)

# close opening file
save_file.close()
f.close()
# count error message file
for file in os.listdir("/home/user/Desktop/check"):
    (filepath, tempfilename) = os.path.split(file)
    (filename, extension) = os.path.splitext(tempfilename)
    if extension == "":
        with open(file) as g:
            errorfile = []
            word = g.read().split(' ')
            if "ERROR" in word:
                errors_file = errors_file + 1
            else:
                pass
g.close
# process previous output file
rFile = open('ErrorTest.txt', 'r')
wFile = open('Wentao_delete_same_error.txt', 'w')
allLine = rFile.readlines()
rFile.close()
s = set()
for ii in allLine:
    s.add(ii)
for i in s:
    wFile.write(i)
wFile.close()

# for debugging
# open('Wentao_delete_same_error.txt', 'w').write(''.join(set(open('ErrorTest.txt').readlines())))

# Summary
print("Logging time:", file_time)
print("All log files :", filename1)
print("Ruby files : ", rb)
print("Useless files : ", m)
print("Readable files:", n)
print("Errors files:", errors_file)
print("\nCool!, You are Done!\n\n>>> start")

# write any header you want to the final file
with open('ErrorTest.txt', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    """
    f.write("Logging time:" + file_time + '\n' + "All log files :" + str(len(filename1)) + "\n" + "Ruby files : " + rb\
            + "\n" + "Useless files : " + m + "\n" + "Readable files:" + n + "Errors files:" + errors_file + "\n" + content)
            """
    f.write("Logging time:" + file_time + '\n' + "All log files :" + str(filename1)\
            + "\n" + "Useless files : " + str(m) + "\n" + "Readable files:" + str(n) + "\n" + "Errors files:" + str(errors_file)\
            + "\n" + "\n" + content)

with open('Wentao_delete_same_error.txt', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    """
    f.write("Logging time:" + file_time + '\n' + "All log files :" + str(len(filename1)) \
            + "\n" + "Useless files : " + m + "\n" + "Readable files:" + n + "Errors files:" + errors_file + "\n" + content)
            """
    f.write("Logging time:" + file_time + '\n' + content)
    # Process file begins
# todo: Check with Tonmoy and Bob for more detail

