"""Implement slack alarm sender.
    
Author: Kyeongmin Woo
Email: wgm0601@gmail.com

References:
    - https://github.com/slackapi/python-slack-sdk
"""

import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from sender.credentials import SLACK_TOKEN


class SlackMsgSender:
    """Slack message sender."""

    def __init__(self, channel_name: str) -> None:
        """initialize."""
        self.client = WebClient(token=SLACK_TOKEN["trade_bot"])
        self.channel_name = channel_name
        if channel_name[0] != "#":
            self.channel_name = "#" + self.channel_name

    def send_msg(self, text: str) -> None:
        """send txt slack msg."""
        response = self.client.chat_postMessage(channel=self.channel_name, text=text)
        assert response["message"]["text"] == text

    def send_file(self, file_path: str) -> None:
        """send file slack msg."""
        response = self.client.files_upload(
            channels=self.channel_name, file=file_path + ".png"
        )
        assert response["file"]
