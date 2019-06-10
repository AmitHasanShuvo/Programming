def result(score):
    min = max = score[0]
    min_count = max_count = 0
    for i in score[1:]:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i

    return max_count, min_count


n = input()
score = list(map(int, input().split()))
print(*result(score))
