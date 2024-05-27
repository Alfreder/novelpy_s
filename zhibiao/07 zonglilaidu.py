import pandas as pd
import time
d = pd.read_csv("net1.csv")
# print(d)

# 获取焦点专利，转化为列表
dl = d['p1'].tolist()
# 焦点专利去重求长度
n = len(list(set(dl)))
# 焦点专利去重转化为列表
ll = list(set(dl))
# 打印焦点专利去重列表、长度
# print(ll, n)
#
# 焦点专利去重后排序
ll.sort(key=None, reverse=False)
# print(ll)

for m in range(0, n):
    print("#"*100)
    # 打印第m个焦点专利
    print(ll[m])

    # 获取焦点专利的所有引用的专利，组成列表,被引
    ll_1 = d[d.p1 == ll[m]]['p2'].tolist()
    print(ll_1, len(ll_1))
    # 获取焦点专利，引用的所有专利，引
    ll_2 = d[d.p2 == ll[m]]['p1'].tolist()
    print(ll_2, len(ll_2))
    print('*'*20)

    g = 0
    for item in ll_1:
        ll_m = []

        ll_3 = d[d.p2 == item]['p1'].tolist()
        # print(item, ll_3)
        for item1 in ll_3:
            if item1 in ll_2:
                #print("False")
                ll_m.append("True")
            else:
                #print("True")
                ll_m.append("False")
        n = ll_m.count("True")
        g = g + n
        print(item, ll_3, ll_m, n)
    print("焦点专利:", ll[m], "总依赖度:", g)
    zhibiao = [ll[m], str(g)]
    print(zhibiao)
    str1 = ','.join(zhibiao)
    fl = open('zonglilaidu.csv', 'a')
    fl.write(str1)
    fl.write('\n')
