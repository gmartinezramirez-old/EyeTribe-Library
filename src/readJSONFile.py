# -*- coding: cp1252 -*-
import csv
import json


def write_file_csv(filename, ts, time, x, y, left_eye_psize, right_eye_psize, diference_time):
    """Write the data readed from data server log into a line on a csv file separated by a space.

    Args:
        filename: string that is the filename of the readed data server log.
        ts: timestamp readed from log.
        x: x position of the gaze.
        y: y position of the gaze.
        left_eye_psize: size of the left eye pupil.
        right_eye_psize: size of the right eye pupil.
        diference_time: diference time between the actual and the last fixation.

    Returns:
        Call to csv library and write a row with de data args.
    """
    filename_without_extension = filename.split(".")[-1]
    extension = ".txt"
    output_filename_csv= filename + extension
    with open(output_filename_csv, 'ab') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=' ')
        csvWriter.writerow([ts,time, x, y, left_eye_psize, right_eye_psize, diference_time])

def read_json_file(filename):
    """

    Args:
        filename: filename (with extension) of the data server log.

    Returns:
        Call to write_file_csv function to write each json line readed to csv file.
    """
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
                    write_file_csv(filename, ts, time, x, y, left_eye_psize, right_eye_psize, diference_time)

