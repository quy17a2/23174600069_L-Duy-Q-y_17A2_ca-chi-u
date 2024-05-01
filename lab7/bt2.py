# Nhập thông tin của 10 sinh viên
students = {}
for i in range(1, 11):
    name = input(f"Nhập tên của sinh viên thứ {i}: ")
    score = float(input(f"Nhập điểm thi của sinh viên thứ {i}: "))
    students[name] = score

# Xếp loại học lực và thống kê số lượng sinh viên ở mỗi loại học lực
grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for student, score in students.items():
    if score >= 8.5:
        grade_count['A'] += 1
    elif score >= 7.0:
        grade_count['B'] += 1
    elif score >= 5.5:
        grade_count['C'] += 1
    elif score >= 4.0:
        grade_count['D'] += 1
    else:
        grade_count['F'] += 1

# In xếp loại học lực của từng sinh viên và thống kê số lượng sinh viên ở mỗi loại học lực
print("\nXếp loại học lực của từng sinh viên:")
for student, score in students.items():
    if score >= 8.5:
        grade = 'A'
    elif score >= 7.0:
        grade = 'B'
    elif score >= 5.5:
        grade = 'C'
    elif score >= 4.0:
        grade = 'D'
    else:
        grade = 'F'
    print(f"{student}: {grade}")

print("\nThống kê số lượng sinh viên ở mỗi loại học lực:")
for grade, count in grade_count.items():
    print(f"{grade}: {count}")
