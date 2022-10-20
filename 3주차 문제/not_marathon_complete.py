def solution(participant, completion):
    answer = ''
    participant = sorted(participant) # 참여선수들을 차례로 정렬해준다.
    completion = sorted(completion)   # 완주선수들을 차레로 정렬해준다.

    # 참여자 명단에 동명이인이 있을 경우
    for i in range(len(completion)):        # 완주 선수들 길이만큼 반복 횟수를 정한다.
        if completion[i] != participant[i]: # 완주 선수 리스트 위치와 참여 선수 리스트 위치가 같지 않다면,
            answer = participant[i]         # 참여 선수의 i번 째 위치를 반환해준다.
            return answer
    
    answer = participant[-1]                # 두 리스트의 위치를 비교해서 참여 선수의 마지막 위치를 반환한다.
    
    
    return answer