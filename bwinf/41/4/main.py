methode = 1

task = "fahrradwerkstatt0.txt"
active_tasks = []

timer = 0

task = open(task).read().splitlines()
for i in range(len(task)):
    task[i] = task[i].split()


def methode1():
    


def methode2():
    pass


def methode3():
    pass


if (methode == 1):
    methode1()
elif (methode == 2):
    methode2()
elif (methode == 3):
    methode3()