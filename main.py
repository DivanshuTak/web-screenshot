import screenshot
import csv

file_name = raw_input("Enter csv file path \n")

with open(file_name , "rb") as f:
    reader = csv.reader(f)
    for row in reader:
    	#add file name where you want to save image
        screenshot.fullpage_screenshot_chrome(row[0], "/home/divanshu/new/"+row[1]+".png" )

