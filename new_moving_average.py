import time

from share.ran_array import ran_array


def dietAverage(records,month):
    result = []


    sum = 0
    # M = month
    # 최소 필요한 자료양 = M 개월 만큼의 자료양
    # 처음 records[0인덱스~M-1인덱스]만큼의 값으로 이동 평균선을 넣어준뒤
    for i in range(0,month):
        sum+=records[i]
    result.append(sum/month)

    # records[M인덱스]값의 이동 평균선 = (records[0~M-1]의 합 + records[M] - records[0])/2 이다
    for i in range(month,len(records)):
        sum+=records[i] #sum + records[M]
        sum-=records[i-month] # (sum + records[M]) - records[i-month===(0)]
        result.append(sum/month)
    print(result)
    # 이렇게 수정시 / 이중 for문 O(N**2) >> M+(N-M) =  O(N)
    # 백만개 0.8317549228668213초



start = time.time()
dietAverage(ran_array(),4)
print("걸린 시간 : ",time.time()-start)