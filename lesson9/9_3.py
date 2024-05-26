# Даны два YAML файла (будут приложены в группе телеграмм) builds.yaml и tasks.yaml.
# В файле builds находится список “Билдов” и перечень задач для выполнение данного билда
# В файле tasks находится список задач и подзадач каждой задачи.
# По название Билда, необходимо вывести список задач и подзадач для
# выполнения билда (задачу нельзя выполнить до выполнения подзадач).

from yaml import safe_load

with open("builds.yaml", "r") as file:
    builds_file = safe_load(file)
with open("tasks.yaml", "r") as file:
    tasks_file = safe_load(file)

build_name = 'forward_interest'
list_of_tasks = []


def get_tasks(builds_file: dict) -> list:
    for build in builds_file.get('builds'):
        if build.get('name') == build_name:
            return build.get('tasks')


def extend_list_of_tasks(list_of_tasks: list, tasks_file: dict) -> list:
    task_number = 0
    while task_number < len(list_of_tasks):
        for task_name in tasks_file.get('tasks'):
            if task_name.get('name') == list_of_tasks[task_number]:
                list_of_tasks += task_name.get('dependencies')
        task_number += 1
    return list_of_tasks


list_of_tasks = get_tasks(builds_file)
print(list_of_tasks)
list_of_tasks = extend_list_of_tasks(list_of_tasks, tasks_file)
print(list_of_tasks)
print(f"number of tasks for {build_name} is {len(list_of_tasks)}")
