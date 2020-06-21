import numpy as np


class PositionSize:

    risk_fraction = 0.01
    balance = 1000
    exposure_fraction = 0.1
    fee_fraction = 0.0001

    def __init__(
            self,
            entry_val, exit_val,
            stop_val, risk_fraction=None, exposure_fraction=None,
            balance=None, fee_fraction=None):

        self.entry = entry_val
        self.exit = exit_val
        self.stop = stop_val
        if risk_fraction is not None:
            self.risk_fraction = risk_fraction
        if exposure_fraction is not None:
            self.exposure_fraction = exposure_fraction
        if balance is not None:
            self.balance = balance
        if fee_fraction is not None:
            self.fee_fraction = fee_fraction

    @property
    def risk_to_reward(self):
        return np.abs((self.exit - self.entry)/(self.entry - self.stop))

    @property
    def fraction_to_stop(self):
        return np.abs(
            (self.stop - self.entry)/self.entry
        )

    @property
    def percent_to_stop(self):
        return self.fraction_to_stop * 100

    @property
    def fraction_to_exit(self):
        return np.abs(
            (self.exit - self.entry)/self.entry
        )

    @property
    def percent_to_exit(self):
        return self.fraction_to_exit * 100

    @property
    def risked_amount(self):
        return self.risk_fraction * self.balance

    @property
    def position_size_gross_capital(self):
        return self.risk_to_reward * self.risked_amount / self.fraction_to_exit

    @property
    def position_size_gross_asset(self):
        return self.position_size_gross_capital/self.entry

    @property
    def exposed(self):
        return self.exposure_fraction * self.balance

    @property
    def leverage(self):
        return self.position_size_gross_capital/self.exposed

    @property
    def fees(self):
        return self.fee_fraction * self.position_size_gross_capital

    def calculate_position_size(self, leverage):
        return self.position_size_gross/leverage

    def calculate_leverage(self, position_size):
        return self.position_size_gross_capital/position_size

    def print_stats(self):
        print(
            f'''
            balance : {self.balance}

            entry: {self.entry}
            exit:  {self.exit}
            stop:  {self.stop}

            R%   : {self.risk_fraction * 100} %
            RR   : {self.risk_to_reward}
            R    : {self.risked_amount}
            Lev  : {self.leverage}
            Exp %: {self.exposure_fraction * 100} %
            AMT  : {self.exposed}

            gross_capital: {self.position_size_gross_capital}
            gross_asset:   {self.position_size_gross_asset}

            fees: {self.fees}

            '''
        )


if __name__ == "__main__":
    bull = PositionSize(
        7272.41, 7024.87, 7302.16,
        balance=1000, exposure_fraction=0.1, risk_fraction=0.005
    )

    bull.print_stats()

