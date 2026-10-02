import numpy as np 
import pandas as pd 

np.random.seed(42)

# code for student id 
number_of_students = 100
student_id = np.arange(1001,1001+number_of_students)
print(student_id)


# code for names 
names = np.array([
    "Aarav", "Arjun", "Aditya", "Rahul", "Rohan",
    "Vikram", "Karan", "Aryan", "Kabir", "Ananya",
    "Priya", "Sneha", "Ishita", "Diya", "Meera",
    "Aisha", "Neha", "Riya", "Kavya", "Pooja"
])
student_names = np.random.choice(names , size = number_of_students)
print(student_names)


# gender 
gender = np.array(["MALE", "FEMALE"] )
student_gender = np.random.choice(gender, size=number_of_students)
print(student_gender)



#age 
age = np.random.randint(20,25,size = number_of_students)
print(age)


# departments 
departments = np.array(["Computer science", "Mechanical", "Electronics", "Civil"])

student_department = np.random.choice(departments,size=number_of_students)
print(student_department)



# cgpa 

cgpa = np.round(np.random.uniform(5.0,10.0,size=number_of_students),2)
print(cgpa)



# attendance 
attendance = np.round(np.random.uniform(60,100,size=number_of_students),1)
print(attendance)

# projects 

projects = np.random.randint(0,6,size=number_of_students)
print(projects)


# internships 
internships = np.random.randint(0,4,size=number_of_students)
print(internships)


#skill scores 

coding_score = np.random.randint(30,101,size=number_of_students)
print(coding_score)

aptitude_score = np.random.randint(30,101,size=number_of_students)
print(aptitude_score)

communication_score = np.random.randint(30,101,size=number_of_students)
print(communication_score)



#placement_score

placement_score = (
    cgpa*10
    + attendance*0.15
    +projects*3
    +internships * 5
    + coding_score*0.20
    + aptitude_score * 0.10
    + communication_score * 0.10 
) 


# placed/not

placement_threshold = np.median(placement_score)
placed = np.where(placement_score >= placement_threshold,
                   "Placed",
                   "Not Placed")
 
 
print(placed)


# package 
base_package = ( 3+ (placement_score - placement_threshold)*0.08)

package_lpa = np.where(
    placed == "Placed"
    , np.round(base_package + np.random.uniform(0,4,size = number_of_students),2),
    0.0
)

print(package_lpa)



# data frame 

df = pd.DataFrame(
    {
        "student_id": student_id,
        "name": student_names,
        "gender": student_gender,
        "age": age,
        "department": student_department,
        "cgpa": cgpa,
        "attendance": attendance,
        "projects": projects,
        "internships": internships,
        "coding_score": coding_score,
        "aptitude_score": aptitude_score,
        "communication_score": communication_score,
        "placed": placed,
        "package_lpa": package_lpa,
    }
)

print(df.head())
print(df.shape)

df.to_csv("data/students.csv", index=False)