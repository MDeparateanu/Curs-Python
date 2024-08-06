class Finance:
    def __init__(self, incomes, expenses):
        self.incomes = incomes
        self.expenses = expenses

    def add_income(self, sum):
        self.incomes += sum

    def add_expense(self, sum):
        self.expenses += sum

    def get_balance(self):
        return self.incomes - self.expenses
