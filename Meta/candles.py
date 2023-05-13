"""Candle Sticks Class & Properties"""


class Candlesticks:

    def isDoji(self, frame) -> bool:
        body = abs(frame.open - frame.close)
        candle = abs(frame.high - frame.low)
        average_price = frame.high + frame.low / 2

        percentage = round(float((body/candle) * 1), 2)

        h = average_price + (frame.high - average_price) * 0.2
        l = average_price - (average_price - frame.low) * 0.2

        if frame.close > frame.open:
            if percentage <= 0.20 and h <= frame.close and l <= frame.open:
                return True

            else:
                return False

        elif frame.open > frame.close:
            if percentage <= 0.20 and h <= frame.open and l <= frame.close:
                return True

            else:
                return False

        elif frame.open == frame.close:
            if percentage <= 0.20:
                return True

            else:
                return False

        # if percentage <= 0.30 and h <= self.open and l <= self.close:
        #     return True

        # return False

    def isSpinningTop(self, frame):
        body = abs(frame.open - frame.close)
        candle = abs(frame.high - frame.low)
        average_price = frame.high + frame.low / 2

        percentage = round(float((body/candle) * 1), 2)

        h = average_price + (frame.high - average_price) * 0.3
        l = average_price - (average_price - frame.low) * 0.3

    def isBullMaburuzu(self, frame):
        if frame.close > frame.open:
            body = abs(frame.close - frame.open)
            candle = abs(frame.high - frame.low)

            percentage = round(float((body/candle) * 1), 2)

            if percentage >= 0.65:
                return True
            else:
                return False

        else:
            return False

    def isBearMaburuzu(self, frame):
        if frame.open > frame.close:
            body = abs(frame.open - frame.close)
            candle = abs(frame.high - frame.low)

            percentage = round(float((body/candle) * 1), 2)
            if percentage >= 0.65:
                return True
            else:
                return False

        else:
            return False

    def isDragonFlyDoji(self, frame):
        body = abs(frame.open - frame.open)
        candle = abs(frame.high - frame.low)

        percentage = round(float((body/candle) * 1), 2)

        mid = (frame.high + frame.low) / 2
        h = mid + ((frame.high - mid) * 0.2)
        if percentage <= 0.2 and frame.open >= h and frame.close >= h:
            return True
        else:
            return False

    def isGravestoneDoji(self, frame):
        body = abs(frame.open - frame.open)
        candle = abs(frame.high - frame.low)

        percentage = round(float((body/candle) * 1), 2)

        mid = (frame.high + frame.low) / 2
        h = mid - ((frame.high - mid) * 0.2)
        if percentage <= 0.2 and frame.open <= h and frame.close <= h:
            return True
        else:
            return False

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
