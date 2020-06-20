# Author:peter young
from typing import List
#不排序去重！

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         size = len(candidates)
#         if size == 0:
#             return []
#         # 剪枝是为了提速，在本题非必需
#         # candidates.sort()
#         # 在遍历的过程中记录路径，它是一个栈
#         path = []
#         res = []
#         # 注意要传入 size ，在 range 中， size 取不到
#         self.__dfs(candidates, 0, size, path, res, target)
#         return res
#
#     def __dfs(self, candidates, begin, size, path, res, target):
#
#         # 先写递归终止的情况
#         if target == 0:
#             res.append(path[:])
#             return
#
#         for i in range(begin,size):
#             if(candidates[i]<=target):
#                 path.append(candidates[i])
#                 self.__dfs(candidates,i,size,path,res,target-candidates[i])
#                 path.pop()

# def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
#     size = len(candidates)
#     if size == 0:
#         return []
#     path = []
#     res = []
#         # 注意要传入 size ，在 range 中， size 取不到
#     dfs(candidates, 0, size, path, res, target)
#     return res
#
# def dfs(candidates, begin, size, path, res, target):
#
#         # 先写递归终止的情况
#     if target == 0:
#         res.append(path[:])
#         return
#
#     for i in range(begin,size):
#         if(candidates[i]<=target):
#             path.append(candidates[i])
#             dfs(candidates,i,size,path,res,target-candidates[i])
#             path.pop()


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    size = len(candidates)
    if size == 0:
        return []
    path = []
    res = []
        # 注意要传入 size ，在 range 中， size 取不到

    def dfs(begin, target):
        if target == 0:
            res.append(path[:])
            return

        for i in range(begin, size):
            if (candidates[i] <= target):
                path.append(candidates[i])
                dfs(i, target - candidates[i])
                path.pop()

    dfs(0, target)
    return res

if __name__ == '__main__':
    candidates = [8,7,4,3]
    target = 11
    # solution = Solution()
    # result = solution.combinationSum(candidates, target)
    result=combinationSum(candidates,target)
    print(result)

