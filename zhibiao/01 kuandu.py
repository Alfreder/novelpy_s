import pandas as pd
import codecs
d = pd.read_csv("net.csv")
#d.columns = ['p1', 'p2']
print(d)

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
    # print(ll[m])
    ll_m = []
    # 获取焦点专利的所有引用的专利，组成列表
    ll_1 = d[d.p1 == ll[m]]['p2'].tolist()
    # print(ll_1, len(ll_1))

    # 如果焦点专利引用的专利数量小于等于1，直接为1
    if len(ll_1) <= 1:
        # print("True")
        ll_m.append("True")
    # 如果焦点专利引用的专利数量大于1
    if len(ll_1) > 1:
        # 循环判断引用的专利中的相互引用关系数量
        for i in range(0, len(ll_1)):
            # bb列表，删除第i个元素，组成第2列，被引用元素
            ll_1_new = []
            for j in range(0, len(ll_1)):
                if j != i:
                    ll_1_new.append(ll_1[j])

            # 获取焦点专利所引用的所有专利中，引用Ai的所有专利
            aa = d[d.p2 == ll_1[i]]['p1'].tolist()
            bb = ll_1_new
            aa = list(set(aa))
            bb = list(set(bb))

            # print(aa, bb)

            if len(aa) < 1:
                ll_m.append("True")
            # 判断aa中与bb中重复引用的数量
            elif len(aa) >= 1:
                n = 0
                for item in bb:
                    if item in aa:
                        n = n + 1
                # print(n)
                if n == 0:
                    # print("False")
                    ll_m.append("False")
                elif n != 0:
                    # print("True")
                    ll_m.append("True")
                #print("*"*30)
    # print(ll_m)
    count1 = ll_m.count("False")
    count2 = len(ll_m)

    print("焦点专利:", ll[m], "绝对宽度:", count1, "相对宽度:", count1/count2)
    zhibiao = [ll[m], str(count1), str(count1/count2)]
    print(zhibiao)
    str1 = ','.join(zhibiao)
    fl = open('kuandu.csv', 'a')
    fl.write(str1)
    fl.write('\n')