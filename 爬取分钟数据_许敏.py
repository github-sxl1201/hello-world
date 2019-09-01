"""
爬取财经网站上面的股票分钟级数据

财经网站推荐：
腾讯财经：http://stockhtm.finance.qq.com/sstock/ggcx/000001.shtml
新浪财经：https://finance.sina.com.cn/realstock/company/sh600000/nc.shtml
东方财富网：http://www.eastmoney.com/

"""

from urllib.request import urlopen             # python自带爬虫库
from random import randint
import pandas as pd
pd.set_option('expand_frame_repr', False)      # 当列太多时不换行
pd.set_option('display.max_rows', 5000)        # 最多显示数据的行数

# =====创建随机数的函数
def _random(n=13):
    """
    创建一个n位的随机整数
    :param n:
    :return:
    """
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))


# ===构建网址
# 参数
stock_code = 'sz300124'
k_type = 1  # 1分钟的数据
num = 240   # 单次获取最多不能超过320条

# 构建url
url = 'http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=%s,m%s,,%s&_var=m%s_today&r=0.%s'
url = url % (stock_code, k_type, num, k_type, _random())

# ===获取数据
content = urlopen(url=url, timeout=15).read().decode()  # 使用python自带的库，从网络上获取信息
print(content)
