#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def even_while(x):
    """偶数を出力する関数。

    例えば、even_while(10) として呼び出す。
    これは、0から10までのうちの偶数を出力する。
    """

    counter = 0
    while counter <= x:
        if counter % 2 == 0:
            print(counter)
        counter += 1

if __name__ == "__main__":
    even_while(10)
