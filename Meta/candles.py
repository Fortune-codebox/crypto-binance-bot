"""Candle Sticks Class & Properties"""


class Candlesticks:

    def isDoji(self, frame) -> bool:
        body = abs(frame.open - frame.close)
        candle = abs(frame.high - frame.low)
        average_price = frame.high + frame.low / 2

        percentage = round(float((body/candle) * 1), 2)

        h = average_price + (frame.high - average_price) * 0.1
        l = average_price - (average_price - frame.low) * 0.1

        if frame.close > frame.open:
            if percentage <= 0.10 and h <= frame.close and l <= frame.open:
                return True

            else:
                return False

        elif frame.open > frame.close:
            if percentage <= 0.10 and h <= frame.open and l <= frame.close:
                return True

            else:
                return False

        elif frame.open == frame.close:
            if percentage <= 0.10:
                return True

            else:
                return False
        else:
            return False

        # if percentage <= 0.30 and h <= self.open and l <= self.close:
        #     return True

        # return False

    def isDragonFlyDoji(self, frame):
        body = abs(frame.open - frame.open)
        candle = abs(frame.high - frame.low)

        percentage = round(float((body/candle) * 1), 2)

        mid = (frame.high + frame.low) / 2
        h = mid + ((frame.high - mid) * 0.4)
        if percentage <= 0.1 and frame.open >= h and frame.close >= h:
            return True
        else:
            return False

    def isGravestoneDoji(self, frame):
        body = abs(frame.open - frame.open)
        candle = abs(frame.high - frame.low)

        percentage = round(float((body/candle) * 1), 2)

        mid = (frame.high + frame.low) / 2
        h = mid - ((frame.high - mid) * 0.4)
        if percentage <= 0.1 and frame.open <= h and frame.close <= h:
            return True
        else:
            return False

    def isHammer(self, frame):
        body = abs(frame.open - frame.close)
        candle = abs(frame.high - frame.low)

        percentage = round(float((body/candle) * 1), 2)

        mid = (frame.high + frame.low) / 2

        h = mid + ((frame.high - mid) * 0.3)
        if percentage > 0.10 and percentage <= 0.25 and frame.open >= h and frame.close >= h:
            return True
        else:
            return False

    def isShootingstar(self, frame):
        body = abs(frame.open - frame.close)
        candle = abs(frame.high - frame.low)

        percentage = round(float((body/candle) * 1), 2)

        mid = (frame.high + frame.low) / 2

        h = mid - ((frame.high - mid) * 0.3)
        if percentage > 0.10 and percentage <= 0.25 and frame.open <= h and frame.close <= h:
            return True
        else:
            return False

    def isSpinningTop(self, frame):

        body = abs(frame.open - frame.close)
        candle = abs(frame.high - frame.low)
        average_price = frame.high + frame.low / 2

        percentage = round(float((body/candle) * 1), 2)

        h = average_price + (frame.high - average_price) * 0.3
        l = average_price - (average_price - frame.low) * 0.3

    def isSpinningBottom(self, frame):
        pass

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

    def isBullEngulfing(self, frame):
        first = frame.iloc[-2]
        second = frame.iloc[-1]

        if second.close > first.close and self.isBullMaburuzu(second):
            return True
        else:
            return False

    def isBearEngulfing(self, frame):
        first = frame.iloc[-2]
        second = frame.iloc[-1]

        if second.close < first.close and self.isBearMaburuzu(second):
            return True
        else:
            return False

    def isBullInsideBar(self, frame):
        first = frame.iloc[-2]
        second = frame.iloc[-1]

        if second.close < first.close and self.isBearMaburuzu(first):
            return True

        else:
            return False

    def isBearInsideBar(self, frame):
        first = frame.iloc[-2]
        second = frame.iloc[-1]

        if second.close < first.close and self.isBullMaburuzu(first):
            return True

        else:
            return False

    def isMorningStar(self, frame):
        first = frame.iloc[-3]
        second = frame.iloc[-2]
        third = frame.iloc[-1]
        checksecond = self.isDoji(second) or self.isDragonFlyDoji(
            second) or self.isHammer(second)
        if self.isBullMaburuzu(first) and checksecond and self.isBearMaburuzu(third):
            return True

        else:
            return False

    def isEveningStar(self, frame):
        first = frame.iloc[-3]
        second = frame.iloc[-2]
        third = frame.iloc[-1]
        checksecond = self.isDoji(second) or self.isGravestoneDoji(
            second) or self.isShootingstar(second)
        if self.isBearMaburuzu(first) and checksecond and self.isBullMaburuzu(third):
            return True

        else:
            return False

    def isTweezerBottom(self):
        pass

    def isTweezersTop(self):
        pass
