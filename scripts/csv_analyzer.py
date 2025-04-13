import csv

def analyze_csv(file_path, threshold):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            grades = list(map(float, row['grade'].split(',')))
            average = sum(grades) / len(grades)
            if average > threshold:
                print(row['name'])

analyze_csv("students.csv", 75)