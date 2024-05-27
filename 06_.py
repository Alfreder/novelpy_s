import json
import pickle
import time
import numpy as np

# json文件相互转化  https://blog.csdn.net/Bianca427/article/details/126134559
with open('./Data/sample/mesh_dict.json', 'rb') as f:
    mesh_dict = json.load(f)  # mesh_dict: key: pmid, value: list of mesh terms for each paper
    print('mesh_dict:', mesh_dict)
    f.close()

with open('./Data/sample/mesh_rels_dict.json', 'rb') as f2:
    mesh_rels_dict = json.load(f2)  # mesh_rels_dict: key: pmid, value: list of combinations of mesh terms for each paper
    print('mesh_rels_dict:', mesh_rels_dict)
    f2.close()
#time.sleep(600)
with open('./Data/sample/cits_dict.json', 'rb') as f3:
    cits_dict = json.load(f3)  # cits_dict: key: pmid, value: list of citing pmids for each paper
    print('cits_dict:', cits_dict)
    f3.close()
with open('./Data/sample/refs_dict.json', 'rb') as f4:
    refs_dict = json.load(f4)  # refs_dict: key: pmid, value: list of reference pmids for each paper
    print('refs_dict:', refs_dict)
    f4.close()
file = open('./Data/sample/pmid_pub_years.txt', 'r')
js = file.read()
pmid_year_dict = json.loads(js)  # pmid_year_dict: key: pmid, value: pub_year
file.close()
# 类型转换未int
pmids = list(pmid_year_dict.keys())
#pmids = list(map(int, pmids))

print('*'*100)
m_dict = {}
ED_rels = {}
focal_nodes = list(pmids)  # pmids: the pmids of papers for disruption scores calculation
pbar = focal_nodes


for node in pbar:
    print('node:', node)
    cits = cits_dict[node]
    refs = refs_dict[node]

    s_rel = mesh_rels_dict[node]  # the combinations of mesh terms in the focal paper (FP)
    n_s = len(s_rel)

    # ED_s calculation
    sj_rel = set()  # the distinct combinations of mesh terms in the references of the FP
    print('refs:', refs)
    for ref in refs:
        sj_rel.update(mesh_rels_dict[ref])
    si = s_rel - sj_rel  # new mesh relations: the combinations of mesh terms in the FP that are not in the references of the focal paper
    sj_old = s_rel & sj_rel  # old mesh relations: the combinations of mesh terms in the FP that are also in the references of the focal paper
    n_si = len(si)
    n_sj = len(sj_old)
    ED_s = round((n_si - n_sj) / n_s, 5)

    # ED_p calculation
    citing_nodes_fp = [fp_cits for fp_cits in cits]  # the pmids of citing papers of the FP
    N = 0
    m = 0
    ED_p = 0
    for c in citing_nodes_fp:
        g_rel = mesh_rels_dict[c]
        n_g = len(g_rel)
        if n_g > 0:
            N += 1
            n_gi = len((s_rel & g_rel) - sj_rel)  # knowledge elements derived exclusively from FP
            n_gj = len(s_rel & g_rel & sj_rel)  # knowledge elements derived from both the FP and its predecessors
            n_gk = len((g_rel & sj_rel) - s_rel)  # knowledge elements only derived from the FP’s predecessors
            n_gn = len(g_rel - sj_rel - s_rel)  # knowledge elements that only appear in the citing paper itself
            ED_g = round((n_gi + n_gn - n_gj - n_gk) / n_g, 5)
            ED_p += ED_g
        if len(s_rel & g_rel) > 0:
            m += 1
    m_dict[node] = m  # the weighting parameter: m

    if N == 0:
        ED_rel = 0.5 * ED_s + 0.5 * ED_p
        ED_rels[node] = ED_rel
        continue

    ED_p = round(ED_p / N, 5)
    ED_rel = 0.5 * ED_s + 0.5 * ED_p
    ED_rels[node] = ED_rel