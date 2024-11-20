from pymongo import MongoClient

# Connection string for your MongoDB Atlas cluster
CONNECTION_STRING = "mongodb+srv://umeshwar:123@cluster0.msbqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Initialize MongoDB client
client = MongoClient(CONNECTION_STRING)

# Create database and collection
db = client["mydatabase"]  # Replace with your database name
collection = db["mycollection"]  # Replace with your collection name

# Menu options
def menu():
    print("\nChoose an operation:")
    print("1. Insert One Record")
    print("2. Insert Many Records")
    print("3. List All Records")
    print("4. List a Particular Record")
    print("5. Update a Record")
    print("6. Delete a Record")
    print("7. Exit")

# 1. Insert One Record
def insert_one():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    record = {"name": name, "age": age, "city": city}
    result = collection.insert_one(record)
    print(f"Inserted record ID: {result.inserted_id}")

# 2. Insert Many Records
def insert_many():
    num_records = int(input("How many records do you want to insert? "))
    records = []
    for i in range(num_records):
        print(f"Record {i + 1}:")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        records.append({"name": name, "age": age, "city": city})
    result = collection.insert_many(records)
    print(f"Inserted record IDs: {result.inserted_ids}")

# 3. List All Records
def list_all():
    print("\nAll Records:")
    for record in collection.find():
        print(record)

# 4. List a Particular Record
def list_one():
    name = input("Enter the name to search: ")
    query = {"name": name}
    record = collection.find_one(query)
    if record:
        print(record)
    else:
        print("No record found with that name.")

# 5. Update a Record
def update_record():
    name = input("Enter the name of the record to update: ")
    new_age = int(input("Enter the new age: "))
    query = {"name": name}
    new_values = {"$set": {"age": new_age}}
    result = collection.update_one(query, new_values)
    if result.modified_count > 0:
        print("Record updated successfully.")
    else:
        print("No matching record found to update.")

# 6. Delete a Record
def delete_record():
    name = input("Enter the name of the record to delete: ")
    query = {"name": name}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        print("Record deleted successfully.")
    else:
        print("No matching record found to delete.")

# Main function
def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            insert_one()
        elif choice == "2":
            insert_many()
        elif choice == "3":
            list_all()
        elif choice == "4":
            list_one()
        elif choice == "5":
            update_record()
        elif choice == "6":
            delete_record()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
