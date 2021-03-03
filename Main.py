import argparse
import os
import shutil
import pandas as pd
import json
import datetime as dt
from Student import Student
from Teacher import Teacher
from pathlib import Path


SRC_DIR = "D:\Python"
BASE_DIR = "csv2json\csv_src"
tday = dt.datetime.today().strftime('%Y%m%d')
cformat = ['id', 'category', 'firstname', 'lastname', 'gender', 'dob', 'previous_school', 'doj', 'class', 'post',
               'salary', 'class_teacher_of', 'roll_no', 'emp_no', 'total_marks', 'city', 'aadhar_number',
               'contact_number', 'blood_group', 'subject_teaches', 'hs_stream', 'sec_percent']
my_parser = argparse.ArgumentParser(description='CSV To JSON')
my_parser.add_argument('filepath', metavar='Filepath', type=str, help='CSV filepath Converted to JSON Ex:"dir1/file.csv"')

args = my_parser.parse_args()
fname = args.filepath
bname = os.path.basename(fname)

if os.path.exists(fname):
    if fname.split(".")[-1] == 'csv':
        chk_df = pd.read_csv(fname)
        fformat = chk_df.columns.tolist()
        if cformat == fformat:
            sfname = os.path.join(SRC_DIR, BASE_DIR , bname)
            if os.path.exists(sfname):
                os.remove(sfname)
            shutil.move(fname, sfname)
            csv_df = pd.read_csv(sfname)
            st = Student(csv_df)
            st.prs_personal()
            srec = st.student_df()
            th = Teacher(csv_df)
            th.prs_personal()
            trec = th.teacher_df()
            jsdir = Path(input("Please enter the path to save json files: "))
            try:
                jsdir.mkdir(mode = 0o007, parents= True, exist_ok= True)
            except OSError:
                print("Failed to make directory")
            else:
                print(jsdir)
                sjname = 'Student_'+ tday +'.json'
                tjname = 'Teacher_' + tday + '.json'
                with open(Path(jsdir,sjname), "w", encoding='utf-8') as outfile:
                    json.dump(srec, outfile, indent=14)
                with open(Path(jsdir,tjname), "w", encoding='utf-8') as outfile:
                    json.dump(trec, outfile, indent=15)
                print('2 JSON files are successfully created')
        else:
            print("Invalid file format")
    else:
        print("Enter .csv file path")
else:
    print("Invalid File Path")


