"""Implement strategy model.
    
Author: Kyeongmin Woo
Email: wgm0601@gmail.com
"""
import os
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
from typing import Dict
# from datetime import datetime
import datetime

from sender.slack_sender import SlackMsgSender
from data.data_loader import PriceData, DataLoader, DataPreprocessor


class StrategyModel:
    """Strategy Model class."""

    def __init__(self, save_dir: str, send_msg: bool = True):
        """Initialize."""
        self.today: datetime = pd.to_datetime("today")
        # self.today: datetime = datetime.date.today()
        self.today_date = self.today.strftime('%y-%m-%d')

        self.dataloader = DataLoader()
        self.preprocessors = DataPreprocessor()
        self.channel_name = "#test_channel"

        self.data: PriceData = self.get_data()
        self.save_dir = save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)

        self.report(send_msg=send_msg)

    def get_data(self) -> PriceData:
        """get data for the strategy.
            
        Notes:
            - the format of the data should be Dict[str, pd.Series] (PriceData)
        """
        raise NotImplementedError("get_data")

    def get_msg(self) -> str:
        """get message for reporting."""
        raise NotImplementedError("get_msg")

    def save_plot(self) -> str:
        """save plot for reporting."""
        raise NotImplementedError("save_plot")

    def report(self, send_msg=True):
        """analyze data and send slack message."""
        msg = self.get_msg()
        file_path = self.save_plot()
        if send_msg:
            self.send_msg(msg, file_path)
            print(f"reported to channel {self.channel_name}")
        print(msg)

    def send_msg(self, text: str, file_path: str) -> None:
        """send slack message with text and file(.txt, .png, etc)."""
        if self.channel_name is None:
            raise ValueError("channel name is None")

        sender =SlackMsgSender(channel_name = self.channel_name)
        if text:
            sender.send_msg(text=text)
        if file_path:
            sender.send_file(file_path=file_path)

if __name__ == "__main__":
    strategy = StrategyModel(save_dir = "img")
    strategy.report()
