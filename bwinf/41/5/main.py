class Node:
    def __init__(self, number):
        self.connections = []
        self.id = number
        self.steps_s = []
        self.steps_m = []
        self.min_step = 0
        self.max_steps = int(n)

    def __str__(self):
        return f"{self.id} {self.connections}"

    def add_connection(self, connection):
        self.connections.append(connection)
        return self

    def next_connection_s(self, step_id):
        if step_id > self.max_steps:
            return

        if step_id in self.steps_s:
            return

        self.steps_s.append(step_id)

        for target_id in self.connections:
            nodes[target_id - 1].next_connection_s(step_id + 1)

    def next_connection_m(self, step_id):
        if step_id > self.max_steps:
            return

        if step_id in self.steps_m:
            return

        self.steps_m.append(step_id)

        for target_id in self.connections:
            nodes[target_id - 1].next_connection_m(step_id + 1)

    def get_intersection(self):
        return list(set(self.steps_m) & set(self.steps_s))


# opens file
taskfile = "huepfburg0.txt"
task = open(taskfile).read().splitlines()

# splits the file and cast to int
n, m = task.pop(0).split()
connections = [list(map(int, connection.split())) for connection in task]

# creates nodes
nodes = []
for node_id in range(int(n)):
    nodes.append(Node(node_id + 1))

# adds all the connections to the nodes
for source_id, target_id in connections:
    nodes[source_id - 1].add_connection(target_id)

# ----------------------------------------------------------------

# sascha
current_node = 1
step_id = 0
nodes[current_node - 1].next_connection_s(step_id)

# mika
current_node = 2
step_id = 0
nodes[current_node - 1].next_connection_m(step_id)

# ----------------------------------------------------------------

sascha = [sorted(node.steps_s) for node in nodes]
mika = [sorted(node.steps_m) for node in nodes]

for node in nodes:
    print(nodes.index(node) + 1, min(node.get_intersection()))
