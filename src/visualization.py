import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("data/students.csv")

# Average package by department

df.groupby("department")["package_lpa"].mean().plot(kind="bar")

plt.title("Average Package by Department")
plt.xlabel("Department")
plt.ylabel("Average Package (LPA)")

plt.savefig("outputs/charts/average_package_by_department.png")
plt.show()



# Placement status

df.groupby("placed").size().plot(kind="bar")

plt.title("Placement Status")
plt.xlabel("Placement")
plt.ylabel("Number of Students")

plt.savefig("outputs/charts/placement_status.png")
plt.show()

# CGPA vs Package

df.plot(x="cgpa", y="package_lpa", kind="scatter")

plt.title("CGPA vs Package")
plt.xlabel("CGPA")
plt.ylabel("Package (LPA)")

plt.savefig("outputs/charts/cgpa_vs_package.png")
plt.show()