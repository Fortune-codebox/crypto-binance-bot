"""Candle Sticks Class & Properties"""


class Candlesticks:
    def __init__(self, high, low, open, close):
        self.high = high
        self.low = low
        self.open = open
        self.close = close

    def isDoji(self):
        pass

    def isBullMaburuzu(self):
        if self.close > self.open:
            body = self.close - self.open
            candle = self.high - self.low

            percentage = round(float((body/candle) * 1), 2)

            if percentage > 0.70:
                return True
            else:
                return False

        else:
            return False

    def isBearMaburuzu(self):
        pass

    def isDragonFly(self):
        pass

    def isGravestoneDoji(self):
        pass

    def isBullEngulfing(self):
        pass

    def isBearEngulfing(self):
        pass

    def isBullInsideBar(self):
        pass

    def isBearInsideBar(self):
        pass

    def isMorningStar(self):
        pass

    def isEveningStar(self):
        pass

    def isTweezerBottom(self):
        pass

    def isTweezersTop(self):
        pass
