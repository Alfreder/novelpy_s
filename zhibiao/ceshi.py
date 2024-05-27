import pandas as pd

d = pd.read_csv("net.csv")
#d.columns = ['p1', 'p2']
dl = d['p1'].tolist()
n = len(list(set(dl)))
ll = list(set(dl))
ll.sort(key=None, reverse=False)

for m in range(0, n):
    print("#" * 100)

    ll_m = []
    ll_1 = d[d.p1 == ll[m]]['p2'].tolist()
    if len(ll_1) <= 1:
        ll_m.append("True")
    if len(ll_1) > 1:
        for i in range(0, len(ll_1)):
            ll_1_new = []
            for j in range(0, len(ll_1)):
                if j != i:
                    ll_1_new.append(ll_1[j])
            aa = d[d.p2 == ll_1[i]]['p1'].tolist()
            bb = ll_1_new
            aa = list(set(aa))
            bb = list(set(bb))
            if len(aa) < 1:
                ll_m.append("True")
            elif len(aa) >= 1:
                n = 0
                for item in bb:
                    if item in aa:
                        n = n + 1
                if n == 0:
                    ll_m.append("False")
                elif n != 0:
                    ll_m.append("True")
    count1 = ll_m.count("False")
    count2 = len(ll_m)
    print("焦点专利:", ll[m], "绝对宽度:", count1, "相对宽度:", count1 / count2)
    zhibiao = [ll[m], str(count1), str(count1 / count2)]
    print(zhibiao)
    str1 = ','.join(zhibiao)
    fl = open('kuandu.csv', 'a')
    fl.write(str1)
    fl.write('\n')
