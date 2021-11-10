import time

from share_func.ran_array import ran_array


def dietAverage(records,month):
    result = []


    for i in range(month-1,len(records)): #이동 평균선을 구하기 위해선 month개월 만큼의 자료가 필요함 (index로 따졌을시 month-1 ~ len(records)-1 만큼)
        currentSum = 0

        for j in range(0,month):
            currentSum+=records[i-j] #i = 3 이라고 했을시 records[3-0,3-1,3-2,3-3] 즉 4개월치 값을 더함

        result.append(currentSum/month)

    print(result)
    # 백만개 1.133028268814087초


start = time.time()
dietAverage(ran_array(),4)
print("걸린 시간 : ",time.time()-start)