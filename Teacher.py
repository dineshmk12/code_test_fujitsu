from Personal import Personal


class Teacher(Personal):
    def teacher_df(self):
        self.tea_df1 = self.csv_obj.loc[self.csv_obj['category'] == 'teacher'].copy()
        self.tea_df1['serperiod'] = self.tea_df1['doj'].apply(lambda x: self.calculateage(x))
        self.tea_df1['post'] = self.tea_df1['post'].apply(lambda x: x.capitalize())
        self.tea_df = self.tea_df1[
            ['id', 'fullName', 'fgender', 'dob', 'age', 'aadhar_number', 'city', 'contact_number', 'emp_no',
             'class_teacher_of', 'doj', 'serperiod', 'previous_school', 'post', 'salary']].copy()

        self.tea_df['salary'] = self.tea_df['salary'].apply(lambda x: '{:,.2f}'.format(x))
        self.tea_df.rename(
            columns={'aadhar_number': 'aadhar', 'fgender':'gender','contact_number': 'contactNumber', 'emp_no': 'empNo',
                     'class_teacher_of': 'classTeacher', 'serperiod': 'servicePeriod', 'previous_school': 'previousSchool'}, inplace=True)
        dct = self.tea_df.to_dict('records')
        fdct = {"teacherRecordCount": self.tea_df.shape[0], "data": dct}
        return fdct


