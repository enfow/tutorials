"""Implement dual momentum strategy alarm.
    
Author: Kyeongmin Woo
Email: wgm0601@gmail.com

Reference:
    - "할 수 있다! 퀀트투자", 강환국
"""
import os
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict

# Type Alias
Name = str
FullData = pd.DataFrame
OpeningPrice = pd.Series

# Constant
TIKKERS = {
    "KOSPI" : "069500",
    "SP500" : "143850",
    "NIKKEI" : "241180",
    "EURO" : "195930",
}
START_YEAR = 2021
DEPOSIT_RATE = 1.008


class DualMomentum:
    """Dual momentum class."""

    def __init__(self, save_dir: str):
        """Initialize."""
        self.today = pd.to_datetime("today")
        self.data: Dict[Name, OpeningPrice] = self.get_opening_price()
        self.save_dir = save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

    def get_opening_price(self) -> Dict[Name, OpeningPrice]:
        """get data with tikker."""
        data : Dict[Name, OpeningPrice] = {}
        for name, tikker in TIKKERS.items():
            series = fdr.DataReader(tikker, START_YEAR)["Open"]
            series = self.preprocessing(series)
            data[name] = series
        return data

    def preprocessing(self, series: pd.Series):
        """define preprocessing process."""
        series = self.from_six_month_before(series)
        series = self.normalize(series)
        return series

    def normalize(self, series: pd.Series):
        """normalize with first date data."""
        return series / series[0]

    def from_six_month_before(self, series: pd.Series):
        """slice dataframe from 6 months ago."""
        six_month_before = self.today - pd.Timedelta("180 days")
        return series.loc[six_month_before:]

    def save_plot(self):
        """save plot."""
        plt.figure(figsize=(14, 4))
        for name, data in self.data.items():
            plt.plot(data.index, data)
        
        today_date = self.today.strftime('%y%m%d')
        plt.title(f"6 months yield at {today_date}")
        plt.legend([f"{name} : {round(self.data[name][-1], 2)}%" for name in TIKKERS])
        plt.grid()
        
        file_name = f"6M_yield_{today_date}"
        file_name = os.path.join(self.save_dir, file_name)
        plt.savefig(file_name)


if __name__ == "__main__":
    strategy = DualMomentum(save_dir = "img")
    strategy.save_plot()
