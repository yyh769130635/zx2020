# Author:peter young
import pandas as pd
import numpy as np
import time
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

def lianxi2(data,m,n):
    ##预处理工作，将两个村庄构建联系
    listA = []
    for i in range(len(data)):
        listTemp = []
        for j in range(len(data[0])):
            if (data[i][j] == 1):
                listTemp.append(j)
        listA.append(listTemp)
    # 列的好友索引
    listB = []
    for j in range(len(data[0])):
        listTemp = []
        for i in range(len(data)):
            if (data[i][j] == 1):
                listTemp.append(i+n)
        listB.append(listTemp)
    total = listB + listA
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


def isin(res,path,count):
    res[(count - 4) // 2].append(path[:])
    return


def xx(i,res,total,level):
    path = []
    path.append(i)
    count=1
    A=i

    def dfs_new(A, curr, count):
        temp=total[curr]
        for index in total[curr]:
            if(count%2 == 0):
                if(index<A):
                    continue
                else:
                    if (count == 2 and index == A):
                        continue
                    else:
                        if (index in path and index!=A):
                            continue
                        else:
                            if (count < level):
                                if(index==A):
                                    # path.append(index)
                                    res[(count - 4) // 2].append(path[:])
                                    # path.pop()
                                    continue
                                else:
                                    path.append(index)
                                    dfs_new(A, index, count + 1)
                                    path.pop()

                            elif (count == level):
                                if (index != A):
                                    return
                                elif (index == A):
                                    # path.append(index)
                                    res[(count - 4) // 2].append(path[:])
                                    # path.pop()
                                    return
            elif( count%2 == 1):
                if(index in path):
                    continue
                else:
                    path.append(index)
                    dfs_new(A, index, count + 1)
                    path.pop()

    dfs_new(A, i ,count)

    return


if __name__ == '__main__':
    data = np.loadtxt(open("Example.csv", "rb"), delimiter=",", skiprows=0)
    m,n=data.shape
    # total=lianxi2(data,m,n)
    first=time.time()
    total = lianxi(data, m, n)

    level=12
    res=[[],[],[],[],[],[]]

# 开始遍历树
    start=time.time()
    print("构造表的时间: %f"%(start-first))
    # xx(0, res, total, level)#用来测试的
    print("遍历树中............")
    for i in range(m):
        xx(i,res,total,level)
    end1=time.time()
    print("树遍历的时间为 %f 秒"%(end1-start))

#开始去重
    for i in range(len(res)):
        # print("去重前有：%d" % len(res[i]))
        count=mySort(res[i])
        print("木托盘上有%d个名字的祭品最多有"%(i*2+4))
        print("answer:%d"%count)

    end2=time.time()
    print(" 去重的时间%f 秒"%(end2-end1))
    print("总时间 %f 秒"%(end2-first))