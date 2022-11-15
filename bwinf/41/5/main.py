# create the Klass Knoten
class Knoten:
    def __init__(self, number):
        self.connections = []
        self.number = number

    def __str__(self):
        return f"{self.number} {self.connections}"

    def getConnections(self):
        return self.connections

    def getNumber(self):
        return self.number

    def addConnection(self, connection):
        self.connections.append(connection)
        return self

# opens fiele
taskfile = "huepfburg0.txt"
task = open(taskfile).read().splitlines()

# splits the file
n, m = task.pop(0).split()
task = [task[i].split() for i in range(len(task))]

# maps everything to int
temp_task = []
for i in range(len(task)):
    temp_task.append(list(map(int, task[i])))
task = temp_task

# creates knoten
knoten = []
for i in range(int(n)):
    knoten.append(Knoten(i + 1))

# adds all the connections to the knotens
for t in task:
    k = knoten[t[0] - 1].addConnection(t[1])
