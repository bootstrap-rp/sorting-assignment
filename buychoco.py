def buyChoco(prices: list[int], money: int) -> int:
        prices.sort()
        price = prices[0] + prices[1]
        if price <= money:
            return money - price
        return money

print(buyChoco([3,2,3],3))