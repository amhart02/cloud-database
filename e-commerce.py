#Connecting Database with python file
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("e-commerce.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#making initial user choice variable
user_choice = 1 

while user_choice != 6:
    #display the menu
    print("Please choose an option: ")
    print("1. View available produce products for purchase")
    print("2. Add a product to your cart")
    print("3. Remove a product from your cart")
    print("4. Update a quantity in your cart")
    print("5. Display items in your cart")
    print("6. Quit")

    #get user input
    print()
    user_choice = int(input("Enter a number 1-6: "))
    print()

    #choice 1 display products
    if user_choice == 1:
        products = db.collection("products").get()
        list_number = 0
        #iterate through each product in the list
        for product in products:
            data = product.to_dict()
            list_number += 1
            print(f'{list_number}- {data["name"]} : ${data["price"]:.2f}')
        print()

    #choice 2 add product to cart and quantity
    elif user_choice == 2:
        products = db.collection("products").get()
        list_number = 0
        product_ids = []
        #iterate through each product in the list
        for product in products:
            data = product.to_dict()
            list_number += 1
            print(f'{list_number}- {data["name"]} : ${data["price"]:.2f}')
            product_ids.append(product.id)
        #ask for user input
        print()
        product_to_add = int(input("Please enter the list number of the product you would like to add: "))
        quantity_to_add = int(input("Please enter the quantity of the product to add to your cart: "))
        print()
        print("Item added to cart!")
        print()
        #add selected product to the cart 
        selected_product_id = product_ids[product_to_add - 1]
        selected_product = db.collection("products").document(selected_product_id).get()
        data = selected_product.to_dict()
        db.collection("cart").add({"name" : data["name"] , "price" : data["price"] , "quantity" : quantity_to_add})

    #remove product from cart
    elif user_choice == 3:
        cart_products = db.collection("cart").get()
        list_number = 0
        total_price = 0
        product_ids = []
        #display cart if it is not empty
        if not cart_products:
            print("The cart is empty!")
        else:
            for product in cart_products:
                data = product.to_dict()
                list_number += 1
                total_price += (data["price"] * data["quantity"])
                print(f"{list_number}- {data["name"]} : ${data["price"]}")
                print(f"Quantity : {data["quantity"]}")
                product_ids.append(product.id)
        print()
        print(f"Total: ${total_price:.2f}")
        #ask for user input
        print()
        product_to_remove = int(input("Please enter the list number of the product you would like to remove: "))
        print()
        print("Item removed from cart!")
        print()
        #remove selected product from cart
        selected_product_id = product_ids[product_to_remove - 1]
        selected_product = db.collection("cart").document(selected_product_id).delete()

    #update quantity of item in cart
    elif user_choice == 4:
        cart_products = db.collection("cart").get()
        list_number = 0
        total_price = 0
        product_ids = []
        #display cart
        if not cart_products:
            print("The cart is empty!")
        else:
            for product in cart_products:
                data = product.to_dict()
                list_number += 1
                total_price += (data["price"] * data["quantity"])
                print(f"{list_number}- {data["name"]} : ${data["price"]}")
                print(f"Quantity : {data["quantity"]}")
                product_ids.append(product.id)
        print()
        print(f"Total: ${total_price}")
        print()
        #get user input
        product_to_quantify = int(input("Please enter the list number in which you want to change the quantity: "))
        new_quantity = int(input("Please enter the new quantity: "))
        print()
        print("Cart item updated!")
        print()
        #updated quantity for selected item
        selected_product_id = product_ids[product_to_quantify - 1]
        selected_product = db.collection("cart").document(selected_product_id).update({"quantity" : new_quantity})

    #display what is in the cart
    elif user_choice == 5:
        cart_products = db.collection("cart").get()
        list_number = 0
        total_price = 0
        #display cart
        if not cart_products:
            print("The cart is empty!")
        else:
            for product in cart_products:
                data = product.to_dict()
                list_number += 1
                total_price += (data["price"] * data["quantity"])
                print(f"{list_number}- {data["name"]} : ${data["price"]}")
                print(f"Quantity : {data["quantity"]}")
        print()
        print(f"Total: ${total_price}")
        print()

    #user quits
    elif user_choice == 6: 
        break

    #user input something wrong
    else:
        print("Please enter a number 1-6.")