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

# Constant
TIKKER = {
    "KOSPI" : "069500",
    "SP500" : "143850",
    "NIKKEI" : "241180",
    "EURO" : "195930",
}
YEAR = 2021
DEPOSIT_RATE = 1.008


class DualMomentum:
    """Dual momentum class."""

    def __init__(self, save_dir: str):
        """Initialize."""
        self.today = pd.to_datetime("today")
        self.today_date = self.today.strftime('%y%m%d')
        self.data = {
            name : self.preprocessing(fdr.DataReader(TIKKER[name], YEAR)) for name in TIKKER.keys()
        } 
        self.save_dir = save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

    def save_plot(self):
        """save plot."""
        plt.figure(figsize=(14, 4))
        for name, data in self.data.items():
            plt.plot(data.index, data)
      
        plt.title(f"6 months yield at {self.today_date}")
        plt.legend([f"{name} : {round(self.data[name][-1], 2)}%" for name in TIKKER.keys()])
        plt.grid()
        
        file_name = f"6M_yield_{self.today_date}"
        file_name = os.path.join(self.save_dir, file_name)
        plt.savefig(file_name)

    def preprocessing(self, df: pd.DataFrame):
        """preprocess data."""
        df = self.get_open_data(df)
        df = self.from_six_month_before(df)
        df = self.normalize(df)
        return df

    def get_open_data(self, df: pd.DataFrame) -> pd.Series:
        """get open data only"""
        return df["Open"]

    def normalize(self, data: pd.Series):
        """normalize with first date data."""
        return data / data[0]

    def from_six_month_before(self, df: pd.Series):
        """slice dataframe from 6 months ago."""
        six_month_before = self.today - pd.Timedelta("180 days")
        return df.loc[six_month_before:]


if __name__ == "__main__":
    strategy = DualMomentum(save_dir = "img")
    strategy.save_plot()
