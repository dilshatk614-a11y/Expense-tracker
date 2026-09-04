import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tab"
)
print("Database connected successfully")
cursor=db.cursor()
cart=[]
while True:
    print("\n=========EXPENSE TRACKER=======")
    print("1.Add Expense")
    print("2.Add category")
    print("3.View all expenses")
    print("4.View Monthly Total")
    print("5.View Spending by category")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Add expense:",)
    elif choice==2:
        print("Add category:",category)
    elif choice==3:
        print("View all expenses:",amount_spend)
    elif choice==4:
        print("View monthly total")
    elif choice==5:
        print("View Spending by category")
    elif choice==6:
        print("Exit")        
        break
    else:
        print("Invalid choice")
