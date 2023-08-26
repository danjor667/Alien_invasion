#!/usr/bin/python3
"""
setting module
"""


class Settings():
    """
    class to manage all the game settings
    """
    def __init__(self):
        """
        doc
        """
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
