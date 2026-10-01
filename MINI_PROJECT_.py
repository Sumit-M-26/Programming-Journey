# ==========================================
#        RESUME BUILDER - MINI PROJECT
#        Introduction to Programming
# ==========================================

def get_list(title):
    print("\n" + title)
    data = []
    while True:
        x = input("Enter item (or 'done'): ")
        if x.lower() == "done":
            break
        if x.strip():
            data.append(x)
    return data


print("=" * 60)
print("                 RESUME BUILDER")
print("          Create Your Professional Resume")
print("=" * 60)

# ---------- PERSONAL INFORMATION ----------
print("\nPERSONAL INFORMATION")
name = input("Full Name: ")
email = input("Email: ")
phone = input("Phone: ")
address = input("Address: ")
linkedin = input("LinkedIn (optional): ")

# ---------- CAREER OBJECTIVE ----------
print("\nCAREER OBJECTIVE")
objective = input("Career Objective: ")

# ---------- EDUCATION ----------
print("\nEDUCATION")
education = []

while True:
    degree = input("Degree/Course (or 'done'): ")
    if degree.lower() == "done":
        break

    college = input("College/School: ")
    year = input("Passing Year: ")
    percentage = input("Percentage/CGPA: ")

    education.append([degree, college, year, percentage])

# ---------- OTHER DETAILS ----------
skills = get_list("SKILLS")
certifications = get_list("CERTIFICATIONS")
hobbies = get_list("HOBBIES")

# ---------- PROJECTS ----------
print("\nPROJECTS")
projects = []

while True:
    project = input("Project Name (or 'done'): ")
    if project.lower() == "done":
        break

    description = input("Project Description: ")
    projects.append([project, description])

# ---------- WORK EXPERIENCE ----------
print("\nWORK EXPERIENCE")
experience = []

while True:
    company = input("Company Name (or 'done'): ")
    if company.lower() == "done":
        break

    position = input("Position: ")
    duration = input("Duration: ")
    experience.append([company, position, duration])


# ==========================================
#          GENERATING RESUME
# ==========================================

print("\n" + "=" * 60)
print("                     RESUME")
print("=" * 60)

print("\n" + name.upper())
print("Email:", email)
print("Phone:", phone)
print("Address:", address)

if linkedin.strip():
    print("LinkedIn:", linkedin)

print("\n" + "-" * 60)
print("CAREER OBJECTIVE")
print("-" * 60)
print(objective)

print("\n" + "-" * 60)
print("EDUCATION")
print("-" * 60)

for e in education:
    print("Degree:", e[0])
    print("College:", e[1])
    print("Year:", e[2])
    print("Percentage/CGPA:", e[3])

print("\n" + "-" * 60)
print("SKILLS")
print("-" * 60)

for skill in skills:
    print("•", skill)

print("\n" + "-" * 60)
print("PROJECTS")
print("-" * 60)

for p in projects:
    print("Project:", p[0])
    print("Description:", p[1])

print("\n" + "-" * 60)
print("WORK EXPERIENCE")
print("-" * 60)

for e in experience:
    print("Company:", e[0])
    print("Position:", e[1])
    print("Duration:", e[2])

print("\n" + "-" * 60)
print("CERTIFICATIONS")
print("-" * 60)

for c in certifications:
    print("•", c)

print("\n" + "-" * 60)
print("HOBBIES")
print("-" * 60)

for h in hobbies:
    print("•", h)

print("\n" + "=" * 60)
print("        RESUME CREATED SUCCESSFULLY!")
print("=" * 60)
print("Thank you for using Resume Builder!")
