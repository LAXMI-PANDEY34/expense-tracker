expenses = []
print("Welcome To Expense Tracker")
while True:
    print("\n========MENU=========")
    print("1. Add Expense")
    print("2. View All  Expenses")
    print("3. View Total  Spending")
    print("4. View Spending By  Category")
    print("5.  Exit")
    print("==========================")
    choice = input("Enter Your choice (1-5):")
    if choice == "1":
        date = input("Enter Date : (DD-MM-YYYY):")
        category = input("Enter Catogory(Food ,  Travel, Shopping etc)")
        description = input("Enter shor description:")
        amount  = float(input("Enter Amount (₹):")) 
        expense ={
            "date" :  date,
            "category" : category,
            "description": description,
            "amount" : amount
        
        }
        expenses.append(expense)
        print("\n Expense Added Successfully!")
        #view All  expense
    elif choice == "2":
        if len(expenses) == 0:
            print("\n No  Expenses Record")
        else:
            print("\n All Expenses")
        i =1
        for  e  in expenses:
           print(f" \n{i}. {e['date']} | {e['category']} | {e ['description']} | {e['amount']} " )
        
           i +=1
           print("------------------------")
              #view Total Spending
    elif choice =="3":
        total  = 0
        for  e in expenses:
              total += e["amount"]   
              print(f"\n total Spending = {total}")
              #Spending by category
    elif choice =="4" :
        if len(expenses) ==0:
            print("\n No Expenses")
        else:
            summary = {}
            for e in  expenses:
               cat = e["category"]
               if cat  in  summary:
                summary[cat] += e["amount"]

               else:
                 summary[cat] = e["amount"]
        print("\n spending  by category:")
        for cat, amt in summary.items():
          print(f"{cat} : {amt}")
              #exit
    elif choice == "5":
        print("Thank you for using expense tracker -- Bye Bye!")
        break

    else:
        print("Invalid Choice. Please Try Again.")

    