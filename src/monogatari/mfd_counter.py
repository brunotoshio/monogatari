# -*- coding: utf-8 -*-
# Copyright 2019 Bruno Toshio Sugano <brunotoshio@gmail.com>
import os

from .dict_counter import DictCounter


class MFDCounter(DictCounter):
    def __init__(self):
        path = os.path.dirname(__file__)
        super().__init__(f"{path}/data/MFD.dic")
