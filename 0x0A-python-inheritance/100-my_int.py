#!/usr/bin/python3


class MyInt(int):
    def __init__(self, val):
        super().__init__()
        self.val = val

    def __eq__(self, num):
        if self.val == num:
            return False
        else:
            return True

    def __ne__(self, num):
        if self.val != num:
            return False
        else:
            return True
