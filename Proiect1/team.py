from employee import Employee
from project import Project
from budget import Budget

class ProjectNotFoundException(Exception):
    pass

class EmployeeNotFoundException(Exception):
    pass

class EmployeeNotPartFromThisTeamException(Exception):
    pass

class Team:
    def __init__(self, nume, lista_angajati, proiecte_alocate):
        self.nume = nume
        self.lista_angajati = lista_angajati
        self.proiecte_alocate = proiecte_alocate

    def add_employee(self, employee):
        if employee.echipa == self.nume:
            self.lista_angajati.append(employee)
        else:
            raise EmployeeNotPartFromThisTeamException(f"Employee {id} not part from team {self.nume}")

    def add_project(self, project):
        self.proiecte_alocate.append(project)

    def remove_employee(self, id):
        flag_employee_found = False
        for employee in self.lista_angajati:
            if employee.id == id:
                flag_employee_found = True
                self.lista_angajati.remove(employee)
                break
        if not flag_employee_found:
            raise EmployeeNotFoundException(f"Employee {id} not found")

    def remove_project(self, project_name):
        flag_project_found = False
        for project in self.proiecte_alocate:
            if project.nume == project_name:
                flag_project_found = True
                self.proiecte_alocate.remove(project)
                break
        if not flag_project_found:
            raise ProjectNotFoundException(f"Project {project_name} not found")

    def update_employee(self, id, nume=None, rol=None, echipa=None, salariu=None):
        flag_employee_found = False
        for employee in self.lista_angajati:
            if employee.id == id:
                flag_employee_found = True
                if nume is not None:
                    employee.nume = nume
                elif rol is not None:
                    employee.rol = rol
                elif echipa is not None:
                    employee.echipa = echipa
                elif salariu is not None:
                    employee.salariu = salariu
                break
        if not flag_employee_found:
            raise EmployeeNotFoundException(f"Employee {id} not found")

    def update_project(self, project_name, descriere=None, data_inceput=None, data_sfarsit=None, budget=None, lista_sarcini=None):
        flag_project_found = False
        for project in self.proiecte_alocate:
            if project.nume == project_name:
                flag_project_found = True
                if descriere is not None:
                    project.descriere = descriere
                elif data_inceput is not None:
                    project.data_inceput = data_inceput
                elif data_sfarsit is not None:
                    project.data_sfarsit = data_sfarsit
                elif budget is not None:
                    project.budget = Budget(budget)
                elif lista_sarcini is not None:
                    project.lista_sarcini = lista_sarcini
                else:
                    print(f"[update_project] No arguments given for {project_name}")
                break
        if not flag_project_found:
            raise ProjectNotFoundException(f"Project {project_name} not found")