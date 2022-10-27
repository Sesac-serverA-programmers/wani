def solution(triangle):
    answer = 0

    # 삼각형 길이만큼 반복문 돌리는 범위 정하기
    for i in range(1, len(triangle)):
        # 0부터 i까지 출력되는 삼각형 경우의 수 모두 구해주기
        for j in range(len(triangle[i])):
            # 처음값(맨 꼭지점 윗값)이 0이라면
            if j == 0:
                # 각 아래 끝값과 더해주기
                triangle[i][j] += triangle[i-1][0]
            # 나머지 두 꼭짓점 중 더 큰 값일 경우
            elif j == len(triangle[i]) - 1:
                # 해당 자리에서 각 꼭짓점 값을 찾아서 더해주기
                triangle[i][j] += triangle[i-1][j-1]
            # 나머지 꼭짓점(작은) 값일 경우
            else:
                # 해당 자리에서 더 큰값을 찾아 더해주기
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        # 삼각형의 최댓값 구해주기
        answer = max(triangle[-1])

    return answer
