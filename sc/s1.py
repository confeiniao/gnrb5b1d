# -*- coding: utf-8 -*-
import time
import pywencai

youxiao = []
sss = ['3连板', '4连板']

for s in sss:
    try:
        res = pywencai.get(query=s, loop=True)
    except Exception:
        time.sleep(61)
        try:
            res = pywencai.get(query=s, loop=True)
        except Exception:
            pass
    try:
        for _, row in res.iterrows():
            try:
                youxiao.append(''.join(filter(str.isdigit, row['股票代码'])))
            except KeyError:
                pass
    except Exception:
        pass

file = '/root/workspace/sc/gp.txt'
if youxiao:
    with open(file, 'w', encoding='utf-8') as file:
        for line in youxiao:
            file.write(line + '\n')
else:
    open(file, 'w').close()