def calculate_percentage(marks, threshold):
    count = 0
    for mark in marks:
        if mark > threshold:
            count = count + 1

    percentage = (count / len(marks)) * 100

    return count, percentage



marks = [45, 67, 80, 55, 90, 32, 72, 60, 88, 49]
threshold = 60

number, percentage = calculate_percentage(marks, threshold)

print("Number of students above threshold:", number)
print("Percentage of students above threshold:", percentage, "%")
