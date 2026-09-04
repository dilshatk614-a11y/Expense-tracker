import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tab"
)
print("Database connected successfully")
cursor=db.cursor()
while True:
    print("\n=====EXPENSE TRACKER======")
    print("1.Add Expense")
    print("2.Add category")
    print("3.View all expenses")
    print("4.View Monthly Total")
    print("5.View Spending by category")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        amount=float(input("Enter amount spent:"))
        date=input("Enter date(YYYY-MM-DD):")
        category=int(input("Enter category ID:"))
        payment_method=input("Enter payment method:")
        query="""
        INSERT INTO second(amount_spent,datee,category,payment_method)VALUES(%s,%s,%s,%s)
        """
        values=(amount,date,category,payment_method)
        cursor.execute(query,values)
        db.commit()
        print("Expense added successfully!")
    elif choice==2:
        category=input("Enter category:")
        query="INSERT INTO first(category)VALUES(%s)"
        cursor.execute(query,(category,))
        db.commit()
        print("Category added successfully!")
    elif choice==3:
        query="""
        SELECT second.id,second.amount_spent,second.datee,first.category,second.payment_method FROM second JOIN first ON second.category=first.id
        """
        cursor.execute(query)
        expenses=cursor.fetchall()
        print("\n====ALL EXPENSES====")
        if len(expenses)==0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(
                "ID:",expense[0],
                "|Amount:",expense[1],
                "|Date:",expense[2],
                "|Category:",expense[3],
                "|Payment:",expense[4]

               )
    elif choice==4:
        month=int(input("Enter month(1-12):"))
        year=int(input("Enter year:"))
        query="""
        SELECT SUM(amount_spent)FROM second WHERE MONTH(datee)=%s AND YEAR(datee)=%s
        """
        cursor.execute(query,(month,year))
        result=cursor.fetchone()
        if result[0] is None:
           print("No expenses found for this month.")
        else:
           print("Total spending:",result[0])
    elif choice==5:
        query="""
        SELECT first.category,SUM(second.amount_spent)
        FROM second 
        JOIN first 
        ON second.category=first.id 
        GROUP BY first.category
        """
        cursor.execute(query)
        results=cursor.fetchall()
        print("\n====SPENDING BY CATEGORY====")
        if len(results)==0:
            print("No expense found.")
        else:
            for result in results:
                print(
                    "Category:",result[0],
                    "|Total:",result[1]
                )    

    elif choice==6:
        print("Thankyou for using Expense Tracker!")
        break
    else:
          print("Invalid choice.Please try again.")
cursor.close()
db.close()
