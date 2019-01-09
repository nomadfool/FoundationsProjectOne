####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Cuphead" #complete me!
signature_flavors = ["crazy train", "paranoid", "7734", "jawbreaker", "motorhead", "powerslave"]# complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("-------- Our Menu --------\n")
    for key in menu:
        print("- %s  (%s KD)" % (key, menu[key]))
    print()


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for i in original_flavors:
        print("- %s" % (i))
    print()


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for i in signature_flavors:
        print("- %s" % (i))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order.lower() in menu:
        return True
    elif order.lower() in original_flavors:
        return True
    elif order.lower() in signature_flavors:
        return True
    else:
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    cart = input("What are you having today? (Spelling is important! Type 'Exit' when your done.)\n")
    while cart != "Exit":
        if is_valid_order(cart) is True:
            order_list.append(cart)

        else:
            print("I'm sorry, that's not on the menu.")

        cart = input()
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return "This order is eligible for payment by credit card."
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for i in order_list:
        if i in menu:
            total += menu[i]
        elif i in original_flavors:
            total += original_price
        else:
            total += signature_price
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for i in order_list:
        print("- %s" % (i))
    print()
    print("That'll be %s KD" % (get_total_price(order_list)))
    if accept_credit_card(get_total_price(order_list)) != False:
        print(accept_credit_card(get_total_price(order_list)))
    print("thank you for shopping at %s. Please come again." % (cupcake_shop_name))