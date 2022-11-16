def solution(n, lost, reserve):

    # 도난 체육복과 여벌 체육복이 중복되는 경우의 수 제외하기
    lost_student = set(lost) - set(reserve)
    reserve_student = set(reserve) - set(lost)

    for student in reserve_student:
        # 앞번호의 학생이 체육복을 잃어버렸을 때
        if (student - 1) in lost_student:
            # 도난당한 학생 목록에서 체육복을 빌리는데 성공한 학생의 인덱스 제외
            lost_student.remove(student - 1)
        # 뒷번호의 학생이 체육복을 잃어버렸을 때
        elif (student + 1) in lost_student:
            # 도난당한 학생 목록에서 체육복을 빌리는데 성공한 학생의 인덱스 제외
            lost_student.remove(student + 1)

    # 전체 학생 수에서 도난당한 학생의 수 제외
    answer = n - len(lost_student)

    return answer
