import csv
subjects={}
with open("marks.csv") as f:
    r=csv.reader(f)
    next(r)
    for roll,name,sub,marks in r:
        marks=int(marks)
        if sub not in subjects:
            subjects[sub]=[(name,marks)]
        else:
            top=subjects[sub][0][1]
            if marks>top:
                subjects[sub]=[(name,marks)]
            elif marks==top:
                subjects[sub].append((name,marks))
for sub,students in subjects.items():
    names=", ".join([f"{n} ({m})" for n,m in students])
    print(f"Subject: {sub} → {names}")
