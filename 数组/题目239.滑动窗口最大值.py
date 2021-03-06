# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内
      的数字。滑动窗口每次只向右移动一位。返回滑动窗口最大值。

        输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
        输出: [3,3,5,5,6,7]

        滑动窗口的位置                最大值
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7


      分析：  剑指offer原题，较为简单吧


      思路： 按照之前的吧

'''



'''
     题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
     例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}。


     分析：这里 很明显的，  就是 是需要以滑动窗口的形式，对于n大小滑动窗口、窗口大小为k，  需要产生的滑动窗口最大值数量应该为：n-k+1
           主要按窗口逐步打出，基本思路包括以下几种：
           （1）最为简单，直接能够相当的，就是每次圈定一个滑动窗口，圈定后对窗口内的数排序得到最大即可。
                     但是这种方法的时间复杂度太高了   O((n-k+1)*k),这里后面乘k是因为内部找最大，太慢了，虽然空间复杂度是O(1)，但是这个方法太low了
           （2）第二种 是较为经典的双端 队列的方式，双端操作的方式，非常经典，该方法可以有效的令时间复杂度为O(n)，空间复杂度为O(k)

                用容量为k的双端队列存储数组元素的索引！！是索引，主要的思考是（视频解释：https://www.youtube.com/watch?v=2SXqBsTR6a8）：
                    【1】如果新来的值比队列尾部的数小，那就追加到后面，因为它可能在前面的最大值划出窗口后成为最大值
                    【2】如果新来的值比尾部的大，那就删掉尾部，再追加到后面
                    【3】如果追加的值的索引跟队列头部的值的索引 数量超过窗口大小k，那就删掉一个头部的值
                    【4】每次队列的头都是滑动窗口中值最大的
             使用上面方式的思考，对于队列来说，其实就是每次在保障在有效的窗口范围内，队列的第一个始终是窗口对应最大的。
           （3）第三种是 使用最大堆的方式，这个方法类同找topk问题一样，用堆方法特别好理解，构建一个窗口size大小的最大堆，
                          每次从堆中取出窗口的最大值，随着窗口往右滑动，需要将堆中不属于窗口的堆顶元素删除。

'''


class solution:
    #数组num   和  窗口大小size
    def maxinwindows(self,num,size):
        n=len(num)
        #边界条件
        if not num or size<=0 or size>n:
            return []

        #定义一个双端队列
        maxqueue=[]
        #定义存放要打印的 窗口中的最大值
        maxlist=[]

        #开始正式的进行遍历吧
        for i in range(n):
            #之前的处理三，  当队列头部 对应下标 跟当前索引下标差  是否  超出了 滑动窗口的限制。  那么就需要弹出队首操作
            if len(maxqueue)>0 and i-size>=maxqueue[0]:
                maxqueue.pop(0)

            #现在开始考虑处理二，如果新加入的大于前面的，那就不断pop吧      这里切记前面可不是全pop,而是只pop比当前值小的
            while len(maxqueue)>0 and num[i]>num[maxqueue[-1]]:
                maxqueue.pop()

            #正常的处理一
            maxqueue.append(i)

            #最后，保存下要打印的即可，结束...   从第size个开始打印
            if i>size-1:
                maxlist.append(num[maxqueue[0]])

        return maxlist


#___________________________________    练习1   ______________________________#
#  比较简单的一道题吧，不断进行 窗口内最大值的统计,  接下来就再来一遍比较经典的双端队列解法。  维护一个长度为size的双端队列
#  时间复杂度为O(N)，空间复杂度为O(k)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        # 边界条件
        if not nums or k<=0 or k>n:
            return []

        #定义双端队列   、  用于存储的窗口最大值    maxqueue中[0]表示最大的，然后后面的表示较小的候选的
        maxqueue=[]
        maxlist=[]

        #进行正式的 队列遍历填充过程
        for i in range(n):
            # 处理方式三   如果追加的值的索引跟队列头部的值的索引 数量超过窗口大小k，那就删掉一个头部的值 （i-k>=maxqueue[0] 表示 头部位置失效了）
            if len(maxqueue)>0 and i-k>=maxqueue[0]:
                maxqueue.pop(0)
            # 处理方式二   如果新来的值比尾部的大，那就删掉尾部，再追加到后面 （这个可以参考解析中的视频，可以弹弹弹，不断弹队尾）
            while len(maxqueue)>0 and nums[i]>nums[maxqueue[-1]]:
                maxqueue.pop()
            # 处理方式1    这里能够保证队列前面都是较大的原因是  如果新来的比之前的大，就会弹出去，而且是从队尾开始弹，所以不用顾虑
            maxqueue.append(i)
            #最后 进行保存
            if i>k-2:  #  每次队列的头都是滑动窗口中值最大的
                maxlist.append(nums[maxqueue[0]])
        # 进行窗口最大值的返回
        return maxlist

