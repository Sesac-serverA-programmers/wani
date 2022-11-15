def solution(answers):
    result = []
    score = [0, 0, 0]  # 각 학생이 얻는 점수 초깃값 저장
    supoja_one = [1, 2, 3, 4, 5]
    supoja_two = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, answer in enumerate(answers):
        # 찍을 숫자와 정답이 같은 경우 맞춘 횟수를 올려준다
        if answer == supoja_one[idx % len(supoja_one)]:
            # print("answer :", answer)
            # print("idx :", idx)
            score[0] += 1
        if answer == supoja_two[idx % len(supoja_two)]:
            score[1] += 1
        if answer == supoja_three[idx % len(supoja_three)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result
