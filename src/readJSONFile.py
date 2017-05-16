# -*- coding: cp1252 -*-
import csv
import json


def write_filecsv(filename, ts, time, x, y,  leftEyepSize, rightEyepSize, diferenceTime):
    fileNameWithoutExtension = filename.split(".")[-1]
    extension = ".txt"
    outputFilenameCSV= filename + extension
    with open(outputFilenameCSV, 'ab') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=' ')
        csvWriter.writerow([ts,time, x, y,  leftEyepSize, rightEyepSize, diferenceTime])

def read_jsonfile(filename):
    last_user_time = 0
    with open(filename) as file:
        print "Processing: " + str(filename)
        for line in file:
            json_data = json.loads(line)
            if json_data["category"] == "tracker":
                if json_data["values"]["frame"]["fix"] == True:
                    ts = json_data["values"]["frame"]["timestamp"]
                    time = json_data["values"]["frame"]["time"]
                    x = json_data["values"]["frame"]["avg"]["x"]
                    y = json_data["values"]["frame"]["avg"]["y"]
                    left_eye_psize = json_data["values"]["frame"]["lefteye"]["psize"]
                    right_eye_psize = json_data["values"]["frame"]["righteye"]["psize"]
                    if last_user_time == 0:
                        diference_time = 0
                        last_user_time = time
                    else:
                        diference_time = time - last_user_time
                        last_user_time = time
                    write_filecsv(filename, ts, time, x, y, leftEyepSize, rightEyepSize, diferenceTime)

