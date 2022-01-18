def maxProfit(self, prices: List[int]) -> int:
    N = len(prices)
    min_ = [0] * N
    min_[0] = prices[0]
    max_ = 0
    for i in range(1, N):
        max_ = max(prices[i] - min_[i-1], max_)
        min_[i] = min(min_[i-1], prices[i])
    return max_