from icecream import ic
num = input()

snum = str(num)
#if snum[len(snum)-1] != '0':

for i in range(len(snum)):
    snum[len(snum)-i-1]