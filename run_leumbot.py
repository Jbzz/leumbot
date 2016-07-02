import os
import sys

from leumbot.bot import build_bot

if __name__ == "__main__":
    config_choice = os.environ.get('LEUMBOT_ENV') or 'dev'
    build_bot(config=config_choice)