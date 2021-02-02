class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.finished = False

    def mark_task_as_finished(self):
        self.finished = True