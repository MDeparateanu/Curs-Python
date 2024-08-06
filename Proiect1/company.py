from departament import Departament
from employee import Employee
from functools import reduce
import functools
import time

class EmployeeNotFoundException(Exception):
    pass

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions


def log_function_call(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Calling function '{func.__name__}' with arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper


def check_permissions(func):
    def wrapper(user, *args, **kwargs):
        # Check if the user has all required permissions
        if user.permissions != 'root':
            raise PermissionError(f"User '{user.name}' does not have the required permissions")
        return func(user, *args, **kwargs)
    return wrapper


class Company:
    def __init__(self, nume, lista_departamente, lista_angajati, lista_resurse):
        self.nume = nume
        self.lista_departamente = lista_departamente
        self.lista_angajati = lista_angajati
        self.lista_resurse = lista_resurse

    #@check_permissions
    def add_employee(self, user, employee):
        self.lista_angajati.append(employee)

    @log_function_call
    def remove_employee(self, employee_name):
        flag_employee_found = False
        for employee in self.lista_angajati:
            if employee.nume == employee_name:
                flag_employee_found = True
                self.lista_angajati.remove(employee)
                break
        if not flag_employee_found:
            raise EmployeeNotFoundException(f"Employee {employee_name} not found")

    @log_function_call
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

    def generate_status_report(self):
        report = f"Company: {self.nume}\n"
        for departament in self.lista_departamente:
            report += departament.generate_status_report() + "\n"
        return report

    def generate_financial_report(self):
        total_budget = 0
        total_expenses = 0

        for departament in self.lista_departamente:
            total_budget += departament.calculate_total_budget()
            total_expenses += departament.calculate_total_expenses()

        report = f"Company: {self.nume}\n"
        report += f"Total Budget: {total_budget}\n"
        report += f"Total Expenses: {total_expenses}\n"
        report += f"Balance: {total_budget - total_expenses}\n"
        return report

    def total_resource_cost(self):
        return reduce(lambda total, resource: total + resource.cost, self.lista_resurse, 0)

    def angajati_from_team(self, team_name):
        return list(filter(lambda angajat: angajat.echipa == team_name, self.lista_angajati))