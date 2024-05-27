import pandas as pd
d = pd.read_csv("net.csv")

dl = d['p1'].tolist()
n = len(list(set(dl)))
ll = list(set(dl))
ll.sort(key=None, reverse=False)
print(ll, n)
print("*"*50)
for i in range(n):
    # A专利所有被引专利
    ll_1 = d[d.p1 == ll[i]]['p2'].tolist()
    # print(ll[i], ll_1)

    n4 = 0
    n1 = len(ll_1)
    for j in range(n1):
        n3 = len(set(d[d.p1 == ll[i]]['p2'].tolist()) & set(d[d.p1 == ll_1[j]]['p2'].tolist()))
        n4 = n4 + n3
    # print(n4)
    print("焦点专利:", ll[i], "总深度:", n4)
    zhibiao = [ll[i], str(n4)]
    #print(zhibiao)
    str1 = ','.join(zhibiao)
    fl = open('zongshendu.csv', 'a')
    fl.write(str1)
    fl.write('\n')