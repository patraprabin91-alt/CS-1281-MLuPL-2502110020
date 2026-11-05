IT12
class Machine:
    def __init__(self, name, model, limit):
        self.name = name
        self.model = model
        self.limit = limit
        self.running = False

    def __str__(self):
        return f"{self.name} - {self.model} (Limit: {self.limit})"

    def start(self):
        self.running = True
        return f"{self.name} started"


# Commission two machines
machine1 = Machine("Lathe", "L100", 500)
machine2 = Machine("Drill", "D200", 300)

# Print both nameplates
print(machine1)
print(machine2)

# Start only machine1
print(machine1.start())

# Prove states are independent
print("Machine 1 running:", machine1.running)
print("Machine 2 running:", machine2.running)

IT10
class Machine:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.__speed = 0

    def operate(self, speed):
        if speed < 0 or speed > self.limit:
            return f"Rejected: speed must be between 0 and {self.limit}"
        self.__speed = speed
        return f"{self.name} running at {speed}"

    def status(self):
        return self.__speed


machine = Machine("Lathe", 100)

print(machine.operate(60))
print(machine.status())

print(machine.operate(150))
print(machine.status())

IT08
class Machine:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.__speed = 0
        self.__jobs = 0
        self.__rejected = 0

    def operate(self, speed):
        if speed < 0 or speed > self.limit:
            self.__rejected += 1
            return "Rejected"
        self.__speed = speed
        self.__jobs += 1
        return "Accepted"

    def status(self):
        return {
            "machine": self.name,
            "jobs": self.__jobs,
            "rejected": self.__rejected,
            "last_speed": self.__speed
        }


machine = Machine("Lathe", 100)

logs = [
    "J01,50", "J02,80", "J03,120", "J04,60", "J05,90",
    "J06,110", "J07,40", "J08,70", "J09,130", "J10,55"
]

for line in logs:
    code, speed = line.split(",")
    result = machine.operate(int(speed))
    print(code, result)

print("\nShift Report:")
print(machine.status())

IT06
class Machine:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.parts = 0
        self.busy = False

    def process(self, speed):
        if speed <= self.limit:
            self.parts += 1
            self.busy = True
            return True
        return False


machines = [
    Machine("Lathe", 100),
    Machine("Drill", 80),
    Machine("Mill", 120)
]

jobs = [50, 70, 90, 60, 110, 40, 100, 75, 115, 55]

for speed in jobs:
    machine = next((m for m in machines if not m.busy), None)

    if machine:
        machine.process(speed)

    for m in machines:
        m.busy = False

busiest = max(machines, key=lambda m: m.parts)

print("Plant Report")
for m in machines:
    print(m.name, ":", m.parts, "parts")

print("Plant total:", sum(m.parts for m in machines))
print("Busiest machine:", busiest.name)
