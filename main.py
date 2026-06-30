#This function is for saving the amount and category to the expenses.txt file
def save_expense(category,amount):
    file=open("expenses.txt","a")
    file.write(category + "-" + str(amount) + "\n")
    file.close()


#This fucntion is used to load the expense   
def load_expenses():
    total=0
    expenses=[]
    file = open("expenses.txt", "r")

    for line in file:
        line = line.strip()
        
        if line=="":
            continue
        if "-" not in line:
            continue

        category,amount=line.rsplit("-",1)
        
        category=category.strip()
        amount=amount.strip()

        try:
            amount=int(amount)
        except ValueError:
            continue

        expense={
            "category":category,
            "amount":amount
        }
        expenses.append(expense)
        total=total+amount
    file.close()
    return expenses,total

expenses,total=load_expenses()


#This function is for choice 1
def add_expense(expenses,total):
    while True:
            try:
                amount=int(input("Enter expense:"))
                break
            except ValueError:
                print("Invalid amount.Please enter a number.")
                

    while True:
            category=input("Enter the category:").strip()
            
            if category!="":
                    break
            print("Category cannot be empty.")

    expense={
            "amount": amount,
            "category":category
        }
    expenses.append(expense)
    total=total+amount

    save_expense(category,amount)

    print("Expense added")
    return expenses,total


#This is for choice 2
def view_expenses(expenses):
    print("Expenses:")

    for expense in expenses:
        print(expense["category"] ,"-" ,expense["amount"])



#This is for choice 3
def view_total(total):
    print("Total expense:",total)



#This is for choice 4
def view_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount

    for category in category_totals:
            print(category, "-", category_totals[category])



while True:

    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total")
    print("4. View category wise total")
    print("5. Exit")

    choice = input("choose an option:")

    if choice =="1":
        expenses,total= add_expense(expenses,total)
        
    

    elif choice=="2":
        view_expenses (expenses)
        
    
    elif choice=="3":
        view_total(total)
        
    elif choice == "4":
       view_category_totals(expenses)


    elif choice=="5":
        print("exiting program")
        break
    else:
        print ("Error")
        

