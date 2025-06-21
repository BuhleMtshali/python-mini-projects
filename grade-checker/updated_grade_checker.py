grade_list = [("zamo", "chemistry", 78), ("luke", "math lit", 45), ("linda", "information systems", 67), ("busi", "networks", 88)];

#looping through a nested array

for name, subject, grade in grade_list:
    print(f"{name.title()}, you got {grade}% in your {subject.title()} test");