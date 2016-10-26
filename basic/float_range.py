#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def float_range_while(start, end, step):
    """floatで増分させる関数。

    例えば、float_range(0, 1, 0.1) を実行した場合、
    0から1まで0.10ずつ増分して出力する。
    小数点以下は、第2位までに丸めてある。
    """
    while start <= end:
        print("{0:.2f}".format(start))
        start += step

if __name__ == "__main__":
    float_range_while(0, 1, 0.1)
    print()
    float_range_while(0, 1, 0.2)
    print()
    float_range_while(-1, 1, 0.1)
    print()
    float_range_while(-1, 1, 0.2)
