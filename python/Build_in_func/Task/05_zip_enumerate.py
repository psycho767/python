names = ["Rahul", "Aman", "Riya"]
marks = [80, 90, 95]

# list_of_tupples = []

# for names, marks in zip(names,marks):
#     list_of_tupples.append((names,marks))
#     print(f"Name-{names},Marks-{marks}")

# print(list_of_tupples)
# for index,values in enumerate(list_of_tupples):
#     print(f"{index},{values}")

for index,(name,mark) in enumerate(zip(names,marks),start=1):
    print(f"{index} {name} {mark}")

 