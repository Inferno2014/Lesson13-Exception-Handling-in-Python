valid = False
while not valid:
    try:
        bill = int(input("Bill amount: "))
        discount = int(input("Discount percent: "))
        discount_amount = bill * discount / 100
        final_bill = bill - discount_amount
    except ValueError:
        print("Please type numbers only.")
    else:
        print("Final bill:", final_bill)
        print("Payment amount:", final_bill)
        a = input('Do you want to cancel your order? Yes/No: ').lower()
        if a == 'no':
            print("Payment finished. Thank you for your patience.")
            valid = True
        elif a == 'yes':
            print('Thank you for your time! Shop again Later!')
            valid = True
        