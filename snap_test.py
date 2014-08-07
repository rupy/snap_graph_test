from snap import *

# サンプルから

# グラフの作成
G1 = TNGraph.New()
G1.AddNode(1)
G1.AddNode(5)
G1.AddNode(32)
G1.AddEdge(1,5)
G1.AddEdge(5,1)
G1.AddEdge(5,32)


# 有効ランダムぐらふの生成（100ノード、1000辺）
G2 = GenRndGnm(PNGraph, 100, 1000)
# ノードの列挙
for NI in G2.Nodes():
    print "node id %d with out-degree %d and in-degree %d" % (
  NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())
# 辺の列挙
for EI in G2.Edges():
    print "edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId())
# ノードによって辺を列挙する
for NI in G2.Nodes():
    for Id in NI.GetOutEdges():
        print "edge (%d %d)" % (NI.GetId(), Id)


