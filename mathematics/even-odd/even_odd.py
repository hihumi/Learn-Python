#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def even_odd(x):
    """偶数か奇数かを判定する関数。

    例えば、even_odd(53) として呼び出す。
    整数を2で割った余りが0なら偶数、余りが1なら奇数。
    """

    while True:
        if x % 2 == 0:
            print(x, ": even")
            break
        elif x % 2 == 1:
            print(x, ": odd")
            break
        else:
            print("予期せぬエラー")
            break

if __name__ == "__main__":
    even_odd(53)
    even_odd(26)
    even_odd(187)
    even_odd(90)
    even_odd(204)
    even_odd(319)


