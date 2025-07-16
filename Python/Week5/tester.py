import budget
myBudget = budget.BudgetManager(2500)
print("Total Funds: ", myBudget.funds)
myBudget.AddBudget("books", 100)
myBudget.AddBudget("rent", 800)
myBudget.AddBudget("Car note",200)

myBudget.Spend("books",50)
myBudget.Spend("rent",800)
myBudget.Spend("Car note", 200)

myBudget.PrintBudget()