import csv
expenses=[]

while True:
  op = int(input("1. add an expense + saves it in csv\n 2.View an expense\n 3.Calculate expenses\n 4.delete an item\n 5.exit\n"))

  if op==1:
    item = input("name of the purchase: ").lower()
    category = input("food\n travel\n study\n other\n :").lower()
    amt = int(input("cost: "))

    expense={
    "item":item,
    "category": category,
    "amount": amt
    }
    expenses.append(expense)

    with open("expenses.csv", "a", newline="") as file:
      writer = csv.writer(file)
      writer.writerow([ expense["item"], expense["category"], expense["amount"] ])
    print("Expenses saved")

  elif op==2:
    expenses.clear()
    with open("expenses.csv", "r") as file:
      reader = csv.reader(file)
      for row in reader:
          expense = {
                "item": row[0],
                "category": row[1],
                "amount": int(row[2])
            }
          expenses.append(expense)
      for expense in expenses:
        print(expense)

  elif op==3:
    t_food=0
    t_travel=0
    t_study=0
    t_other=0
    total=0
    for expense in expenses:
      if expense["category"]=="food":
        t_food+=expense["amount"]
      elif expense["category"]=="travel":
        t_travel+=expense["amount"]
      elif expense["category"]=="study":
        t_study+=expense["amount"]
      elif expense["category"]=="other":
        t_other+=expense["amount"]
      total+=expense["amount"]
    print("food :", t_food)
    print("travel :", t_travel)
    print("study :", t_study)
    print("other :", t_other)
    print("aggregative :", total)
    max_expense_amount=0
    min_expense_amount=0
    if expenses:
        max_expense_amount = expenses[0]["amount"]
        min_expense_amount = expenses[0]["amount"]
        for expense in expenses:
            if expense["amount"] > max_expense_amount:
                max_expense_amount = expense["amount"]
            if expense["amount"] < min_expense_amount:
                min_expense_amount = expense["amount"]
        print("highest cost :", max_expense_amount)
        print("lowest cost :", min_expense_amount)
    else:
        print("No expenses to calculate max/min.")

  elif op == 4:
    rows=[]
    with open("expenses.csv", "r") as file:
      reader=csv.reader(file)
      for row in reader:
        rows.append(row)
    for i, row in enumerate(rows):
      print(i+1, row)

    ch=int(input("enter the expense number to delete: "))
    if 1<=ch<=len(rows):
        del rows[ch-1]
        with open("expenses.csv", "w", newline="")as file:
          writer=csv.writer(file)
          writer.writerows(rows)
        print("Expense deleted successfully.")
    else:
        print("Invalid expense number.")

  elif op ==5:
    print("exiting")
    break

  else:
    print("invalid input")
