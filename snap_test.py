#coding: utf-8

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


# 有効ランダムグラフの生成（100ノード、1000辺）
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


# Forest Fire modelを用いたネットワーク
G3 = GenForestFire(1000, 0.35, 0.35)
# バイナリを保存＆読み込み
FOut = TFOut("test.graph")
G3.Save(FOut)
FOut.Flush()
FIn = TFIn("test.graph")
G4 = TNGraph.Load(FIn)
# 保存してテキストファイルとして読み込む
SaveEdgeList(G4, "test.txt", "Save as tab-separated list of edges")
G5 = LoadEdgeList(PNGraph, "test.txt", 0, 1)

