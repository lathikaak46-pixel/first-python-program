print("Smart Campus Energy Saver")

students_present = input("Are students present in the classroom? (yes/no): ")

if students_present.lower() == "yes":
    print("Classroom occupied.")
    print("Lights and fans are ON.")
else:
    print("Classroom empty.")
    print("Lights and fans are automatically switched OFF.")

print("Thank you for using Smart Campus Energy Saver!")
