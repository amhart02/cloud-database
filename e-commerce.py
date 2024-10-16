#Connecting Database with python file
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("e-commerce.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# collection is the table, document is something in that table, field is an attribute of that something 

#final a total price !!! USE THIS
# result = db.collection("products").get()
# total = 0
# for record in result:
#     data = record.to_dict()
#     total += data["price"]
# print(total)

# #how to print stuff
# for record in result:
#     data = record.to_dict()
#     print(record.id)
#     print(f"{record.id} : {data["name"]}")

# #get user input
# choice = input("Select a product: ")
# new_price = int(input("What is the new product price? "))
# #setting a new product into the database
# result = db.collection("products").document(choice).set({"name" : choice, "price" : new_price})
# #getting the data from the database
# result = db.collection("products").document(choice).get()
# #measures to ensure data comes through
# data = result.to_dict()
# if data is None: 
#     print("Invalid Product")
# else:
#     print(data["price"])

# db.collection("products").document("2").set({"name" : "grapes", "description" : "purple yummy", "price" : 3.99})

# #to delete a varible from the database table
# db.collection("products").document("2").delete()

# #user input and adding a new phonenumber 
# new_number = input("What is the new phone number: ")
# db.collection("users").add({"phone number" : new_number})

#get all the users in the users table
# results = db.collection("users").get()
# #use conditioning when getting a user 
# results = db.collection("users").where("phone number", "==", 90).where("phone number", ">=", 80).get()
# #printing out all the user ids and phone numbers 
# for result in results:
#     data = result.to_dict()
#     print(f"id = {result.id} phone number = {data["phone number"]}")

#more examples of what we've been doing
# name = input("Which name? ")
# phoneNumber = input("Which phone number? ")
# new_number = input("New number: ")

# results = db.collection("grades").where("name", "==", name).where("phone number", "==", phoneNumber).get()
# if len(results) == 1:
#     id = result[0].id
#     db.collection("users").document(id).set({"name": name, "phone number" : new_number})
# else: 
#     print("Can't find the record")

#### START OF ACTUAL PROJECT ####

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
        products = db.collection("products").get()
        list_number = 0
        product_ids = []
        for product in products:
            data = product.to_dict()
            list_number += 1
            print(f'{list_number}- {data["name"]} : ${data["price"]:.2f}')
            product_ids.append(product.id)
        print()
        product_to_add = int(input("Please enter the list number of the product you would like to add: "))
        quantity_to_add = int(input("Please enter the quantity of the product to add to your cart: "))
        print()
        print("Item added to cart!")
        print()
        
        selected_product_id = product_ids[product_to_add - 1]
        selected_product = db.collection("products").document(selected_product_id).get()
        data = selected_product.to_dict()
        db.collection("cart").add({"name" : data["name"] , "price" : data["price"] , "quantity" : quantity_to_add})

    #remove product from cart
    elif user_choice == 3:
        print()
    #update quantity of item in cart
    elif user_choice == 4:
        print()
    #display what is in the cart
    elif user_choice == 5:
        print()
    #user quits
    elif user_choice == 6: 
        break

    #user input something wrong
    else:
        print("Please enter a number 1-6.")