class CoinChangeCounter:
    def __init__(self):
        self.table = []

    #initialize the table with the given dimensions
    def count_ways(self, denominations, target_amount):
        #initialize the table with zeros
        self.table = [0] * (target_amount + 1)
        #there is one way to make 0 amount (use no coins)
        self.table[0] = 1

        #update the table for each coin
        for coin in denominations:
            for amount in range(coin, target_amount + 1):
                self.table[amount] += self.table[amount - coin]

        return self.table[target_amount]


def main():
    coin_change_counter = CoinChangeCounter()
    coin_denominations = [1, 2, 3]
    target_amount = 4

    #compute the number of ways to make the target amount
    ways = coin_change_counter.count_ways(coin_denominations, target_amount)
    print("Number of ways to make", target_amount, "using the given denominations:", ways)


if __name__ == "__main__":
    main()
