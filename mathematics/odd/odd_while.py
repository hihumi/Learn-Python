#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def odd_while(x):
    """奇数を出力する関数。

    例えば、odd_while(10) として呼び出す。
    これは、0から10までのうちの奇数を出力する。
    """

    counter = 0
    while counter <= x:
        if counter % 2 == 1:
            print(counter)
        counter += 1

if __name__ == "__main__":
    odd_while(10)