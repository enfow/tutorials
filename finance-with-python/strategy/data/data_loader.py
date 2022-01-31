"""Define data loaders.
    
Author: Kyeongmin Woo
Email: wgm0601@gmail.com
"""
import pandas as pd
import FinanceDataReader as fdr
from datetime import datetime

from typing import Dict

# Type Alias
Stock = str
Tikker = str
Tikkers = Dict[Stock, Tikker]
Price = pd.Series
PriceData = Dict[Stock, Price]

# Constant
START_YEAR = 2021

class DataLoader:
    """Set of data loaders."""
    def get_opening_price(self, tikkers:Tikkers) -> PriceData:
        """get data with tikker."""
        data : PriceData = {}
        for name, tikker in tikkers.items():
            series = fdr.DataReader(tikker, START_YEAR)["Open"]
            data[name] = series
        return data

class DataPreprocessor:
    "Set of preprocessors."

    def normalize(self, series: pd.Series):
        """normalize with first date data."""
        return series / series[0]

    def slice_data_with_days(
        self,
        series: pd.Series,
        base_date: datetime = pd.to_datetime("today"),
        n_days: int = 180
    ):
        """slice data with days."""
        n_days_before = base_date - pd.Timedelta(f"{n_days} days")
        return series.loc[n_days_before:]

