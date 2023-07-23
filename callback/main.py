# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/6/30 18:38
# Describe:
from callback.call_back import CallBackFunc

cbf = CallBackFunc()


# 主函数
def main():
    return 1, 2
    # print("调用main()函数")
    # k = 1
    # # 返回2k+1形式的奇数
    # i = cbf.getOddNumber(k, cbf.double)
    # print(f"i: {i}")
    # # 返回4k+1形式的奇数
    # i = getOddNumber(k, quadruple)
    # print(f"i: {i}")
    # # 返回8k+1形式的奇数
    # i = getOddNumber(k, lambda k: k*8)
    # print(f"i: {i}")


if __name__ == "__main__":
    q, w = main()
    print(q, w)
    print(main())
    print(type(main()))
