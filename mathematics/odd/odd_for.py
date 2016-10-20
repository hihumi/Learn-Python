#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def odd_for(x):
    """奇数を出力する関数。

    例えば、even_for(10) として呼び出す。
    これは、0 から (10 - 1) までの奇数を出力する。
    """

    for i in range(x):
        if i % 2 == 1:
            print(i)

if __name__ == "__main__":
    odd_for(10)