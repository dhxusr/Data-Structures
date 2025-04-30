"""
Write a program that takes as input a sequence of transactions of the form "buy x shares at $y each" or
"sell x shares at $y each", assuming that the transactions occur on consecutive days and x and y are integers
Given this input sequence, the output should be the total capital gain (or loss) for the entire sequence, using
the FIFO protocol to identify shares.
"""

from collections import deque
import datetime

class SharesGains():

    def __init__(self):
        self._shares = deque()
        self._gains = 0


    def inpt(self, sequence: str):

        if not isinstance(sequence, str):
            raise TypeError("Sequence must be of type 'str'.")

        sequence = sequence.split(' ')
        if sequence[0] == "buy":
            print("Buying shares...")
            shares = int(sequence[1])
            price = int(sequence[4].strip('$'))

            for _ in range(shares):
                self._shares.append(price)
            print("shares bought successfully.")

        elif sequence[0] == "sell":
            print("Selling shares...")
            sold_shares = int(sequence[1])
            price = int(sequence[4].strip('$'))    

            if len(self._shares) >= sold_shares:
                for _ in range(sold_shares):
                    share_price = self._shares.popleft()
                    self._gains += (price - share_price)
                print("Shares sold successfully.")

            else:
                print("Invalid operation, there's no enough shares to sell.")

        else:
            print("Invalid input. must be: buy/sell x shares at $y each")


    def get_gains(self):

        if self._gains < 0:
            print(f"lost {-self._gains}$.")

        else:
            print(f"Gain {self._gains}$.")


if __name__ == "__main__":

    myshares = SharesGains()

    myshares.inpt("buy 10 shares at $5")
    myshares.inpt("buy 20 shares at $6")
    
    myshares.inpt("sell 20 shares at $3")
    myshares.inpt("sell 10 shares at $10")
    myshares.get_gains()
    myshares.inpt("sell 5 shares at $5")
