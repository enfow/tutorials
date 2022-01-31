"""Implement strategy model.
    
Author: Kyeongmin Woo
Email: wgm0601@gmail.com
"""
import os
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict
from datetime import datetime

from model import StrategyModel
from sender.slack_sender import SlackMsgSender
from data.data_loader import Tikkers, PriceData, DataLoader, DataPreprocessor


# Constant
TIKKERS: Tikkers = {
    "KOSPI" : "069500",
    "SP500" : "143850",
    "NIKKEI" : "241180",
    "EURO" : "195930",
}
START_YEAR = 2021
DEPOSIT_RATE = 1.008


class DualMomentum(StrategyModel):
    """Dual Momentum Strategy class."""

    def __init__(self, save_dir: str, send_msg: bool = True):
        """Initialize."""
        self.channel_name = "#dual_momentum"
        self.n_days: int = 180

        StrategyModel.__init__(self, save_dir, send_msg)

    def get_data(self) -> PriceData:
        data = self.dataloader.get_opening_price(tikkers=TIKKERS)
        for name in data:
            new_data = self.preprocessors.slice_data_with_days(data[name])
            new_data = self.preprocessors.normalize(new_data)
            data[name] = new_data
        return data

    def get_msg(self) -> str:
        """get message to send."""
        yields= {name : self.data[name][-1] for name in self.data}
        msg = f"Momentum 분석: {self.today_date}\n"
        for name, y in yields.items():
            msg += f"{name} : {round(y, 3)}%\n"
        return msg

    def save_plot(self) -> str:
        """save plot."""
        plt.figure(figsize=(14, 4))
        for name, data in self.data.items():
            plt.plot(data.index, data)
        
        plt.title(f"{self.n_days} days yield at {self.today_date}")
        plt.legend([f"{name} : {round(self.data[name][-1], 2)}%" for name in TIKKERS])
        plt.grid()
        
        file_name = f"6M_yield_{self.today_date}"
        file_path = os.path.join(self.save_dir, file_name)
        plt.savefig(file_path)

        return file_path

if __name__ == "__main__":
    strategy = DualMomentum(save_dir = "img", send_msg=False)
