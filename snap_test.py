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

# Forest Fire modelを用いたネットワーク
G6 = GenForestFire(1000, 0.35, 0.35)
# 無向グラフに変換
G7 = ConvertGraph(PUNGraph,G6)
WccG = GetMxWcc(G6)
# {0,1,2,3,4,5}に由来するサブグラフを得る
SubG = GetSubGraph(G6, TIntV.GetV(0,1,2,3,4))
# 3-coreを得る
Core3 = GetKCore(G6, 3)
# 出次数10入次数5のノードを削除する
DelDegKNodes(G6, 10, 5)

# 1000ノード、出次数3のPreferential Attachment graphの生成
  G8 = GenPrefAttach(1000, 3)
  # 整数のペアのベクトル（size, count）
  CntV = TIntPrV()
  # 接続したコンポーネントの分布を得る(component size, count)
  GetWccSzCnt(G8, CntV)
  # 次数分布のペアを得る (degree, count)
  GetOutDegCnt(G8, CntV)
  # 浮動小数点数を得る
  EigV = TFltV()
  # グラフの隣接行列の第一固有ベクトル
  GetEigVec(G8, EigV)
  # G8の直径を得る
  GetBfsFullDiam(G8, 100)
  # G8のクラスタリング相関を得て、G8におけるトライアド（3者関係）の数を数える
  GetTriads(G8)
  GetClustCf(G8)
