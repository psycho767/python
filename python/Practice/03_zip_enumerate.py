subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]

for index,(sub,mark) in enumerate(zip(subjects,marks),start=1):
    print(f"{index}. {sub} - {mark}")