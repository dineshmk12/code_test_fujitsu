from Personal import Personal

class Student(Personal):

    def student_df(self):
        self.stu_df1 = self.csv_obj.loc[self.csv_obj['category'] == 'student'].copy()
        self.stu_df1['grade'] = self.stu_df1['total_marks'].apply(lambda x: self.grade(x))
        self.stu_df1['hs_stream'] = self.stu_df1['hs_stream'].apply(lambda x: x.capitalize())
        self.stu_df = self.stu_df1[
            ['id', 'fullName', 'fgender', 'dob', 'age', 'aadhar_number', 'city', 'contact_number', 'roll_no', 'class',
             'total_marks', 'grade', 'sec_percent', 'hs_stream']].copy()
        self.stu_df['roll_no'] = self.stu_df['roll_no'].astype(int)
        self.stu_df['total_marks'] = self.stu_df['total_marks'].astype(int)
        self.stu_df['sec_percent'] = self.stu_df['sec_percent'].astype(int)
        self.stu_df.rename(
            columns={'aadhar_number': 'aadhar','fgender':'gender', 'contact_number': 'contactNumber', 'roll_no': 'rollNumber',
                     'class': 'className', 'total_marks': 'totalMarks', 'sec_percent': 'secPercent',
                     'hs_stream': 'hsStream'}, inplace=True)
        dct = self.stu_df.to_dict('records')
        fdct = {"studentRecordCount" : self.stu_df.shape[0],"data": dct}
        return fdct


