class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n 
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy() # 在初始的時候把當前的狀態快取一份
            for start, distination, price in flights:
                if prices[start] == float('inf'):
                    continue
                if prices[start] + price < tmpPrices[distination]:
                    tmpPrices[distination] = prices[start] + price
            prices = tmpPrices  # 更動完後 把快取狀態更新回去歷史狀態
        return -1 if prices[dst] == float("inf") else prices[dst]