num_tasks = int(input("Enter number of tasks: "))
tasks = {}

for i in range(num_tasks):
    task_name = input("Enter task name: ")
    num_deps = int(input(f"How many dependencies for {task_name}? "))

    dependencies = []
    for j in range(num_deps):
        dep_name = input(f"Enter dependency {j + 1}: ")
        dependencies.append(dep_name)

    tasks[task_name] = dependencies

print("\nTASK STRUCTURE:")
for task, deps in tasks.items():
    print(f"{task} -> {deps}")

print("\nINITIAL TASKS (no dependencies):")
initial_tasks = [t for t, d in tasks.items() if len(d) == 0]
if not initial_tasks:
    print("None")
else:
    for t in initial_tasks:
        print(t)

execution_order = []
completed_tasks = set()
all_tasks = list(tasks.keys())

while len(completed_tasks) < len(all_tasks):
    task_started_in_this_step = False

    for task in all_tasks:
        if task not in completed_tasks:
            is_ready = True
            for dep in tasks[task]:
                if dep not in completed_tasks:
                    is_ready = False
                    break

            if is_ready:
                completed_tasks.add(task)
                execution_order.append(task)
                task_started_in_this_step = True
                print(f"Step {len(execution_order)}: {task}")

    if not task_started_in_this_step:
        print("\nNo task can be started.")
        print("ERROR: Circular dependency detected!")
        print("These tasks could not be completed:")
        for task in all_tasks:
            if task not in completed_tasks:
                print(task)
        break
else:
    print("\nALL TASKS COMPLETED SUCCESSFULLY")