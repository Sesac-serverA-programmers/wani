def solution(brown, yellow):
    answer = []

    # w >= h
    # 2w + 2h - 4 = brown
    # (w - 2) * (h - 2) = yellow
    # w * h = brown + yellow

    total = brown + yellow

    for h in range(1, total + 1):
        if (total / h) % 1 == 0:  # 전체 넓이 / 세로 = 가로
            w = total / h
            if w >= h:  # 가로는 세로보다 같거나 길다.
                if (2 * w) + (2 * h) == brown + 4:
                    return [w, h]

    return answer
