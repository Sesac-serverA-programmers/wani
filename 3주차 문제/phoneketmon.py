def solution(nums):
    answer = 0

    num = len(nums) // 2   # 가져가도 되는 폰켓몬의 갯수
    arr = list(set(nums))  # 폰켓몬 중복 제거 후 리스트에 삽입

    if len(arr) > num:     # 정렬된 폰켓몬 갯수가 가져가도 되는 폰켓몬 갯수보다 크다면, num을 리턴
        answer = num
    else:                  # 정렬된 폰캣몬의 갯수가 num과 같거나 적다면, 중복을 제거한 폰켓몬을 리턴
        answer = len(arr)

    return answer
