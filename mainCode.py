# Author:peter young
##这个是一层一层来遍历的
import pandas as pd
import numpy as np
import os
import copy

def lianxi(data,m,n):
    ##预处理工作，将两个村庄构建联系
    listA = []
    for i in range(len(data)):
        listTemp = []
        for j in range(len(data[0])):
            if (data[i][j] == 1):
                listTemp.append(j + m)
        listA.append(listTemp)
    # 列的好友索引
    listB = []
    for j in range(len(data[0])):
        listTemp = []
        for i in range(len(data)):
            if (data[i][j] == 1):
                listTemp.append(i)
        listB.append(listTemp)
    total = listA + listB
    return total

def dfs(A,i,total,count,path,res,C):
    #递归结束条件
    if(count==0):
        if(i==A):
            # path.sort()
            # if(path[:] not in res):
            res.append(path[:])
            return
        else:
            return

    temp=total[i]
    for index in total[i]:
        if(count>1 and index==A):
            continue

        #不允许出现重复的人名
        if(index in path):
            continue
        path.append(index)
        dfs(A,index,total,count-1,path,res,C)
        path.pop()

def xxx(A,i,total,count):
    path = []
    res = []
    C=count
    dfs(A,i,total,count,path,res,C)
    return res

def paixu(res):
    length=len(res)
    # 先对每一行，行中元素排序
    for i in range(length):
       res[i].sort()
    list_new=[]
    for i in res:
        if i not in list_new:
            list_new.append(i)
    count=len(list_new)
    return count


def mySort(res):
    res_dic = {}
    count = 0
    for c in res:
        c.sort()
        x = '/'.join(map(str, c))
        if x not in res_dic:
            count += 1
            res_dic[x] = 1
    return count

if __name__ == '__main__':
    data = np.loadtxt(open("Example.csv", "rb"), delimiter=",", skiprows=0)
    m,n=data.shape
    total=lianxi(data,m,n)
    # print(len(total))
    for count in range(8,10,2):
        res=[]
        for i in range(m):
            res=res+(xxx(i,i,total,count))
        print(len(res))
        # num=paixu(res)
        # print("count=%d"%count)
        # print("answer=%d"%num)
