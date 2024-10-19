#Connecting Database with python file
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("e-commerce.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


#final a total price !!! USE THIS
# result = db.collection("products").get()
# total = 0
# for record in result:
#     data = record.to_dict()
#     total += data["price"]
# print(total)

user_choice = 1 

while user_choice != 6:
    print("Please choose an option: ")
    print("1. View available produce products for purchase")
    print("2. Add a product to your cart")
    print("3. Remove a product from your cart")
    print("4. Update a quantity in your cart")
    print("5. Display items in your cart")
    print("6. Quit")

    print()
    user_choice = int(input("Enter a number 1-6: "))
    print()

    #display products
    if user_choice == 1:
        products = db.collection("products").get()
        list_number = 0
        for product in products:
            data = product.to_dict()
            list_number += 1
            print(f'{list_number}- {data["name"]} : ${data["price"]:.2f}')
        print()

    #add product to cart and quantity
    elif user_choice == 2:
        #display the products
        products = db.collection("products").get()
        list_number = 0
        product_ids = []
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
        # add selected product to the cart 
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
        print()
        product_to_remove = int(input("Please enter the list number of the product you would like to remove: "))
        print()
        print("Item removed from cart!")
        print()

        selected_product_id = product_ids[product_to_remove - 1]
        selected_product = db.collection("cart").document(selected_product_id).delete()

    #update quantity of item in cart
    elif user_choice == 4:
        cart_products = db.collection("cart").get()
        list_number = 0
        total_price = 0
        product_ids = []
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

        product_to_quantify = int(input("Please enter the list number in which you want to change the quantity: "))
        new_quantity = int(input("Please enter the new quantity: "))
        print()
        print("Cart item updated!")
        print()

        selected_product_id = product_ids[product_to_quantify - 1]
        selected_product = db.collection("cart").document(selected_product_id).update({"quantity" : new_quantity})

    #display what is in the cart
    elif user_choice == 5:
        cart_products = db.collection("cart").get()
        list_number = 0
        total_price = 0
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