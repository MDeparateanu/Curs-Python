from employee import Employee

class TaskNotFoundException(Exception):
    pass

class Task:
    def __init__(self, titlu, descriere, termen_limita, responsabil, status):
        self.titlu = titlu
        self.descriere = descriere
        self.termen_limita = termen_limita
        self.responsabil = responsabil
        self.status = status

    def allocate_employee(self, employee):
        self.responsabil = employee

    def generate_status_report(self):
        report = f"Task: {self.titlu}\n"
        report += f"Description: {self.descriere}\n"
        report += f"Deadline: {self.termen_limita}\n"
        report += f"Responsible: {self.responsabil.nume}\n"
        report += f"Status: {self.status}\n"
        return report

