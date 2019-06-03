n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())

    if grade >= 38:
        # Here, we are only ever calculating 'grade mod 5' once:
        mod5 = grade % 5

        if mod5 >= 3:
            grade = grade + (5 - mod5)

    print(grade)
