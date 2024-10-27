import csv

def write_grades():
#Asks how many students.
    num_students = int(input("Enter the number of students: "))

    #Open files 'grades.csv'.
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        #Write the header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

         #Collect information for each student
        for _ in range(num_students):
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            exam1 = int(input("Enter the grade for Exam 1: "))
            exam2 = int(input("Enter the grade for Exam 2: "))
            exam3 = int(input("Enter the grade for Exam 3: "))

            #Write student data as a new row in the CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("Grades saved to grades.csv")

# Part 2: Function to read and display data.
def display_grades():
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)

        print("\nStudent Grades:\n")
        for row in reader:
            print(f"{row[0]:<12} {row[1]:<12} {row[2]:<8} {row[3]:<8} {row[4]:<8}")

#Run both functions.
if __name__ == "__main__":
    write_grades()
    display_grades()

