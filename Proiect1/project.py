from budget import Budget
from task import Task
from datetime import datetime

class TaskNotFoundException(Exception):
    pass


class Project:
    def __init__(self, nume, descriere, data_inceput, data_sfarsit, budget, lista_sarcini):
        self.nume = nume
        self.descriere = descriere
        self.data_inceput = data_inceput
        self.data_sfarsit = data_sfarsit
        self.budget = Budget(budget)
        self.lista_sarcini = lista_sarcini

    def add_task(self, task):
        self.lista_sarcini.append(task)

    def remove_task(self, titlu):
        flag_task_found = False
        for task in self.lista_sarcini:
            if task.titlu == titlu:
                flag_task_found = True
                self.lista_sarcini.remove(task)
                break
        if not flag_task_found:
            raise TaskNotFoundException(f"Task {titlu} not found")

    def update_task(self, titlu, descriere=None, termen_limita=None, responsabil=None, status=None):
        flag_task_found = False
        for task in self.lista_sarcini:
            if task.titlu == titlu:
                flag_task_found = True
                if descriere is not None:
                    task.descriere = descriere
                if termen_limita is not None:
                    task.termen_limita = termen_limita
                if responsabil is not None:
                    task.responsabil = responsabil
                if status is not None:
                    task.status = status
                break
        if not flag_task_found:
            raise TaskNotFoundException(f"Task {titlu} not found")


    # def allocate_resource(self, titlu, resource):
    #     for task in self.lista_sarcini:
    #         if task.titlu == titlu:
    #             task.resource = resource
    #             return
    #     raise TaskNotFoundException(f"Task {titlu} not found")

    def track_progress(self):
        total_tasks = len(self.lista_sarcini)
        if total_tasks == 0:
            print(f"No tasks defined for project {self.nume}")
        completed_tasks = sum(task.status == "Completed" for task in self.lista_sarcini)
        progress = (completed_tasks / total_tasks) * 100
        return f"Project progress: {progress:.2f}%"

    def track_budget(self):
        return self.budget.get_budget()

    def generate_status_report(self):
        report = f"Project: {self.nume}\n"
        report += f"Progress: {self.track_progress()}\n"
        report += "Tasks:\n"
        for task in self.lista_sarcini:
            report += f"  Task: {task.titlu}, Status: {task.status}\n"
        return report

    # This function will return True if the project was finished (data_sfarsit < current time)
    def project_finished(self):
        # Get the current time
        current_time = datetime.now()
        date_object = datetime.strptime(self.data_sfarsit, "%Y-%m-%d")
        return date_object < current_time

    def upper_case_titlu(self):
        return list(map(lambda x: x.titlu.upper(), self.lista_sarcini))
