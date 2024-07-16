class CoinChangeCounter:
    def __init__(self):
        self.table = []

    #initialize the table with the given dimensions
    def count_ways(self, denominations, target_amount):
        num_denominations = len(denominations)
        
        #initialize the table with zeros
        self.table = [[0 for _ in range(num_denominations)] for _ in range(target_amount + 1)]

        #fill the first column with 1, because there's one way to make 0 using any coin
        for i in range(num_denominations):
            self.table[0][i] = 1

        #fill the table entries in a bottom-up manner
        for i in range(1, target_amount + 1):
            for j in range(num_denominations):
                #calculate ways including the current coin
                ways_with_current_coin = self.table[i - denominations[j]][j] if i - denominations[j] >= 0 else 0
                #calculate ways excluding the current coin
                ways_without_current_coin = self.table[i][j - 1] if j >= 1 else 0

                #sum both ways
                self.table[i][j] = ways_with_current_coin + ways_without_current_coin

        return self.table[target_amount][num_denominations - 1]


def main():
    coin_change_counter = CoinChangeCounter()
    coin_denominations = [1, 2, 3]
    target_amount = 4

    #compute the number of ways to make the target amount
    ways = coin_change_counter.count_ways(coin_denominations, target_amount)
    print("Number of ways to make", target_amount, "using the given denominations:", ways)


if __name__ == "__main__":
    main()
