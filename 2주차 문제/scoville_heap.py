import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # heapq 리스트 선언하기
    
    while scoville[0] < K: # 스코빌이 K보다 크거나 같아질 때까지 반복문 실행
        
        if len(scoville) > 1:
            answer += 1
            first = heapq.heappop(scoville) # scoville이 가장 낮은 음식의 값을 return하며 삭제
            second = heapq.heappop(scoville) # scoville이 두 번째로 낮은 음식의 값을 return하며 삭제
            heapq.heappush(scoville, first + second * 2) # scoville에 섞은 음식의 스코빌 지수 자동 정렬
        else:
            return -1 # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없을 때

    return answer