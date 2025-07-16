funds =  2500
budgets = {}
expenses = {}

def AddBudget(name, amount):
    global funds
    if name in budgets:
        raise ValueError("Budget for item already exists")
    if amount  > funds:
        raise ValueError("No can do, you are too broke")
    budgets[name] = amount
    funds -= amount
    expenses[name] = 0
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("item not in budget")
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent
    
def PrintBudget():
    print("Budget      Spent      Reamining")
    print("---------------------------------")
    totalBudgeted = 0
    totalSpent = 0
    totalReamining = 0
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent: 10.2f} ' 
              f' {remainingBudget:10.2f}')
        totalBudgeted += budgeted
        totalSpent += spent
        totalReamining = remainingBudget
        print(f'{"Total":15s}, {budgeted:10.2f}, {spent: 10.2f} ' 
              f' {remainingBudget:10.2f}')



print("Total Funds: ", funds)
AddBudget("books", 100)
AddBudget("rent", 800)
AddBudget("Car note",200)

Spend("books",50)
Spend("rent",800)
Spend("Car note", 200)

PrintBudget()