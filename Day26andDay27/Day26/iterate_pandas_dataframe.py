import pandas

student_dict = {
    "student": ["Manas", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (item, row) in student_data_frame.iterrows():
    print(row.student)