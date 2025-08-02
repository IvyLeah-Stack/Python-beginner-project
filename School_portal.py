#Credentials of the stdents
students = {
    "Ivy Leah": {
        "registration": "DPP3/6633/2023",
        "password": "Ivy22"
    }
}

# Function to authenticate user
def authenticate(username, registration, password):
    if username in students:
        if (students[username]["registration"] == registration and 
            students[username]["password"] == password):
            return True
    return False

# Function to display dashboard
def show_dashboard():
    while True:
        print("\n------ DASHBOARD ------")
        print("1. Home")
        print("2. Student Fees")
        print("3. Course Registration")
        print("4. Results")
        print("5. Logout")
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            print("\n[] Welcome to the Home panel.")
            print("=" * 50)
            print("UPCOMING STUDENT EVENTS")
            print("=" * 50)
            print("• Introduction of the New Vice Chancellor")
            print("• First Years Admission - 20/09/2023")
            print("=" * 50)
            
        elif choice == "2":
            print("\n[] Here is your Student Fees information.")
            print("=" * 50)
            print(" STUDENT FEES SUMMARY")
            print("=" * 50)
            print("Amount Paid: KSH 200,000")
            print("Remaining Balance: KSH 40,000")
            print("=" * 50)
            
        elif choice == "3":
            print("\n[] Register your courses here.")
            print("=" * 50)
            print("REGISTERED COURSES")
            print("=" * 50)
            print("1. Project Planning Tools and Techniques")
            print("2. Micro-economics")
            print("3. Macro Economics")
            print("4. Procurement and Supply Chain Management")
            print("5. Fundamentals of Accounting")
            print("=" * 50)
            
        elif choice == "4":
            print("\n[] View your Results here.")
            print("=" * 50)
            print("🎓 ACADEMIC RESULTS")
            print("=" * 50)
            print("• Micro Economics: A")
            print("• Macro Economics: B")
            print("• Project Planning Tools and Techniques: C")
            print("• Microeconomics: A")
            print("• Fundamentals of Accounting: E")
            print("• Procurement and Supply Chain Management: A")
            print("=" * 50)
            print("  IMPORTANT NOTICE:")
            print("You received an E grade in Fundamentals of Accounting.")
            print("You are required to do a supplementary exam for this course.")
            print("Please contact the academic office for exam scheduling.")
            print("=" * 50)
            
        elif choice == "5":
            print("\n[🚪] Logging out...")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

# Main login 
def login():
    attempts = 3
    while attempts > 0:
        print("\n=== School Portal Login ===")
        username = input("Enter Username: ").strip()
        registration = input("Enter Registration Number: ").strip()
        password = input("Enter Password: ").strip()
        
        if authenticate(username, registration, password):
            print("\n✅ Login successful. Welcome,", username)
            show_dashboard()
            return
        else:
            attempts -= 1
            print(f" Invalid credentials. {attempts} attempt(s) left.")
    
    print("\n Too many failed attempts. You have been completely logged out of the system.")
    print("Please contact the system administrator for assistance.")
    print("System access has been temporarily suspended for security reasons.")

# Start the program
if __name__ == "__main__":
    login()