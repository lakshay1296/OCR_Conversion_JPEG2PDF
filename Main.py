import os
import datetime
import csv
import platform

print(platform.architecture())

import ocrmypdf

#
# def main():
#
#     path = input("Enter the path of directory: ")
#     count = 0
#
#     # f = open("D:\\File_list.csv", "r+")
#     # reader = csv.DictReader(f)
#     # lis= []
#     # for row in reader:
#     #     lis.append(str(row["Path"]))
#
#     os.makedirs(path + "\\OCR", exist_ok="ignore")
#
#     for root, dir, files in os.walk(path):
#         for singFile in files:
#
#             if str(singFile).endswith(".pdf"):
#
#                     # # if str(singFile) not in lis:
#                     #     count = count + 1
#                     #
#                     #     old_file = singFile
#                     #     oldest_path = root + "\\" + old_file
#                     #
#                     #     if "-" in singFile:
#                     #         newFile = singFile.split("-")
#                     #         file_name = newFile[0] + ".pdf"
#                     #
#                     #     else:
#                     #         file_name = singFile
#                     #
#                     #     old_path = root + "\\" + singFile
#                     #     new_path = root + "\\" + file_name
#                     #     os.rename(old_path,new_path)
#                     #     print (singFile)
#                     #     print ("python pypdfocr.py " + new_path)
#                     #     os.system("python pypdfocr.py " + new_path)
#                     #     os.rename(new_path,oldest_path)
#
#                     # ocrmypdf.ocr(root + "\\" + singFile, root + "\\OCR\\" + singFile)
#
#
#                     print ("File" + str(count) + ":" + " " + singFile + " has been OCR'd")
#
#                     # else:
#                     #     pass
#
# if __name__ == '__main__':
#     lis = []
#
#     # Start Time
#     start_time = datetime.datetime.now()
#     lis.append(start_time)
#
#     # Main Function
#     main()
#
#     # End Time
#     end_time = datetime.datetime.now()
#     lis.append(end_time)
#
#     print ("Start Time: " + str(lis[0]))
#     print ("End Time: " + str(lis[1]))