import pandas as pd

df = pd.read_csv("data/students.csv")

# 1. Overall placement percentage
print("\n--- Overall Placement Percentage ---")
print(df["placed"].value_counts(normalize=True) * 100)


# 2. Placed students by department
print("\n--- Placed Students by Department ---")
print(
    df[df["placed"] == "Placed"]
    .groupby("department")
    .size()
)


# 3. Placement rate by department
print("\n--- Placement Rate by Department ---")
print(
    pd.crosstab(
        df["department"],
        df["placed"],
        normalize="index"
    ) * 100
)


# 4. Average CGPA by placement status
print("\n--- Average CGPA ---")
print(
    df.groupby("placed")["cgpa"].mean()
)


# 5. Average coding score by placement status
print("\n--- Average Coding Score ---")
print(
    df.groupby("placed")["coding_score"].mean()
)


# 6. Average attendance by placement status
print("\n--- Average Attendance ---")
print(
    df.groupby("placed")["attendance"].mean()
)


# 7. Projects and internships comparison
print("\n--- Projects and Internships ---")
print(
    df.groupby("placed")[["projects", "internships"]].mean()
)


# 8. Average package of placed students
print("\n--- Average Package ---")
print(
    df[df["placed"] == "Placed"]["package_lpa"].mean()
)


# 9. Top 5 placed students
print("\n--- Top 5 Students by Package ---")
print(
    df[df["placed"] == "Placed"][
        ["name", "department", "cgpa",
         "attendance", "coding_score", "package_lpa"]
    ]
    .sort_values("package_lpa", ascending=False)
    .head(5)
)

# Save important analysis results

placement_rate = df["placed"].value_counts(normalize=True) * 100

average_cgpa = df.groupby("placed")["cgpa"].mean()

average_coding = df.groupby("placed")["coding_score"].mean()

average_attendance = df.groupby("placed")["attendance"].mean()

average_package = df[df["placed"] == "Placed"]["package_lpa"].mean()

report = f"""
STUDENT PERFORMANCE & PLACEMENT ANALYTICS
==========================================

Total Students: {len(df)}

Placement Percentage:
{placement_rate}

Average CGPA by Placement Status:
{average_cgpa}

Average Coding Score by Placement Status:
{average_coding}

Average Attendance by Placement Status:
{average_attendance}

Average Package of Placed Students:
{average_package:.2f} LPA
"""

with open("outputs/reports/analysis_summary.txt", "w") as file:
    file.write(report)

print("\nAnalysis report saved successfully!")