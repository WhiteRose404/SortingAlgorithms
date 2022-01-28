def cuttingoff(array):
    for i in range(len(array)):
        array[i]=min(array[i],100)
        array[i]=max(array[i],0)

array = [int(input()) for i in range(len)]
cuttingoff(array)