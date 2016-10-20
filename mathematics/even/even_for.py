#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def even_for(x):
    """偶数を出力する関数。

    例えば、even_for(10) として呼び出す。
    これは、0 から(10 - 1) までのうちの偶数を出力する。
    """

    for i in range(x):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    even_for(10)
