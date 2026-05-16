print("welcome to the Tip calculator🧮")
print("lets calculate tip 😊")
tot_bill=float(input("what was the total bill$:"))
tip_percent=float(input("enter the percentage of tip you would like to give like 10,12,20:"))
no_of_people=int(input("enter how many members to be split the bill:"))
tip_percent=tip_percent/100
tot_tip=tot_bill*tip_percent
bill_with_tip=tot_bill+tot_tip
tip_for_each_person=tot_tip/no_of_people
print("The total bill is:",round(tot_bill,2),"$")
print("Total tip got is:",round(tot_tip,2),"$")
print("The tip for each person is:",round(tip_for_each_person,2),"$")
print("The total bill with tip is:",round(bill_with_tip,2),"$")
print("Thank you for using this calculator🤗")
