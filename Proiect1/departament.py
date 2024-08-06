from project import Project
from budget import Budget



class TeamNotFoundException(Exception):
    pass


class ProjectNotFoundException(Exception):
    pass


class Departament:
    def __init__(self, nume, lista_echipe, proiecte):
        self.nume = nume
        self.lista_echipe = lista_echipe
        self.proiecte = proiecte

    def add_project(self, project):
        self.proiecte.append(project)

    def add_team(self, team):
        self.lista_echipe.append(team)

    def remove_team(self, team_name):
        flag_team_found = False
        for team in self.lista_echipe:
            if team.nume == team_name:
                flag_team_found = True
                self.lista_echipe.remove(team)
                break
        if not flag_team_found:
            raise TeamNotFoundException(f"Team {team_name} not found")

    def remove_project(self, project_name):
        flag_project_found = False
        for project in self.proiecte:
            if project.nume == project_name:
                flag_project_found = True
                self.proiecte.remove(project)
                break
        if not flag_project_found:
            raise ProjectNotFoundException(f"Project {project_name} not found")

    def update_project(self, project_name, descriere=None, data_inceput=None, data_sfarsit=None, budget=None, lista_sarcini=None):
        flag_project_found = False
        for project in self.proiecte:
            if project.nume == project_name:
                flag_project_found = True
                if descriere is not None:
                    project.descriere = descriere
                elif data_inceput is not None:
                    project.data_inceput = data_inceput
                elif data_sfarsit is not None:
                    project.data_sfarșsit = data_sfarsit
                elif budget is not None:
                    project.budget = Budget(budget)
                elif lista_sarcini is not None:
                    project.lista_sarcini = lista_sarcini
                else:
                    print(f"[update_project] No arguments given for {project_name}")
                break
        if not flag_project_found:
            raise ProjectNotFoundException(f"Project {project_name} not found")

    def update_team(self, team_name, lista_angajati=None, proiecte_alocate=None):
        flag_team_found = False
        for team in self.lista_echipe:
            if team.nume == team_name:
                flag_team_found = True
                if lista_angajati is not None:
                    team.lista_angajati = lista_angajati
                elif proiecte_alocate is not None:
                    team.proiecte_alocate = proiecte_alocate
                break
        if not flag_team_found:
            raise TeamNotFoundException(f"Team {team_name} not found")

    def generate_status_report(self):
        report = f"Departament: {self.nume}\n"
        for project in self.proiecte:
            report += project.generate_status_report() + "\n"
        return report

    def calculate_total_budget(self):
        return sum(project.budget.get_budget() for project in self.proiecte)

    def calculate_total_expenses(self):
        return sum(project.budget.expenses for project in self.proiecte)

    # Filter project which has data_sfarsit < current time (finished projects)
    def finished_projects(self):
        # Use the filter function to filter finished projects
        return list(filter(lambda project: project.project_finished(), self.proiecte))
