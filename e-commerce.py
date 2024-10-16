import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("e-commerce.json")
firebase_admin.initialize_app(cred)

db = firestore.client()



########

# result = db.collection("products").get()
# total = 0
# for record in result:
#     data = record.to_dict()
#     total += data["price"]
# print(total)

# for record in result:
#     data = record.to_dict()
#     print(record.id)
#     print(f"{record.id} : {data["name"]}")

# choice = input("Select a product: ")
# new_price = int(input("What is the new product price? "))
# result = db.collection("products").document(choice).set({"name" : choice, "price" : new_price})
# result = db.collection("products").document(choice).get()
# data = result.to_dict()
# if data is None: 
#     print("Invalid Product")
# else:
#     print(data["price"])

# db.collection("products").document("2").set({"name" : "grapes", "description" : "purple yummy", "price" : 3.99})

# db.collection("products").document("2").delete()

new_number = input("What is the new phone number: ")
db.collection("users").add({"phone number" : new_number})

results = db.collection("users").get()
# results = db.collection("users").where("phone number", "==", 90).where("phone number", ">=", 80).get()
for result in results:
    data = result.to_dict()
    print(f"id = {result.id} phone number = {data["phone number"]}")

name = input("Which name? ")
phoneNumber = input("Which phone number? ")
new_number = input("New number: ")

results = db.collection("grades").where("name", "==", name).where("phone number", "==", phoneNumber).get()
if len(results) == 1:
    id = result[0].id
    db.collection("users").document(id).set({"name": name, "phone number" : new_number})
else: 
    print("Can't find the record")