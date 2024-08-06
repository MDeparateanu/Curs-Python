class Budget:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = 0

    def add_funds(self, sum):
        self.budget += sum

    def deduct_funds(self, sum):
        if sum <= self.budget:
            self.budget -= sum
            self.expenses += sum
        else:
            print("Insuficient funds\n")

    def get_budget(self):
        return self.budget
