import numpy as np
from .. import plot
from pathlib import Path
from ta.volatility import average_true_range


class Tester:

    def reinitialize(self, **kwargs):
        return Tester(*self.__originalData, **kwargs)

    def __init__(
        self, buySignal, sellSignal, initialAccountBalance=1000,
        takerFee=0.001, risk=1.0
    ):
        self.initialAccountBalance = initialAccountBalance
        self.accountBalance = self.initialAccountBalance
        self.takerFee = takerFee
        self.buySignal = buySignal
        self.sellSignal = sellSignal
        self.__originalData = [self.buySignal, self.sellSignal]
        self.risk = risk
        self.balancehistory = [self.accountBalance]
        self.balanceSetter = self.balancehistory.append
        self.inTrade = False
        self.won = 0
        self.lost = 0
        self.winLog = []; self.winLogSetter = self.winLog.append
        self.lostLog = []; self.logLogSetter = self.lostLog.append
        self.avgWinPercent = 0
        self.avgLossPercent = 0
        self.biggestWin = 0
        self.biggestLoss = 0
        self.buy_stamp = []
        self.sell_stamp = []

    def testall(self, data, nSkip=100, printLog=True, logFile=None):
        N = len(data) - nSkip
        data.columns = data.columns.str.lower()
        self.printLog = printLog
        self.logFile = logFile
        for k in np.arange(N):
            self(data.iloc[0:(k + nSkip)])
        if self.inTrade:
            self.data_temp = data
            self.sell(data)

    def __call__(self, data):
        data.columns = data.columns.str.lower()

        self.data_temp = data

        if not self.inTrade:
            if self.buySignal(data):
                self.buy(data)
        else:
            if self.sellSignal(data):
                self.sell(data)
            # elif data['low'].iloc[-1] < self.stop:
            #     self.sell(data)

    def buy(self, data):
        self.inTrade = True
        self.buy_stamp.append(
            len(data)-1
        )
        self.OPENTRADE = data['close'].iloc[-1]
        self.riskedAmount = self.risk*self.accountBalance
        self.accountBalance -= \
            (self.riskedAmount + self.riskedAmount*self.takerFee)
        # self.stop = data['low'].iloc[-1] - average_true_range(
        #     data['high'], data['low'], data['close']
        # ).iloc[-1]*2.5

    def sell(self, data):
        self.sell_stamp.append(
            len(data)-1
        )
        self.inTrade = False
        self.CLOSETRADE = data['close'].iloc[-1]
        self.winFraction = self.CLOSETRADE/self.OPENTRADE
        trade = self.winFraction*self.riskedAmount
        self.accountBalance += trade
        pnlPercent = (self.winFraction-1)*100
        winLossValue = trade - self.riskedAmount
        self.balancehistory.append(self.accountBalance)
        if pnlPercent < 0:
            self.lost += 1
            self.logLogSetter(pnlPercent)
            self.avgLossPercent = sum(self.lostLog)/len(self.lostLog)
            if pnlPercent < self.biggestLoss:
                self.biggestLoss = pnlPercent
        if pnlPercent > 0:
            self.won += 1
            self.winLogSetter(pnlPercent)
            self.avgWinPercent = sum(self.winLog)/len(self.winLog)
            if pnlPercent > self.biggestWin:
                self.biggestWin = pnlPercent
        if self.won+self.lost == 0:
            percentWins = 0
        else:
            percentWins = self.won/(self.won+self.lost)
        self.percentWinsTotal = percentWins
        self.tradeLog = \
            f'''
            openValue       : %f
            closeValue      : %f
            P/L percent     : %f
            win/loss amount : %f
            accountBalance  : %f
            no wins         : %d
            no losses       : %d
            percentWins     : %f
            avergageWinPer  : %f
            averageLossPer  : %f
            ''' % (self.OPENTRADE, self.CLOSETRADE, pnlPercent, winLossValue,
                   self.accountBalance, self.won, self.lost, percentWins,
                   self.avgWinPercent, self.avgLossPercent)

        if hasattr(self, 'tradeLog'):
            if self.printLog:
                print(self.tradeLog)
            if self.logFile is not None:
                with open(self.logFile, 'a+') as f:
                    f.write(self.tradeLog)

    def plot_trades(self, *args, **kwargs):
        p = self.buySignal.plot_candles(
            *args, **kwargs
        )
        p = plot.min(
            self.buy_stamp, self.data_temp, fig=p
        )
        p = plot.max(
            self.sell_stamp, self.data_temp, fig=p
        )
        self.axis = p
        return p

    def show(self):
        self.buySignal.show()
    
    def save(self, path, bull='bull', bear='bear'):
        path = Path(path)
        if not path.exists():
            path.mkdir(parents=True)
        self.buySignal.save(
            path/bull
        )
        self.sellSignal.save(
            path/bear
        )
