#我的做法

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) == 0:
            return result
        elif len(nums) < k:
            return [max(nums)]

        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))
        return result

#双端队列 https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/
#每次push进去都把后边比他小的挤压掉，第一个一直都是最大的
class MonotonicQueue {
private:
    deque < int > data;
    public:
    void


push(int
n) {
while (!data.empty() & & data.back() < n)
data.pop_back();
data.push_back(n);
}

int
max()
{
return data.front();}

void
pop(int
n) {
if (!data.empty() & & data.front() == n)
data.pop_front();
}
};

vector < int > maxSlidingWindow(vector < int > & nums, int
k) {
    MonotonicQueue
window;
vector < int > res;
for (int i = 0; i < nums.size();
i + +) {
if (i < k - 1) {// 先填满窗口的前 k - 1
window.push(nums[i]);
} else {// 窗口向前滑动
window.push(nums[i]);
res.push_back(window.max());
window.pop(nums[i - k + 1]);
}
}
return res;
}



