from pymongo import MongoClient


# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if needed
db = client['mydatabase']  # This will create 'mydatabase' if it doesn't exist
collection = db['mycollection']  # This will create 'mycollection' if it doesn't exist

# Step 2: CREATE - Insert a new document (user) into the collection
def create_user(name, age, blood_group):
    user_data = {
        'name': name,
        'age': age,
        'blood_group': blood_group
    }
    user_id = collection.insert_one(user_data).inserted_id
    print(f"User added with ID: {str(user_id)}")

# Step 3: READ - Get all users from the collection
def get_all_users():
    users = list(collection.find())
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string for display purposes
        print(user)

# Step 4: READ by ID - Get a user by their ID
def get_user_by_id(user_id):
    try:
        user = collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])  # Convert ObjectId to string for display
            print(user)
        else:
            print("User not found")
    except Exception as e:
        print("Invalid ID format")

# Step 5: UPDATE - Update a user's information by their ID
def update_user(user_id, name=None, age=None, blood_group=None):
    update_data = {}
    if name:
        update_data['name'] = name
    if age:
        update_data['age'] = age
    if blood_group:
        update_data['blood_group'] = blood_group

    if not update_data:
        print("No data provided for update")
        return

    try:
        result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        if result.matched_count:
            print("User updated successfully")
        else:
            print("User not found")
    except Exception as e:
        print("Invalid ID format")

# Step 6: DELETE - Delete a user by their ID
def delete_user(user_id):
    try:
        result = collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count:
            print("User deleted successfully")
        else:
            print("User not found")
    except Exception as e:
        print("Invalid ID format")

# Step 7: Menu-driven interface to perform CRUD operations
if __name__ == "__main__":
    while True:
        print("\nCRUD Operations Menu:")
        print("1. Add User")
        print("2. Get All Users")
        print("3. Get User by ID")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            blood_group = input("Enter blood group: ")
            create_user(name, age, blood_group)

        elif choice == '2':
            get_all_users()

        elif choice == '3':
            user_id = input("Enter user ID: ")
            get_user_by_id(user_id)

        elif choice == '4':
            user_id = input("Enter user ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age_input = input("Enter new age (leave blank to skip): ")
            blood_group = input("Enter new blood group (leave blank to skip): ")
            age = int(age_input) if age_input else None
            update_user(user_id, name, age, blood_group)

        elif choice == '5':
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

