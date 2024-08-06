from budget import Budget
from company import *
from departament import *
from employee import Employee
from finance import Finance
from project import *
from resource import Resource
from task import Task
from team import Team


def main():
    # Create some budget instances
    budget1 = Budget(5000)
    budget2 = Budget(2000)

    # Test Budget methods
    print("Initial budget1:", budget1.get_budget())
    budget1.add_funds(1500)
    print("After adding funds, budget1:", budget1.get_budget())
    budget1.deduct_funds(2000)
    print("After deducting funds, budget1:", budget1.get_budget())
    budget1.deduct_funds(5000)

    # Create some tasks
    task1 = Task("Task1", "Description1", "2024-09-01", "Employee1", "In Progress")
    task2 = Task("Task2", "Description2", "2024-10-01", "Employee2", "Completed")
    task3 = Task("Task3", "Description3", "2021-02-01", "Employee3", "Completed")
    task4 = Task("Task4", "Description4", "2020-02-01", "Employee4", "Completed")

    # Create a project
    project1 = Project("Project1", "Project1 Description", "2024-01-01", "2024-12-31", 10000, [task1, task2])
    project2 = Project("Project2", "Project4 Description", "2021-01-01", "2021-03-01", 30000, [task3])
    project3 = Project("Project3", "Project3 Description", "2020-01-01", "2020-03-01", 30000, [task4])

    # Test Project methods
    print("\nInitial project budget:", project1.track_budget())
    print("Project progress:", project1.track_progress())
    print("Project report:\n", project1.generate_status_report())

    # Create some resources
    resource1 = Resource("Resource1", "Type1", "Available", 300)
    resource2 = Resource("Resource2", "Type2", "Available", 150)

    # Create some employees
    employee1 = Employee("Employee1", 1, "Developer", "Team1", 5000)
    employee2 = Employee("Employee2", 2, "Tester", "Team1", 4500)

    # Create some teams
    team1 = Team("Team1", [employee1, employee2], [project1])

    # Create some departments
    departament1 = Departament("Department1", [team1], [project1])
    departament1.add_project(project2)
    departament1.add_project(project3)

    # Create a company
    company = Company("Company1", [departament1], [employee1, employee2], [resource1, resource2])

    # Test Company methods
    print("\nCompany status report:\n", company.generate_status_report())
    print("Company financial report:\n", company.generate_financial_report())

    # Create users
    admin_user = User("AdminUser", ["admin"])
    manager_user = User("ManagerUser", ["manager"])
    normal_user = User("NormalUser", ["user"])

    # Test adding/removing/updating employees
    print("\nAdding a new employee:")
    new_employee = Employee("Employee3", 3, "Manager", "Team2", 6000)
    company.add_employee(admin_user, new_employee)
    #company.add_employee(new_employee)
    print("Company employees after adding new employee:", [e.nume for e in company.lista_angajati])

    print("\nRemoving an employee:")
    company.remove_employee("Employee3")
    print("Company employees after removing employee:", [e.nume for e in company.lista_angajati])

    print("\nUpdating employee details:")
    company.update_employee(1, nume="UpdatedEmployee1", salariu=5500)

    # Test adding/removing/updating projects in a department
    print("\nAdding a new project to department:")
    new_project = Project("Project new", "New Project Description", "2024-03-01", "2024-11-30", 5000, [])
    departament1.add_project(new_project)
    print("Department projects after adding new project:", [p.nume for p in departament1.proiecte])

    print("\nRemoving a project from department:")
    departament1.remove_project("Project new")

    # Test adding/removing/updating teams
    print("\nAdding a new team to department:")
    new_team = Team("Team2", [], [])
    departament1.add_team(new_team)
    print("Department teams after adding new team:", [t.nume for t in departament1.lista_echipe])

    print("\nRemoving a team from department:")
    departament1.remove_team("Team2")
    print("Department teams after removing team:", [t.nume for t in departament1.lista_echipe])

    #
    # print("\nAllocating resource to task:")
    # project.allocate_resource("Task1", resource1)
    # print("Task details after allocating resource:",
    #       [(t.titlu, t.resource.nume if t.resource else None) for t in project.lista_sarcini])

    # Test allocating employees and resources
    print("\nAllocating employee to task:")
    task1.allocate_employee(employee2)  # Allocating Employee2 to Task1
    print("Task details after allocating employee:", task1.generate_status_report())

    # Check finished projects in the department
    print(
        f"\nFinished projects for departament {departament1.nume}: ",
        [project.nume for project in departament1.finished_projects()]
    )

    # Calculate total costs of resources for a company
    print(f"\nTotal resources for company {company.nume}: ", company.total_resource_cost())

    # List with title of tasks with upper case
    print(f"\nUpper case for title of tasks of project {project1.nume}: ",
          [task_titlu for task_titlu in project1.upper_case_titlu()])

    #List of employees from a certain Team
    print(f"List of employees from team {team1.nume} ",
          [x.nume for x in company.angajati_from_team("Team1")])

if __name__ == "__main__":
    main()
