#Our Menu
menu={
    'Pizza':100,
    'Pasta':90,
    'Burger':60,
    'Coffee':70,
    'Salad':50
}

#for handling uppercase and lowercase ambiguity
lowercase_menu={item.lower():price for item,price in menu.items()}

def menu_display(menu):
    print("Menu:")
    for item,price in menu.items():
        print(f"{item}: Rs{price}")

#method to keep orderdetails and calculate total amount
def take_order(lowercase_menu):
    total_order_amount=0
    order_details={}

    while True:
        item=input("Enter the name of the item you want to order: ").strip().lower()
        if item in lowercase_menu:
            quantity=int(input(f"How many {item.title()}s would you like to order: "))
            order_details[item]=order_details.get(item,0)+quantity
            total_order_amount+=lowercase_menu[item]*quantity
            print(f"{quantity} {item.title()}s have been added to your order. ")
        else:
            print(f"Ordered item {item.title()} is not available yet. ")

        another_order=input("Do you want to add another item? (Yes,No): ").strip().lower()
        if another_order!="yes":
            break
    return total_order_amount,order_details

#Applying 10% discount whenever our total_order_discount exceeds 200.
def apply_discount(total_order_amount):
    discount_threshold=200
    discount_rate=0.1 
    if total_order_amount>discount_threshold:
        discount=total_order_amount*discount_rate
        total_order_amount-=discount
        print(f"A discount of Rs{discount:.2f} has been applied")
    return total_order_amount

#Summery of Orders which is to display to the user.
def order_summery(total_order_amount,order_details):
    print("\nOrder Summery: ")
    for item,quantity in order_details.items():
        print(f"{item.title()}:{quantity} X Rs{lowercase_menu[item]} = Rs{lowercase_menu[item]*quantity}")
    print(f"Total Amount: Rs{total_order_amount} ")

#Getting Feedback from the user.
def get_feedback():
    feedback=input("Please Provide your Feedback about our services: ")
    print("Thank You For Your Feedback. ")

#Main Method
def main():
    print("Welcome to Pyhton Restaurant! ")
    menu_display(menu)
    while True:
        total_order_amount,order_details=take_order(lowercase_menu)
        total_order_amount=apply_discount(total_order_amount)

        order_summery(total_order_amount,order_details)

        get_feedback()

        new_customer=input("Is there another customer? (Yes/No): ").strip().lower()
        if new_customer!="yes":
            print("Thank You For Visiting Python Restaurant. Have a Great Day!")
            break
    
if __name__=="__main__":
    main()




