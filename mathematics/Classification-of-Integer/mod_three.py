#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mod_three(x):
    """整数nを3で割った場合の余り0, 1, 2に分類して出力する関数。

    例えば、mod_three(20) として呼び出す。
    これは、0から20までの整数と、それを3で割った場合の余り0, 1, 2を出力する。
    """

    counter = 0
    while counter <= x:
        if counter % 3 == 0:
            print(counter, ": 余り0の整数")
        elif counter % 3 == 1:
            print(counter, ": 余り1の整数")
        elif counter % 3 == 2:
            print(counter, ": 余り2の整数")
        counter += 1

if __name__ == "__main__":
    mod_three(20)