# Problem link
# https://www.geeksforgeeks.org/batch/dsa-python-self-paced-april/track/hashing-basic-python/problem/hashing-for-pair-1


def sumExists(arr, N, sum):
    # Your code here

    dict = {}

    count = 0

    for ele in arr:
        dict[ele] = ele

    for key in dict.keys():
        j = sum - dict[key]

        if (j in dict.keys()) and (j != key):
            print(j)
            count = count + 1


    if count > 0:
        return 1
    return 0

sumExists([61 ,14 ,75 ,71 ,36 ,34 ,12], 7,68)