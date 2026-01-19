# Creating check list at the start of the day

checkList: list = []

number_of_task: int = int(input("Enter how many tasks you want to add?: "))

for i in range(number_of_task):
    task: str = input(f"Enter the task {i+1}: ")
    checkList.append(task)
    print(checkList)

print("\n----My Check List----")
for task in checkList:
    print("->", task)

# Review tasks at the end of the day
completed_task: list = []
incompleted_task: list = []

print("\n----Review at the end of the day----")
for task in checkList:
    status: str = input(f"Did you completed the task '{task}'? (yes/no): ").lower()

    if status == "yes":
        completed_task.append(task)
    else:
        incompleted_task.append(task)

# ----Result Time----
print("\n\n----Completed Tasks----")
for task in completed_task:
    print("->", task)

print("\n----Incompleted Tasks----")
for task in incompleted_task:
    print("->", task)