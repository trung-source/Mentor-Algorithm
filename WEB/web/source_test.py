
# MENTOR 2

umin = 0.85
alpha = 0.4


# Khai bao toa do mat phang 1000*10000
from os import access
from random import randint, random
from re import A
from colorama import Back
import numpy as np
import matplotlib.pyplot as plt
import math
import csv
from bokeh.plotting import figure, output_file, show


fig_size = (10, 10)
f = plt.figure()


# Ham tinh shortest path distance giua 2 nut (s: chi so nut thu nhat, d: chi so nut thu hai trong mang
# BackBone, Topo: Topology Backbone)
def hop_count(s,d,Topology_Backbone):
    if s == d:                          # Neu chi so s == d
        return 0                        # tra ve hops = 0
    else:
        n = len(Topology_Backbone)
        visited = np.zeros(n)
        parent = np.zeros(n)
        q = [s]
        visited[s] = 1
        # Tim cha cua tung nut Backbone
        while(q):
            m = q[0]
            del q[0]
            for i in range(n):
                if (Topology_Backbone[m,i] == 1 ) and (visited[i] == 0):
                    visited[i] = 1
                    parent[i] = m
                    q.append(i)


        count = 1
        j = parent[d]           # j la nut cha cua d
        while j!=s:             # Kiem tra j va s
            count = count +1
            j = parent[int(j)]           # Tim cha cua nut j roi lai quay lai vong lap while


        return count


# Tim cac nut giua 2 nut
def node_between(s,d,Topology_Backbone):
    if s == d:
        return 0
    else:
        n = len(Topology_Backbone)
        visited = np.zeros(n)
        parent = np.zeros(n)
        q = [s]
        visited[s] = 1
        # Tim cha cua tung nut Backbone
        while(q):
            m = q[0]
            del q[0]
            for i in range(n):
                if (Topology_Backbone[m,i] == 1) and (visited[i] == 0):
                    visited[i] = 1
                    parent[i] = m
                    q.append(i)

        j = parent[d]
        res = [j]
        while j!=s:
            j = parent[int(j)]
            res.append(j)
        res.pop()
        return res





# Tao 100 Node voi gia tri ngau nhien

# Node = []
# for i in range(100):
#     Node.append(randint(1,1000))

# print(Node)

# Node = [535, 934, 143, 588, 46, 218, 98, 220, 148, 185, 197, 956, 324, 611, 941, 928, 
# 306, 1000, 641, 739, 982, 369, 152, 403, 564, 795, 384, 259, 238, 966, 65, 959,  190, 
# 641, 418, 639, 416, 616, 675, 937, 910, 739, 609, 678, 928, 291, 577, 873, 8, 707, 644, 
# 729, 286, 795, 927, 321, 713, 954, 372, 257, 71, 131, 433, 339, 728, 544, 883, 297, 728, 
#  438, 417, 341, 589, 839, 924, 400, 141, 822, 997, 932, 541, 39, 936, 753, 919, 945, 543,
#   236, 429, 629, 739, 627, 765, 610, 832, 230, 470, 483, 623, 667]

# Node = [930,          45,
#          293,         647,
#          949,         885,
#          613,         218,
#          678,         512,
#          193,         118,
#          926,         364,
#          377,         937,
#           70,         645,
#           53,        923,
#          976,         767,
#          495,         972,
#          461,          73,
#          628,         211,
#           71,         500,
#          488,         888,
#          726,         972,
#          114,          32,
#          404,         166,
#          174,         509,
#          294,         918,
#          455,         630,
#          325,         906,
#          259,         204,
#          761,         808,
#          960,         743,
#          251,           9,
#          176,         889,
#          895,         911,
#          644,         154,
#          964,         433,
#          678,         230,
#          262,         858,
#          930,         214,
#          935,         851,
#          376,          21,
#          393,          48,
#          909,         966,
#          592,         732,
#           63,         680,
#          934,         905,
#          513,         624,
#          336,         704,
#          401,         229,
#          441,         605,
#          954,          62,
#           47,          68,
#          873,         403,
#          648,         758,
#          343,         711,
#          789,         809,
#          279,         823,
#          747,         835,
#           91,         960,
#          161,         793,
#          732,         624,
#          461,         399,
#           37 ,        122,
#          530,         296,
#          725 ,        614,
#          418 ,       889,
#          606,         306,
#           10,         315,
#          633,         646,
#          493,         793,
#          879,         421,
#          182,         823,
#          979,         414,
#          102,         706,
#          934,         123,
#          909,         441,
#          487,         332,
#          843,         320,
#          679,         272,
#          702,           2,
#          414,         812,
#          846,         545,
#          194,         695,
#            2,         379,
#          675,         393,
#          656,         581,
#          661,         358,
#          834,         800,
#          111,         872,
#          134,         401,
#           84,         628,
#          725,         329,
#          212,         863,
#          141,         934,
#          409,         98,
#          35,          685,
#          89,          986,
#          153,         325,
#          246 ,        587,
#          358,         123 ,
#          496,         258,
#          236,         159 ,
#          589,         357,
#          721,        456,
#          694,         321]


# Node = [211, 914, 
#         64, 56, 
#         588, 379, 
#         574, 324, 
#         20, 679, 
#         922, 801, 
#         956, 605, 
#         344, 697, 
#         768, 511, 
#         462, 709, 
#         158, 410, 
#         914, 547, 
#         980, 791, 
#         812, 196, 
#         598, 75, 
#         984, 82, 
#         196, 650, 
#         464, 185, 
#         250, 880, 
#         520, 868, 
#         359, 40, 
#         700, 204, 
#         45, 642, 
#         523, 242, 
#         948, 616, 
#         919, 313, 
#         972, 106, 
#         379, 119, 
#         85, 285, 
#         778, 108, 
#         860, 634, 
#         626, 777, 
#         45, 192, 
#         725, 118, 
#         25, 931, 
#         924, 48, 
#         414, 372, 
#         81, 957, 
#         567, 718, 
#         362, 887, 
#         962, 945, 
#         957, 214, 
#         956, 218, 
#         714, 43, 
#         943, 306, 
#         351, 309, 
#         126, 676, 
#         322, 940, 
#         270, 976, 
#         847, 401, 
#         222, 463, 
#         748, 422, 
#         464, 353, 
#         992, 574, 
#         200, 910, 
#         867, 537, 
#         40, 691, 
#         662, 764, 
#         304, 888, 
#         178, 993, 
#         115, 714, 
#         286, 680, 
#         490, 372, 
#         924, 46, 
#         710, 553, 
#         156, 568, 
#         192, 306, 
#         756, 136, 
#         521, 451, 
#         908, 246, 
#         126, 113, 
#         719, 785, 
#         479, 657, 
#         14, 961, 
#         716, 400, 
#         880, 700, 
#         6, 124, 
#         646, 899,
#         717, 385, 
#         153, 492, 
#         377, 852, 
#         172, 145, 
#         287, 668, 
#         978, 24, 
#         739, 627, 
#         609, 553, 
#         105, 848, 
#         230, 731, 
#         643, 565, 
#         200, 564]

# Tao 100 Node voi gia tri ngau nhien

# Node = []
# for i in range(180):
#     Node.append(randint(1,1000))

# print(Node)


Node = [500, 500, 
        64, 56, 
        588, 379, 
        574, 324, 
        20, 679, 
        922, 801, 
        956, 605, 
        344, 697, 
        768, 511, 
        462, 709, 
        158, 410, 
        914, 547, 
        980, 791, 
        812, 196, 
        598, 75, 
        984, 82, 
        196, 650, 
        464, 185, 
        250, 880, 
        520, 868, 
        359, 40, 
        700, 204, 
        45, 642, 
        523, 242, 
        948, 616, 
        919, 313, 
        972, 106, 
        379, 119, 
        85, 285, 
        778, 108, 
        860, 634, 
        626, 777, 
        45, 192, 
        725, 118, 
        25, 931, 
        924, 48, 
        414, 372, 
        81, 957, 
        567, 718, 
        362, 887, 
        962, 945, 
        957, 214, 
        956, 218, 
        714, 43, 
        943, 306, 
        351, 309, 
        126, 676, 
        322, 940, 
        270, 976, 
        847, 401, 
        222, 463, 
        748, 422, 
        464, 353, 
        992, 574, 
        200, 910, 
        867, 537, 
        40, 691, 
        662, 764, 
        304, 888, 
        178, 993, 
        115, 714, 
        286, 680, 
        490, 372, 
        924, 46, 
        710, 553, 
        156, 568, 
        192, 306, 
        756, 136, 
        521, 451, 
        908, 246, 
        126, 113, 
        719, 785, 
        479, 657, 
        14, 961, 
        716, 400, 
        880, 700, 
        6, 124, 
        646, 899,
        717, 385, 
        153, 492, 
        377, 852, 
        172, 145, 
        287, 668, 
        978, 24, 
        739, 627, 
        609, 553, 
        105, 848, 
        230, 731, 
        643, 565, 
        200, 564]

width = 1000
height = 1000
graph = figure(title = "Bokeh Scatter Graph",plot_width=width, plot_height=height)


def source_func(Node,Umin = 0.85,Alpha=0.4,fig=f,graph=graph):
    # Node = Node[0:180]
    # print(len(Node))
    x = 1000
    y = 1000
    CountNode = int(len(Node)/2)                     # So luong cac Node
    # print(CountNode)
    W = 2
    R = 0.3
    C = 15                              # Dung luong lien ket
    Alpha = 0.4

    # So dieu kien Traffic cho vao ban dau
    Condition = 5
    Condition_array = []


    x_node = Node[::2]                 # Lay Cot dau tien (Index chan)
    y_node = Node[1::2]                 # Lay Cot thu hai (Index le)
    # print(x_node)
    # print(y_node)
    



    for i in range(len(x_node)):
        graph.scatter(x_node[i], y_node[i],size=10,fill_color="black",marker="plus")
        graph.text(x_node[i]-10, y_node[i]-10, text=["(%s)" % str(i+1)],
       text_baseline="middle", text_align="center")
     




    # Tinh gia moi lien ket
    cost = np.zeros((len(x_node),len(x_node)))
    # print(cost)
    for i in range(len(x_node)):
        for j in range(len(x_node)):
            if i != j:
        
                cost[j,i] = np.sqrt((x_node[j]-x_node[i])**2+(y_node[j]-y_node[i])**2)

    # print(cost)

    # Khai bao tham so luu luong
    Traffic = np.zeros((len(x_node),len(x_node)))

    #  luu luong giua nut i và i+2 bang 1
    for i in range(len(x_node)-2):
        Traffic[i,i+2] += 1
        Traffic[i+2,i] += 1

    # luu luong giua nut i va i+58 bang 2
    for i in range(len(x_node)-58):
        Traffic[i,i+58] += 2
        Traffic[i+58,i] += 2

    # Luu luong giua nut i va i +62 bang 3
    for i in range(len(x_node)-62):
        Traffic[i,i+62] += 3
        Traffic[i+62,i] += 3

    # Luu luong giua nut 13 va 47 bang 18
    Traffic[12,46] += 18
    Traffic[46,12] += 18

    # Luu luong giua nut 34 va 69 bang 20
    Traffic[33,68] += 20
    Traffic[68,33] += 20

    # Luu luong giua nut 20 va 38 bang 30
    Traffic[19,37] += 30
    Traffic[37,19] += 30

    # Luu luong giua nut 45 va 29 bang 10
    Traffic[44,28] += 10
    Traffic[28,44] += 10

    #  ------------------------------------------------- TIM CAC BACK BONE DAU TIEN --------------------------
    # Tinh trong so cac Node
    Node_weight = np.ones((len(x_node)))
    for i in range(len(x_node)):
        Node_weight[i] = np.sum(Traffic[i,:])

    # print("NODE",Node_weight[46,33])
    # print("TRAFFIC",Traffic[33,46])
    Backbone_node = []
    Normalized_weight = np.zeros(len(x_node))
    for i in range(len(x_node)):
        Normalized_weight[i] = Node_weight[i]/C
        if Normalized_weight[i] >= W:
            # print("bef",Backbone_node)
            Backbone_node.append(i+1)
            # print(Backbone_node)

    # Tinh MAXCOST
    Max_cost = np.max(cost)
    # print(Max_cost)

    # Tinh ban kinh toi da
    Radius = Max_cost*R


    # Ve backbone
    for i in range(len(Backbone_node)):
        graph.scatter(x_node[Backbone_node[i]-1], y_node[Backbone_node[i]-1],size=10,fill_color="black",marker="square")
        graph.circle(x_node[Backbone_node[i]-1], y_node[Backbone_node[i]-1],fill_color=None,legend_label="Ban kinh", radius=Radius,line_color='OliveDrab')

    # ---------------------------- TIM CAC NUT TRUY NHAP UNG VOI BACK BONE -----------------------
    

    Member_node = []                        # Khoi tao mot mang rong nut truy nhap
    # Xem nut thuoc backbone nao
    root = np.zeros(CountNode)

    # Kiem tra tat ca cac nut (Kiem tra 1 nut khong phai la Backbone voi tat ca cac nut backbone)
    for i in range(1,len(x_node)+1):
        # Kiem tra nut i co nam trong tap Backbone
        if i not in Backbone_node:
            # Neu khong thi bien luu gia tri Max cost tam thoi cua node i
            minTemp = 2000
            # Duyet cac nut Backbone
            for j in range(len(Backbone_node)):
                # Kiem tra xem co nut nao nam trong Radius cua backbone khong
                if cost[i-1,Backbone_node[j]-1] <= Radius:
                    if cost[i-1,Backbone_node[j]-1] < minTemp:
                        minTemp = cost[i-1,Backbone_node[j]-1]
                        root[i-1] = Backbone_node[j]

            if root[i-1] != 0:
                Member_node.append(i)
                graph.scatter(x_node[i-1], y_node[i-1],size=10,fill_color="cyan",marker="circle")
              
                temp_x_node = [x_node[i-1]]
                temp_x_node.append(x_node[int(root[i-1])-1])

                temp_y_node = [y_node[i-1]]
                temp_y_node.append(y_node[int(root[i-1])-1])
                graph.line(temp_x_node,temp_y_node,line_color="black",line_width=0.5)

          

    # print(Member_node)

    # Cac nut chua duoc xet
    Uncheck_node = []
    for i in range(len(x_node)+1):
        if i not in Backbone_node and i not in Member_node:
            if i == 0:
                continue
            Uncheck_node.append(i)
            graph.scatter(x_node[i-1], y_node[i-1],size=10,fill_color="yellow",marker="circle")
        


    # Tim cac backbone con lai
    while(Uncheck_node):
        # Xac dinh cac nut trung tam
        # Tinh gia tri hoanh do nut trung tam xtc
        tso = 0
        mso = 0
        for i in range(len(Uncheck_node)):
            # print(tso)
            tso = tso + x_node[Uncheck_node[i]-1]*Node_weight[Uncheck_node[i]-1]
            mso = mso + Node_weight[Uncheck_node[i]-1]
        #     print(i)
        # print(Uncheck_node)

        
        x_center_of_gravity = tso/mso
        # print("y:\n",x_center_of_gravity)



        # Tinh gia tri hoanh do nut trung tam ytc
        for i in range(len(Uncheck_node)):
            tso = tso + y_node[Uncheck_node[i]-1]*Node_weight[Uncheck_node[i]-1]
            mso = mso + Node_weight[Uncheck_node[i]-1]
        
        y_center_of_gravity = tso/mso


        # print("y:\n",y_center_of_gravity)


        # Khoi tao mang luu tru gia tri max dc (subDc) va max w (subW) cua cac nut trong mang uncheck_node
        subDc = np.zeros(len(Uncheck_node))
        subW = np.zeros(len(Uncheck_node))
        
        for i in range(len(Uncheck_node)):
            # print(np.sqrt(x_node[Uncheck_node[i]-1] - x_center_of_gravity**2 + (y_node[Uncheck_node[i]-1] - y_center_of_gravity**2) ))
            # print("SUB:\n",x_node[Uncheck_node[i]-1] - x_center_of_gravity**2 )
        
            subDc[i] = np.sqrt((x_node[Uncheck_node[i]-1] - x_center_of_gravity)**2 + (y_node[Uncheck_node[i]-1] - y_center_of_gravity)**2) 
            subW[i] = Node_weight[Uncheck_node[i]-1]
        # print("SUB:\n",subDc)
    
        maxDc = np.max(subDc)
        maxW = int(np.max(subW))
        # print("MAXDC",maxDc)
        # print("MAXDC",maxW)


        merit = np.zeros(len(Uncheck_node))

        for i in range(len(Uncheck_node)):
            merit[i] = 0.5*((maxDc - subDc[i])/maxDc) + 0.5*subW[i]/maxW   # An dinh thuong cho cac nut
        # print(merit)
        
        # Chon nut co merit lon nhat lam backbone
        # m = np.where(merit == np.max(merit))
        m = np.argmax(merit)

        # print("m",m)
        n = Uncheck_node[m]
        # print(n)
        Backbone_node.append(Uncheck_node[m])
        # print(Backbone_node)
        del Uncheck_node[m]
     
        graph.scatter(x_node[n-1],y_node[n-1],size=10,fill_color="black",marker="square")
        graph.text(x_node[i]-10, y_node[i]-10, text=["(%s)" % str(i+1)],
       text_baseline="middle", text_align="center")
        graph.circle(x_node[n-1], y_node[n-1],fill_color=None,legend_label="Ban kinh", radius=Radius,line_color='OliveDrab')
        
        # Kiem tra xem cac node uncheck con lai node nao la member cua backbone moi
        temp_uncheck_node = []
        tUncheck_node = Uncheck_node
        for i in range(len(tUncheck_node)):
            # print(tUncheck_node[i])
            if cost[tUncheck_node[i]-1,n-1] <= Radius:
                root[tUncheck_node[i]-1] = n
                # print(root)
                Member_node.append(tUncheck_node[i])
                # axarr.plot(x_node[tUncheck_node[i]],y_node[tUncheck_node[i]],color='black',linewidth=0.5)
                graph.scatter(x_node[tUncheck_node[i]-1],y_node[tUncheck_node[i]-1],size=10,fill_color="cyan",marker="circle")
                
     
                temp_x_node = [x_node[tUncheck_node[i]-1]]
                temp_x_node.append(x_node[n-1])
                
                temp_y_node = [y_node[tUncheck_node[i]-1]]
                temp_y_node.append(y_node[n-1])

                # print(temp_y_node)
                graph.line(temp_x_node,temp_y_node,line_color="black",line_width=0.5)

            
                # print(Uncheck_node==tUncheck_node[i], Uncheck_node[Uncheck_node[i]==tUncheck_node[i]])
            

                if Uncheck_node[i] == tUncheck_node[i]:
                    temp_uncheck_node.append(Uncheck_node[i])
        for i in range(len(temp_uncheck_node)):
            Uncheck_node.remove(temp_uncheck_node[i])
        

        # print((Uncheck_node))


    #   them den khi nao phan loai het cac nut backbone va nut truy nhap

    # # Kiem tra nut nao la backbone thi dung Backbone_node
    # print("BackBone: ",Backbone_node)
    # # Kiem tra xem ung voi moi nut back bone co nut truy nhap nao
    # access_node = np.zeros((CountNode))
    # access_node = list(access_node)
    # for i in range(len(Backbone_node)):
    #     for j in range(len(Member_node)):
    #         if root[Member_node[j]-1] == Backbone_node[i]:
    #             print(j)


    # ------------------------------------ XAY DUNG CAY PRIM-DIJISKTRA -----------------------------
    # Tim nut trung tam

    # Tinh trong so cac nut backbone
    Backbone_weight = np.zeros(len(Backbone_node))
    for i in range(len(Backbone_node)):
        Backbone_weight[i] = Node_weight[Backbone_node[i]-1]


    # Tinh moment cac nut Backbone
    Moment = np.zeros(len(Backbone_node))
    for i in range(len(Backbone_node)):
        for j in range(len(Backbone_node)):
            if i!=j:
                Moment[i] = Moment[i] + cost[Backbone_node[i]-1,Backbone_node[j]-1]*Backbone_weight[j]
    #             print(Moment[i])

    # print(Moment)


    # Chon nut trung tam la nut co Momen nho nhat, Modify nut do thanh mau xanh
    m = np.argmin(Moment)
    Center_backbone = Backbone_node[m]
    # print(Center_backbone)
    graph.scatter(x_node[Center_backbone-1],y_node[Center_backbone-1],size=10,fill_color="lawngreen",marker="square")

   

    # Xay dung cay
    U = Center_backbone                        # U:nut backbone trung tam
    V = Backbone_node.copy()                         # V: tap tat ca cac nut backbone ke ca nut trung tam
    V.remove(U)
    # print(V)

    U = [U]
    # Tinh gia tri Prim-Dijisktra
    L = np.zeros(CountNode)                 # khoi tao L la mang chua gia cac nut
    for i in range(len(L)):
        L[i] = 999999                       # khoi tao gia mac dinh ban dau la 9999999

    d = np.zeros(CountNode)           # khoi tao d la mang gom 1 hang, CountNode cot

    while(V):                       # khi tap V van con nut thi van lap    
        node = U[len(U)-1]
        # print(node)
        for i in range(len(V)):
            if d[node-1]*Alpha + cost[node-1,V[i]-1] < L[V[i]-1]:
                L[V[i]-1] = d[node-1]*Alpha + cost[node-1,V[i]-1]
                root[V[i]-1] = node               # Thay doi nut cha
                # print(V[i]-1)
        # print(L)

        minTemp = np.argmin(L)
        # print(minTemp)
        U.append(minTemp+1)
        V.remove(minTemp+1)
        # print(U)
        # print(V)
        d[minTemp] = cost[minTemp, int(root[minTemp])-1] + d[int(root[minTemp])-1]
        L[minTemp] = 9999999

        # print("S\n",L)
        temp_x_node = [x_node[minTemp]]
        temp_x_node.append(x_node[int(root[minTemp])-1])
        
        temp_y_node = [y_node[minTemp]]
        temp_y_node.append(y_node[int(root[minTemp])-1])

        # print(temp_y_node)
      
        graph.line(temp_x_node,temp_y_node,legend_label="Prim-Dijistra",line_color="red",line_width=3)
        

    # ---------------------------------- TINH TOAN LUU LUONG SU DUNG VA THEM LIEN KET ----------------------------
    # Tinh luu luong cac nut backbone
    Traffic_Backbone = np.zeros((len(Backbone_node),len(Backbone_node)))

    for i in range((CountNode)):
        for j in range(i):
            if Traffic[i,j] != 0:
                if i+1 not in Backbone_node:                        # kiem tra i co la nut backbone khong
                    a = int(root[i])                                     # gan a bang nut backbone ma nut i thuoc ve
                else:
                    a = i+1
                if a == 0:
                    print("H\n",i, j, root[i], '\n')
                if j+1 not in Backbone_node:
                    b = int(root[j])
                else:
                    b = int(j+1)
                # print(a)
                A = [idx for idx,ele in enumerate(Backbone_node) if Backbone_node[idx] == a].pop()
                # print(A)
                B = [idx for idx,ele in enumerate(Backbone_node) if Backbone_node[idx] == b].pop()
                # print(B)
                if A!=B:
                    # luu luong giua hai nut backbone la tong luu luong giua cac nut truy nhap cua hai nut backbone do
                    Traffic_Backbone[A,B] = Traffic_Backbone[A,B] + Traffic[i,j]
                    Traffic_Backbone[B,A] = Traffic_Backbone[B,A] + Traffic[i,j]
                # print(Traffic_Backbone)
                

    # --------------------------------- Topology cua cac nut BackBone ----------------------
    # Topology cac nut backbone
    Topology_Backbone = np.zeros((len(Backbone_node),len(Backbone_node)))

    for i in range(len(Backbone_node)):
        if root[Backbone_node[i]-1] != 0:                 # neu cha cua nut backbone i khac 0 thi moi kiem tra
            A = [idx for idx,ele in enumerate(Backbone_node) if int(Backbone_node[idx]) == int(root[Backbone_node[i]-1])].pop()               # a la index cua cha nut backbone i
            # print(A)


            Topology_Backbone[A,i] = 1       # tim 1 hops 
            Topology_Backbone[i,A] = 1
            # print(Topology_Backbone)
                



    # ----------------------------- TINH SO LUONG HOPS GIUA 2 NUT BACKBONE --------------------
    Hop_Backbone = np.zeros((len(Backbone_node),len(Backbone_node)))
    for i in range(len(Backbone_node)):
        for j in range(i+1,len(Backbone_node)):
            Hop_Backbone[i,j] =  hop_count(i,j,Topology_Backbone)
            Hop_Backbone[j,i] =  hop_count(i,j,Topology_Backbone)

    tHop_Backbone = Hop_Backbone.copy()
    # gan luu luong thuc te giua cac nut backbone cho mang tTraffic_Backbone, do phia duoi thuc hien them luu luong thi mang Traffic_backbone se thay doi
    tTraffic_Backbone = Traffic_Backbone.copy()

    # ------------------------------- THEM CAC LIEN KET ----------------------------------
    maxHop = 0
    for i in range(len(Backbone_node)):
        for j in range(i+1,len(Backbone_node)):             # khong xet cac hops bang 0
            # tim cap nut co hops lon nhat de xet
            if Hop_Backbone[i,j] > maxHop:
                a = i
                b = j
                maxHop = int(Hop_Backbone[i,j])

    Hop_Backbone[a,b] = 0





    # mang luu cac thong tin sau: [nut backbone thu i , nut backbone thu j , n: so duong lien ket , U: do su dung]
    ultis = []              
    index = 0
    while maxHop > 1:
        if Traffic_Backbone[a,b] != 0:
            n = math.ceil(Traffic_Backbone[a,b]/C)
            U = Traffic_Backbone[a,b]/(n*C)
            # Them lien ket truc tiep
            if U>Umin:
                c = Backbone_node[a]
                d = Backbone_node[b]
                print("THEM LIEN KET TRUC TIEP GIUA ",c," va ",d)
                # print(c)
                temp_x_node = [x_node[c-1]]
                temp_x_node.append(x_node[d-1])
                
                temp_y_node = [y_node[c-1]]
                temp_y_node.append(y_node[d-1])

                # print(temp_y_node)
               
                graph.line(temp_x_node,temp_y_node,legend_label="Them lien ket",line_color="blue",line_width=3)


                ultis.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])
                index += 1
            
            else:
                Node_Between = node_between(a,b,Topology_Backbone)          # goi ham node between
                Homing_cost = 99999
                # print("NODE BET \n",Node_Between)



                # thuc hien lua cho nut home 
                # neu cost(n1,n3)+cost(n3,n2)<cost(n1,n4)+cost(n4,n2) chon n3
                for i in range(len(Node_Between)):
                    # print(cost[Backbone_node[a]-1,Backbone_node[int(Node_Between[i])]-1] + cost[Backbone_node[int(Node_Between[i])]-1, Backbone_node[b]-1])
                    if Homing_cost > cost[Backbone_node[a]-1,Backbone_node[int(Node_Between[i])]-1] + cost[Backbone_node[int(Node_Between[i])]-1, Backbone_node[b]-1]:
                        Homing_cost = cost[Backbone_node[a]-1,Backbone_node[int(Node_Between[i])]-1] + cost[Backbone_node[int(Node_Between[i])]-1, Backbone_node[b]-1]  #Chon nut home de homing cost nho nhat
                        h = int(Node_Between[i])             # h la index trong mang Node_Between
                        # print(Homing_cost)
                    

                # Thuc hien chuyen luu luong
                print("Chuyen luu luong giua 2 nut ",Backbone_node[a]," va ",Backbone_node[b]," ve nut home ",Backbone_node[h])
                Traffic_Backbone[a,h] = Traffic_Backbone[a,h] + Traffic_Backbone[a,b]
                Traffic_Backbone[b,h] = Traffic_Backbone[b,h] + Traffic_Backbone[a,b]
                Traffic_Backbone[h,a] = Traffic_Backbone[h,a] + Traffic_Backbone[a,b]
                Traffic_Backbone[h,b] = Traffic_Backbone[h,b] + Traffic_Backbone[a,b]

        # print(Traffic_Backbone)
        maxHop = 0
        for i in range(len(Backbone_node)):
            for j in range(i+1,len(Backbone_node)):
                if Hop_Backbone[i,j] > maxHop:
                    a = i
                    b = j
                    maxHop = Hop_Backbone[i,j]

        # dua hops giua hai nut backbone co chi so a va b  bang 0
        Hop_Backbone[a,b] = 0
        # print(Hop_Backbone)
    # print(ultis)


    # Xet 2 nut co hops bang 1 dau tien
    n = math.ceil(Traffic_Backbone[a,b]/C)
    U = Traffic_Backbone[a,b]/(n*C)
    ultis.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])
    index += 1

    # Xet 2 nut co hops bang 1 tiep theo
    for i in range(len(Backbone_node)):
        for j in range(i+1,len(Backbone_node)):
            if Hop_Backbone[i,j] == 1:
                n = math.ceil(Traffic_Backbone[i,j]/C)
                U = Traffic_Backbone[i,j]/(n*C)
                ultis.append([Backbone_node[i] ,Backbone_node[j] ,n ,U ,cost[Backbone_node[i]-1,Backbone_node[j]-1], cost[Backbone_node[i]-1,Backbone_node[j]-1]*n ])
                index += 1

    # print(index)
    # for u in ultis:
    #     print(u)
    # axarr.show()


    graph.legend.location = "top_left"

    # add a title to your legend
    graph.legend.title = "Obervations"

    # change appearance of legend text
    graph.legend.label_text_font = "times"
    graph.legend.label_text_font_style = "italic"
    graph.legend.label_text_color = "navy"

    # change border and background of legend
    graph.legend.border_line_width = 3
    graph.legend.border_line_color = "navy"
    graph.legend.border_line_alpha = 0.8
    graph.legend.background_fill_color = "navy"
    graph.legend.background_fill_alpha = 0.2
    graph.legend.click_policy = "hide"
    

    # ----------------------------------- IN CAC KET QUA RA FILE ------------------------------


    # Cac nut backbone: Backbone_node
    # name of csv file 
    filename = "WEB\web\csv\Backbone_Node.csv"
        
    # writing to csv file 
    with open(filename, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["Backbone Node"]
        # writing the fields 
        csvwriter.writerow(fields) 
        # writing the data rows 
        for val in Backbone_node:
            csvwriter.writerow([val])

    # Luu luong thuc te BackBone: tTraffic_Backbone

    # name of csv file 
    filename1 = "WEB\web\csv\Traffic_Backbone.csv"
        
    # print(tTraffic_Backbone)
    # writing to csv file 
    with open(filename1, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["Luu Luong Thuc Te BackBone"]
        # writing the fields 
        csvwriter.writerow(fields) 
        # writing the data rows 
        csvwriter.writerows(tTraffic_Backbone)

    # Trong so tung nut: Node_Between

    # name of csv file 
    filename = "WEB\web\csv\Trong_so_node.csv"

    # print(Node_weight)
    # writing to csv file 
    with open(filename, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["Trong so nut"]
        # writing the fields 
        csvwriter.writerow(fields) 
        temp_write_idx = []
        for i in range(len(Node_weight)):
            temp_write_idx.append(i+1)
        
        csvwriter.writerow(temp_write_idx)

        # writing the data rows 
        csvwriter.writerows([Node_weight])
    # in ra so duong su dung tren moi lien ket va do su dung tren tung lien ket: ultis


    # name of csv file 
    filename = "WEB\web\csv\Do_su_dung.csv"

    # print(Node_weight)
    # writing to csv file 
    with open(filename, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["So duong su dung tren moi lien ket va do su dung tren tung lien ket"]
        # writing the fields 
    # mang luu cac thong tin sau: [nut backbone thu i , nut backbone thu j , n: so duong lien ket , U: do su dung]

        header = ["BackBone 1","BackBone 2","So duong lien ket n","Do su dung u","Chi phi 1 lien ket"," Tong chi phi "]

        csvwriter.writerow(fields)
        csvwriter.writerow(header) 
    

        

        # writing the data rows 
        csvwriter.writerows(ultis)



    # Tim cac nut truy nhap ung voi backbone
    access = []
    id = 0
    for i in range(len(Backbone_node)):
        for j in range(len(Member_node)):
            if(root[Member_node[j]-1] == Backbone_node[i]):
                access.append([Backbone_node[i], Member_node[j]])
                id +=1
    print("----------------")
    for a in access:
            print(a)
    show(graph)
  
    
    return graph


def source_func_2(Node,Umin = 0.8,Alpha=0.5,fig=f,graph=graph,New_trafic = 1):

    x = 1000
    y = 1000
    # print(len(Node))
    # CountNode = 100                     # So luong cac Node
    CountNode = math.ceil(len(Node)/2  )                   # So luong cac Node

    W = 2
    R = 0.3
    C = 12                              # Dung luong lien ket
    
    # Umin = 0.85

    # So dieu kien Traffic cho vao ban dau
    Condition = 5
    Condition_array = []


    x_node = Node[::2]                 # Lay Cot dau tien (Index chan)
    y_node = Node[1::2]                 # Lay Cot thu hai (Index le)
    # print(x_node)
    # print(y_node)
       

    for i in range(len(x_node)):
        
        graph.scatter(x_node[i], y_node[i],size=10,fill_color="black",marker="plus")
        graph.text(x_node[i]-10, y_node[i]-10, text=["(%s)" % str(i+1)],
       text_baseline="middle", text_align="center")





    # Tinh gia moi lien ket
    cost = np.zeros((len(x_node),len(x_node)))
    # print(cost)
    for i in range(len(x_node)):
        for j in range(len(x_node)):
            if i != j:
        
                cost[j,i] = np.sqrt((x_node[j]-x_node[i])**2+(y_node[j]-y_node[i])**2)

    # print(cost)

    # Khai bao tham so luu luong
    Traffic = np.zeros((len(x_node),len(x_node)))

    #  luu luong giua nut i và i+2 bang 1
    for i in range(len(x_node)-2):
        Traffic[i,i+2] = 1
        Traffic[i+2,i] = 1

    # luu luong giua nut i va i+58 bang 2
    for i in range(len(x_node)-58):
        Traffic[i,i+58] += 2
        Traffic[i+58,i] += 2

    # Luu luong giua nut i va i +62 bang 3
    for i in range(len(x_node)-62):
        Traffic[i,i+62] += 3
        Traffic[i+62,i] += 3

    # Luu luong giua nut 13 va 47 bang 18
    Traffic[12,46] += 18
    Traffic[46,12] += 18

    # Luu luong giua nut 34 va 69 bang 20
    Traffic[33,68] += 20
    Traffic[68,33] += 20

    # Luu luong giua nut 20 va 38 bang 30
    Traffic[19,37] += 30
    Traffic[37,19] += 30

    # Luu luong giua nut 45 va 29 bang 10
    Traffic[44,28] += 10
    Traffic[28,44] += 10


    if New_trafic == 1:
        print("ADDING NEW TRAFFIC")
        # Luu luong giua nut 3 va 10 tang them 8
        Traffic[2,9] += 8
        Traffic[9,2] += 8

        # Luu luong giua nut 13 va 37 tang them 5
        Traffic[12,36] += 5
        Traffic[36,12] += 5

        # Luu luong giua nut 15 va 30 tang them 6
        Traffic[14,29] += 6
        Traffic[29,14] += 6

        # Luu luong giua nut 40 va 58 tang them 10
        Traffic[39,57] += 10
        Traffic[57,39] += 6




    #  ------------------------------------------------- TIM CAC BACK BONE DAU TIEN --------------------------
    # Tinh trong so cac Node
    Node_weight = np.ones((len(x_node)))
    for i in range(len(x_node)):
        Node_weight[i] = np.sum(Traffic[i,:])

    Backbone_node = []
    Normalized_weight = np.zeros(len(x_node))
    for i in range(len(x_node)):
        Normalized_weight[i] = Node_weight[i]/C
        if Normalized_weight[i] >= W:
            # print("bef",Backbone_node)
            Backbone_node.append(i+1)
            # print(Backbone_node)


    # Tinh MAXCOST
    Max_cost = np.max(cost)
    # print(Max_cost)

    # Tinh ban kinh toi da
    Radius = Max_cost*R
    


    # Ve backbone
    for i in range(len(Backbone_node)):
        graph.scatter(x_node[Backbone_node[i]-1], y_node[Backbone_node[i]-1],size=10,fill_color="black",marker="square")
        graph.circle(x_node[Backbone_node[i]-1], y_node[Backbone_node[i]-1],fill_color=None,legend_label="Ban kinh", radius=Radius,line_color='OliveDrab')
        
        # add a Circle renderer to this figure
        # graph.circle(0,0,radius=0.4,fill_color=None,line_color='OliveDrab')

    # ---------------------------- TIM CAC NUT TRUY NHAP UNG VOI BACK BONE -----------------------
    

    Member_node = []                        # Khoi tao mot mang rong nut truy nhap
    # Xem nut thuoc backbone nao
    root = np.zeros(CountNode)

    # Kiem tra tat ca cac nut (Kiem tra 1 nut khong phai la Backbone voi tat ca cac nut backbone)
    for i in range(1,len(x_node)+1):
        # print(i)
        # Kiem tra nut i co nam trong tap Backbone
        if i not in Backbone_node:
            # Neu khong thi bien luu gia tri Max cost tam thoi cua node i
            minTemp = 2000
            # Duyet cac nut Backbone
            for j in range(len(Backbone_node)):
                # Kiem tra xem co nut nao nam trong Radius cua backbone khong
                if cost[i-1,Backbone_node[j]-1] <= Radius:
                    # print(Radius)
                    if cost[i-1,Backbone_node[j]-1] < minTemp:
                        minTemp = cost[i-1,Backbone_node[j]-1]
                        # print("MIN",minTemp)
                        root[i-1] = Backbone_node[j]


            if root[i-1] != 0:
                Member_node.append(i)
             
                graph.scatter(x_node[i-1], y_node[i-1],size=10,fill_color="cyan",marker="circle")

                temp_x_node = [x_node[i-1]]
                temp_x_node.append(x_node[int(root[i-1])-1])
                # print(cost[i-1,int(root[i-1])-1])
                temp_y_node = [y_node[i-1]]
                temp_y_node.append(y_node[int(root[i-1])-1])
                graph.line(temp_x_node,temp_y_node,line_color="black",line_width=0.5)

    
    


    # print(Member_node)

    # Cac nut chua duoc xet
    Uncheck_node = []
    for i in range(len(x_node)+1):
        if i not in Backbone_node and i not in Member_node:
            if i == 0:
                continue
            Uncheck_node.append(i)
            graph.scatter(x_node[i-1], y_node[i-1],size=10,fill_color="yellow",marker="circle")

           

    # Tim cac backbone con lai
    while(Uncheck_node):
        # Xac dinh cac nut trung tam
        # Tinh gia tri hoanh do nut trung tam xtc
        tso = 0
        mso = 0
        for i in range(len(Uncheck_node)):
            # print(tso)
            tso = tso + x_node[Uncheck_node[i]-1]*Node_weight[Uncheck_node[i]-1]
            mso = mso + Node_weight[Uncheck_node[i]-1]
        #     print(i)
        # print(Uncheck_node)

        
        x_center_of_gravity = tso/mso
        # print("y:\n",x_center_of_gravity)



        # Tinh gia tri hoanh do nut trung tam ytc
        for i in range(len(Uncheck_node)):
            tso = tso + y_node[Uncheck_node[i]-1]*Node_weight[Uncheck_node[i]-1]
            mso = mso + Node_weight[Uncheck_node[i]-1]
        
        y_center_of_gravity = tso/mso


        # print("y:\n",y_center_of_gravity)


        # Khoi tao mang luu tru gia tri max dc (subDc) va max w (subW) cua cac nut trong mang uncheck_node
        subDc = np.zeros(len(Uncheck_node))
        subW = np.zeros(len(Uncheck_node))
        
        for i in range(len(Uncheck_node)):
            # print(np.sqrt(x_node[Uncheck_node[i]-1] - x_center_of_gravity**2 + (y_node[Uncheck_node[i]-1] - y_center_of_gravity**2) ))
            # print("SUB:\n",x_node[Uncheck_node[i]-1] - x_center_of_gravity**2 )
        
            subDc[i] = np.sqrt((x_node[Uncheck_node[i]-1] - x_center_of_gravity)**2 + (y_node[Uncheck_node[i]-1] - y_center_of_gravity)**2) 
            subW[i] = Node_weight[Uncheck_node[i]-1]
        # print("SUB:\n",subDc)
    
        maxDc = np.max(subDc)
        maxW = int(np.max(subW))
        # print("MAXDC",maxDc)
        # print("MAXDC",maxW)


        merit = np.zeros(len(Uncheck_node))

        for i in range(len(Uncheck_node)):
            merit[i] = 0.5*((maxDc - subDc[i])/maxDc) + 0.5*subW[i]/maxW   # An dinh thuong cho cac nut
        # print(merit)
        
        # Chon nut co merit lon nhat lam backbone
        # m = np.where(merit == np.max(merit))
        m = np.argmax(merit)

        # print("m",m)
        n = Uncheck_node[m]
        # print(n)
        Backbone_node.append(Uncheck_node[m])
        # print(Backbone_node)
        del Uncheck_node[m]

        graph.scatter(x_node[n-1],y_node[n-1],size=10,fill_color="black",marker="square")
        graph.text(x_node[i]-10, y_node[i]-10, text=["(%s)" % str(i+1)],
       text_baseline="middle", text_align="center")
        graph.circle(x_node[n-1], y_node[n-1],fill_color=None,legend_label="Ban kinh", radius=Radius,line_color='OliveDrab')

        # Kiem tra xem cac node uncheck con lai node nao la member cua backbone moi
        temp_uncheck_node = []
        tUncheck_node = Uncheck_node
        for i in range(len(tUncheck_node)):
            # print(tUncheck_node[i])
            if cost[tUncheck_node[i]-1,n-1] <= Radius:
                root[tUncheck_node[i]-1] = n
                # print(root)
                Member_node.append(tUncheck_node[i])
            
                graph.scatter(x_node[tUncheck_node[i]-1],y_node[tUncheck_node[i]-1],size=10,fill_color="cyan",marker="circle")
                
                temp_x_node = [x_node[tUncheck_node[i]-1]]
                temp_x_node.append(x_node[n-1])
                
                temp_y_node = [y_node[tUncheck_node[i]-1]]
                temp_y_node.append(y_node[n-1])

                # print(temp_y_node)
               
                # print(Uncheck_node==tUncheck_node[i], Uncheck_node[Uncheck_node[i]==tUncheck_node[i]])
                graph.line(temp_x_node,temp_y_node,line_color="black",line_width=0.5)


                if Uncheck_node[i] == tUncheck_node[i]:
                    temp_uncheck_node.append(Uncheck_node[i])
        for i in range(len(temp_uncheck_node)):
            Uncheck_node.remove(temp_uncheck_node[i])
        

        # print((Uncheck_node))


    #   them den khi nao phan loai het cac nut backbone va nut truy nhap

    # # Kiem tra nut nao la backbone thi dung Backbone_node
    # print("BackBone: ",Backbone_node)
    # # Kiem tra xem ung voi moi nut back bone co nut truy nhap nao
    # access_node = np.zeros((CountNode))
    # access_node = list(access_node)
    # for i in range(len(Backbone_node)):
    #     for j in range(len(Member_node)):
    #         if root[Member_node[j]-1] == Backbone_node[i]:
    #             print(j)


    # ------------------------------------ XAY DUNG CAY PRIM-DIJISKTRA -----------------------------
    # Tim nut trung tam

    # Tinh trong so cac nut backbone
    Backbone_weight = np.zeros(len(Backbone_node))
    for i in range(len(Backbone_node)):
        Backbone_weight[i] = Node_weight[Backbone_node[i]-1]


    # Tinh moment cac nut Backbone
    Moment = np.zeros(len(Backbone_node))
    for i in range(len(Backbone_node)):
        for j in range(len(Backbone_node)):
            if i!=j:
                Moment[i] = Moment[i] + cost[Backbone_node[i]-1,Backbone_node[j]-1]*Backbone_weight[j]
    #             print(Moment[i])

    # print(Moment)


    # Chon nut trung tam la nut co Momen nho nhat, Modify nut do thanh mau xanh
    m = np.argmin(Moment)
    Center_backbone = Backbone_node[m]
    # print(Center_backbone)

  
    graph.scatter(x_node[Center_backbone-1],y_node[Center_backbone-1],size=10,fill_color="lawngreen",marker="square")


    # Xay dung cay
    U = Center_backbone                        # U:nut backbone trung tam
    V = Backbone_node.copy()                         # V: tap tat ca cac nut backbone ke ca nut trung tam
    V.remove(U)
    # print(V)

    U = [U]
    # Tinh gia tri Prim-Dijisktra
    L = np.zeros(CountNode)                 # khoi tao L la mang chua gia cac nut
    for i in range(len(L)):
        L[i] = 999999                       # khoi tao gia mac dinh ban dau la 9999999

    d = np.zeros(CountNode)           # khoi tao d la mang gom 1 hang, CountNode cot

    while(V):                       # khi tap V van con nut thi van lap    
        node = U[len(U)-1]
        # print(node)
        for i in range(len(V)):
            if d[node-1]*Alpha + cost[node-1,V[i]-1] < L[V[i]-1]:
                L[V[i]-1] = d[node-1]*Alpha + cost[node-1,V[i]-1]
                root[V[i]-1] = node               # Thay doi nut cha
                # print(V[i]-1)
        # print(L)

        minTemp = np.argmin(L)
        # print(minTemp)
        U.append(minTemp+1)
        V.remove(minTemp+1)
        # print(U)
        # print(V)
        d[minTemp] = cost[minTemp, int(root[minTemp])-1] + d[int(root[minTemp])-1]
        L[minTemp] = 9999999

        # print("S\n",L)
        temp_x_node = [x_node[minTemp]]
        temp_x_node.append(x_node[int(root[minTemp])-1])
        
        temp_y_node = [y_node[minTemp]]
        temp_y_node.append(y_node[int(root[minTemp])-1])

        # print(temp_y_node)
 
        graph.line(temp_x_node,temp_y_node,legend_label="Prim-Dijistra",line_color="red",line_width=3)

        

    # ---------------------------------- TINH TOAN LUU LUONG SU DUNG VA THEM LIEN KET ----------------------------
    # Tinh luu luong cac nut backbone
    Traffic_Backbone = np.zeros((len(Backbone_node),len(Backbone_node)))

    for i in range((CountNode)):
        for j in range(i):
            if Traffic[i,j] != 0:
                if i+1 not in Backbone_node:                        # kiem tra i co la nut backbone khong
                    a = int(root[i])                                     # gan a bang nut backbone ma nut i thuoc ve
                else:
                    a = i+1
                if a == 0:
                    print("H\n",i, j, root[i], '\n')
                if j+1 not in Backbone_node:
                    b = int(root[j])
                else:
                    b = int(j+1)
                # print(a)
                A = [idx for idx,ele in enumerate(Backbone_node) if Backbone_node[idx] == a].pop()
                # print(A)
                B = [idx for idx,ele in enumerate(Backbone_node) if Backbone_node[idx] == b].pop()
                # print(B)
                if A!=B:
                    # luu luong giua hai nut backbone la tong luu luong giua cac nut truy nhap cua hai nut backbone do
                    Traffic_Backbone[A,B] = Traffic_Backbone[A,B] + Traffic[i,j]
                    Traffic_Backbone[B,A] = Traffic_Backbone[B,A] + Traffic[i,j]
                # print(Traffic_Backbone)
                

    # --------------------------------- Topology cua cac nut BackBone ----------------------
    # Topology cac nut backbone
    Topology_Backbone = np.zeros((len(Backbone_node),len(Backbone_node)))

    for i in range(len(Backbone_node)):
        if root[Backbone_node[i]-1] != 0:                 # neu cha cua nut backbone i khac 0 thi moi kiem tra
            A = [idx for idx,ele in enumerate(Backbone_node) if int(Backbone_node[idx]) == int(root[Backbone_node[i]-1])].pop()               # a la index cua cha nut backbone i
            # print(A)


            Topology_Backbone[A,i] = 1       # tim 1 hops 
            Topology_Backbone[i,A] = 1
            # print(Topology_Backbone)
                



    # ----------------------------- TINH SO LUONG HOPS GIUA 2 NUT BACKBONE --------------------
    Hop_Backbone = np.zeros((len(Backbone_node),len(Backbone_node)))
    for i in range(len(Backbone_node)):
        for j in range(i+1,len(Backbone_node)):
            Hop_Backbone[i,j] =  hop_count(i,j,Topology_Backbone)
            Hop_Backbone[j,i] =  hop_count(i,j,Topology_Backbone)
            # print("HOP: ",Backbone_node[i] ,Backbone_node[j], Hop_Backbone[i,j])

    tHop_Backbone = Hop_Backbone.copy()
    # gan luu luong thuc te giua cac nut backbone cho mang tTraffic_Backbone, do phia duoi thuc hien them luu luong thi mang Traffic_backbone se thay doi
    tTraffic_Backbone = Traffic_Backbone.copy()
    print("TRAFFIC \n",Traffic_Backbone)
    print("Backbone",Backbone_node)

   
    # ------------------------------- THEM CAC LIEN KET ----------------------------------

    # sp_dist = np.zeros((len(Backbone_node),len(Backbone_node)))
    sp_pred_2 = {}
    sp_dist_2 = {}


    
    old_cost = {}

    def update_list(sp_pred_2,sp_dist_2,Backbone_node,Topology_Backbone):
        for i in range(len(Backbone_node)):
            for j in range(i+1,len(Backbone_node)):             # khong xet cac hops bang 0
                Node_Between = node_between(i,j,Topology_Backbone)          # goi ham node between
                Node_Between_invert = node_between(j,i,Topology_Backbone)          # goi ham node between
                sp_dist_2.setdefault((Backbone_node[i],Backbone_node[i]),0)
                sp_dist_2.setdefault((Backbone_node[j],Backbone_node[j]),0)
                # print("BACKboNE: ",Backbone_node)
                # print(Backbone_node[i], Backbone_node[j], Node_Between_invert)
                # print(Backbone_node[j1], Backbone_node[i], Node_Between_invert)

                if len(Node_Between) >= 1:
                    # sp_dist[i,j] += cost[Backbone_node[i]-1,Backbone_node[int(Node_Between[0])]-1] + cost[Backbone_node[int(Node_Between[-1])]-1,Backbone_node[j]-1]
                    # sp_dist_2[Backbone_node[i],Backbone_node[j]] += cost[Backbone_node[i]-1,Backbone_node[int(Node_Between_invert[0])]-1] + cost[Backbone_node[int(Node_Between_invert[-1])]-1,Backbone_node[j]-1]
                    
                    sp_dist_2.setdefault((Backbone_node[i],Backbone_node[j]),cost[Backbone_node[i]-1,Backbone_node[int(Node_Between_invert[0])]-1] + cost[Backbone_node[int(Node_Between_invert[-1])]-1,Backbone_node[j]-1])
                    sp_dist_2.setdefault((Backbone_node[j],Backbone_node[i]),cost[Backbone_node[j]-1,Backbone_node[int(Node_Between[0])]-1] + cost[Backbone_node[int(Node_Between[-1])]-1,Backbone_node[i]-1])
                    sp_pred_2.setdefault((Backbone_node[i],Backbone_node[j]),Backbone_node[int(Node_Between[0])])
                    sp_pred_2.setdefault((Backbone_node[j],Backbone_node[i]),Backbone_node[int(Node_Between_invert[0])])
                    # Node_Between.pop(0)
                    # Node_Between_invert.pop(0)
                    for node in range(len(Node_Between)-1):
                        sp_pred_2.setdefault((Backbone_node[i],Backbone_node[int(Node_Between[node])]),Backbone_node[int(Node_Between[node+1])])
                        sp_pred_2.setdefault((Backbone_node[j],Backbone_node[int(Node_Between_invert[node])]),Backbone_node[int(Node_Between_invert[node+1])])
                        sp_dist_2[Backbone_node[i],Backbone_node[j]] += cost[Backbone_node[int(Node_Between_invert[node])]-1,Backbone_node[int(Node_Between_invert[node+1])]-1]
                        sp_dist_2[Backbone_node[j],Backbone_node[i]] += cost[Backbone_node[int(Node_Between[node])]-1,Backbone_node[int(Node_Between[node+1])]-1]
                        
                        
                        # print(node)
                        # print("AS: ",Backbone_node[i] ,Backbone_node[int(Node_Between[node])] ,Backbone_node[int(Node_Between[node+1])])
                        # print(Node_Between)
                    
                    
                    # print(Backbone_node[i],Backbone_node[j], sp_dist_2[Backbone_node[i],Backbone_node[j]])
                    # print(Backbone_node[j],Backbone_node[i], sp_dist_2[Backbone_node[j],Backbone_node[i]])

                    # print(cost[91,1],cost[91,11]+cost[11][1])

                    
                else:
                    sp_pred_2.setdefault((Backbone_node[i],Backbone_node[j]), Backbone_node[i])
                    sp_pred_2.setdefault((Backbone_node[j],Backbone_node[i]), Backbone_node[j])
                    sp_dist_2.setdefault((Backbone_node[i],Backbone_node[j]),cost[Backbone_node[i]-1,Backbone_node[j]-1])
                    sp_dist_2.setdefault((Backbone_node[j],Backbone_node[i]),cost[Backbone_node[j]-1,Backbone_node[i]-1])
                    old_cost.setdefault((Backbone_node[i],Backbone_node[j]),cost[Backbone_node[i]-1,Backbone_node[j]-1])
                    # old_cost.setdefault((Backbone_node[j],Backbone_node[i]),cost[Backbone_node[j]-1,Backbone_node[i]-1])
                    # print("S ",Backbone_node[i],Backbone_node[j], sp_dist_2[Backbone_node[i],Backbone_node[j]])

        # print("BACKBONE: ",Backbone_node)
        # print("S: ",sp_pred_2)
        # print("OLD: ", old_cost)
        ultis_1 = []
        for k in old_cost:
            for i in range(len(Backbone_node)):
                for j in range(i+1,len(Backbone_node)):             # khong xet cac hops bang 0
            # tim cap nut co hops lon nhat de xet
                    if Backbone_node[i] == k[0] and Backbone_node[j] == k[1]:
                        a = i
                        b = j
                        print(k[0],k[1])
                        # a = k[0]
                        # b = k[1]
                        if Traffic_Backbone[a,b]:
                            n = math.ceil(Traffic_Backbone[a,b]/C)
                            U = Traffic_Backbone[a,b]/(n*C)
                            ultis_1.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])

                    #     print(old_cost[k])
        #                     Total += float(old_cost[k]*n)
        # print("Total",Total)
        # name of csv file 
        filename = "WEB\web\csv\Do_su_dung_old.csv"

        # print(Node_weight)
        # writing to csv file 
        with open(filename, 'w', newline="") as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
            fields = ["So duong su dung tren moi lien ket va do su dung tren tung lien ket"]
            # writing the fields 
        # mang luu cac thong tin sau: [nut backbone thu i , nut backbone thu j , n: so duong lien ket , U: do su dung]

            header = ["BackBone 1","BackBone 2","So duong lien ket n","Do su dung u","Chi phi 1 lien ket"," Tong chi phi "]

            csvwriter.writerow(fields)
            csvwriter.writerow(header) 
        

            

            # writing the data rows 
            csvwriter.writerows(ultis_1)



        

        return sp_dist_2,sp_pred_2

    sp_dist,sp_pred = update_list(sp_pred_2,sp_dist_2,Backbone_node,Topology_Backbone)
    # print(sp_dist)
    # print(sp_pred.keys())
    # print(Hop_Backbone)

    maxHop = 0
    # print(Hop_Backbone)
    for i in range(len(Backbone_node)):
        for j in range(i+1,len(Backbone_node)):             # khong xet cac hops bang 0
            # tim cap nut co hops lon nhat de xet
            if Hop_Backbone[i,j] > maxHop:
                a = i
                b = j
                maxHop = int(Hop_Backbone[i,j])
            if Hop_Backbone[i,j] == maxHop:
                # Tim nut co khoang cach lon nhat de xet
                if sp_dist[Backbone_node[i],Backbone_node[j]] > sp_dist[Backbone_node[a],Backbone_node[b]]:
                    # print(maxHop)
                    # print("NEW: ", Backbone_node[i],Backbone_node[j] ,"OLD: ", Backbone_node[a],Backbone_node[b])
                    # print("TES", sp_dist[Backbone_node[i],Backbone_node[j]] , sp_dist[Backbone_node[a],Backbone_node[b]])
                    a = i
                    b = j
            # if maxHop == 4:
            #     print("-------------4------")
            #     print("NEW: ", Backbone_node[i],Backbone_node[j] ,"OLD: ", Backbone_node[a],Backbone_node[b])
            #     print("TES", sp_dist[Backbone_node[i],Backbone_node[j]] , sp_dist[Backbone_node[a],Backbone_node[b]])

                    

    Hop_Backbone[a,b] = 0
    Hop_Backbone[b,a] = 0


    
        # for i in range(len(Backbone_node)):
        #     for j in range(i+1,len(Backbone_node)):
        #         Node_Between = node_between(i,j,Topology_Backbone)          # goi ham node between
        #         Node_Between_invert = node_between(j,i,Topology_Backbone)          # goi ham node between
        #         link_cost = cost[Backbone_node[i]-1,Backbone_node[j]-1]
        #         if len(Node_Between) >= 1:
        #             for node in range(len(Node_Between)):
        #                 # print(Backbone_node[int(Node_Between[node])],Backbone_node[i])
        #                 if sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[i]] + link_cost < sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[j]]:
        #                     if Backbone_node[int(Node_Between[node])] not in s_list:
        #                         s_list.append(Backbone_node[int(Node_Between[node])])
        #                     # print("S: ",s_list)
        #                     # print(Backbone_node[int(Node_Between[node])], Backbone_node[i], Backbone_node[j])


        #                 if sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[j]] + link_cost < sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[i]]:
                            
        #                     if Backbone_node[int(Node_Between[node])] not in d_list:
        #                         d_list.append(Backbone_node[int(Node_Between[node])])
        #                     # print("D: ",d_list)
                            # print(Backbone_node[int(Node_Between[node])] , Backbone_node[i] ,Backbone_node[j])
    ultis = []              
    index = 0
    ultis_2 = []
    while maxHop >= 1:
        print("---------------------------------",Traffic_Backbone[a,b])
        if Traffic_Backbone[a,b]:
            n = math.ceil(Traffic_Backbone[a,b]/C)
            U = Traffic_Backbone[a,b]/(n*C)
            s_list = []
            d_list = []
            print("Start ",Backbone_node[a],Backbone_node[b],maxHop)
            # print(Hop_Backbone)
            Node_Between = node_between(a,b,Topology_Backbone)          # goi ham node between
            Node_Between.append(a)
            Node_Between.append(b)

            link_cost = cost[Backbone_node[a]-1,Backbone_node[b]-1]
            if len(Node_Between) >= 1:
                for node in range(len(Node_Between)):
                    # print(Backbone_node[int(Node_Between[node])],Backbone_node[i])
                    if sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[a]] + link_cost < sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[b]]:
                        
                        if Backbone_node[int(Node_Between[node])] not in s_list:
                            s_list.append(Backbone_node[int(Node_Between[node])])
                            # print("S: ",s_list)

                            print(Backbone_node[int(Node_Between[node])], Backbone_node[a], Backbone_node[b])


                    if sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[b]] + link_cost < sp_dist[Backbone_node[int(Node_Between[node])],Backbone_node[a]]:
                        
                        if Backbone_node[int(Node_Between[node])] not in d_list:
                            d_list.append(Backbone_node[int(Node_Between[node])])

                            # print("D: ",d_list)
                            print(Backbone_node[int(Node_Between[node])] , Backbone_node[b] ,Backbone_node[a])
            print("D and S list: ",s_list, d_list)
            
            maxL = {}
            for ni in s_list:
                for nj in d_list:
                    # print("TEST: ",sp_dist[ni,Backbone_node[a]] + link_cost + sp_dist[Backbone_node[b],nj], sp_dist[ni,nj])
                    if sp_dist[ni,Backbone_node[a]] + link_cost + sp_dist[Backbone_node[b],nj] < sp_dist[ni,nj]:
                        maxL[ni,nj] = sp_dist[ni,nj] - sp_dist[Backbone_node[b],nj] - sp_dist[ni,Backbone_node[a]]


            
            # tes = {(2,4):5,(3,2):3,(2,4):4,(2,2):1,(9,4):6}
            # sorted_tes = (sorted(tes.items(),reverse=True, key =
            #          lambda kv:(kv[1], kv[0]))) 
            # print(sorted_tes)
            # print(sorted_tes[1][1])
            draw = False

            sorted_maxL = (sorted(maxL.items(),reverse=True, key =
                    lambda kv:(kv[1], kv[0])))


            if len(sorted_maxL)>=1:
                
                
                if sorted_maxL[0][1] > cost[Backbone_node[a]-1,Backbone_node[b]-1]:
                    if sorted_maxL[0][1] > sp_dist[Backbone_node[a],Backbone_node[b]]:
                        print("CANT ADD DIRECT LINK: ",Backbone_node[a] ,Backbone_node[b])
                        draw = False
                    else:
                        draw = True

                        if math.ceil(sorted_maxL[0][1]) < sp_dist[Backbone_node[a],Backbone_node[b]]:
                            sp_dist[Backbone_node[a],Backbone_node[b]] = math.ceil(sorted_maxL[0][1])
                            sp_dist[Backbone_node[b],Backbone_node[a]] = math.ceil(sorted_maxL[0][1])
                        else:
                            sp_dist[Backbone_node[a],Backbone_node[b]] = (sorted_maxL[0][1] + sp_dist[Backbone_node[a],Backbone_node[b]])/2
                            sp_dist[Backbone_node[b],Backbone_node[a]] = sp_dist[Backbone_node[a],Backbone_node[b]]
                else:
                    sp_dist[Backbone_node[a],Backbone_node[b]] = cost[Backbone_node[a]-1,Backbone_node[b]-1]
                    sp_dist[Backbone_node[b],Backbone_node[a]] = cost[Backbone_node[a]-1,Backbone_node[b]-1]
                    draw = True

                
            # VE LIEN KET TRUC TIEP
            if draw == True:
                c = Backbone_node[a]
                d = Backbone_node[b]
                # n = math.ceil(Traffic_Backbone[a,b]/C)
                # U = Traffic_Backbone[a,b]/(n*C)
                NODE = node_between(a,b,Topology_Backbone)
                NODE.append(a)
                NODE.reverse()
                NODE.append(b)

                print(c,d)
                # U2 = 0
                cost_2 = {}
                total_cost_2 = 0
                for node in range(len(NODE)-1):
                    # print("NODE",Backbone_node[int(NODE[node])])
                    # if node == 0:
                    #     print("NODE",Backbone_node[int(NODE[node])])

                    #     n_temp = math.ceil(Traffic_Backbone[a,int(NODE[node])]/C)
                    #     U_temp = Traffic_Backbone[a,int(NODE[node])]/(n_temp*C)
                        
                    # elif node == len(NODE)-1:
                    #     # print(Backbone_node[int(NODE[node])])
                    # else:
                    # print("NODE22",Backbone_node[int(NODE[node])],Backbone_node[int(NODE[node+1])])

                    n_temp = math.ceil(Traffic_Backbone[int(NODE[node]),int(NODE[node+1])]/C)
                    U_temp = Traffic_Backbone[int(NODE[node]),int(NODE[node+1])]/(n_temp*C)
                    cost_2.setdefault((Backbone_node[int(NODE[node])],Backbone_node[int(NODE[node+1])]),(n_temp,cost[Backbone_node[int(NODE[node])]-1,Backbone_node[int(NODE[node+1])]-1]))

                    # U2 += U_temp
                    total_cost_2 += cost[Backbone_node[int(NODE[node])]-1,Backbone_node[int(NODE[node+1])]-1]*n_temp

                # print("COST_2: ",cost_2)
                # print("TOTAL: ",total_cost_2)


            

                print("THEM LIEN KET TRUC TIEP GIUA ",c," va ",d)
                # print(c)
                temp_x_node = [x_node[c-1]]
                temp_x_node.append(x_node[d-1])
                
                temp_y_node = [y_node[c-1]]
                temp_y_node.append(y_node[d-1])

                # print(temp_y_node)
                ultis_2.append([Backbone_node[a] ,Backbone_node[b] , total_cost_2 ])
               
                graph.line(temp_x_node,temp_y_node,legend_label="Them lien ket",line_color="blue",line_width=3)

                ultis.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])

            else:
                print("CANT ADD DIRECT LINK: ",Backbone_node[a] ,Backbone_node[b])
                print("No maxL")



            # if len(sorted_maxL)>1:
                
            #     if sorted_maxL[0][1] - sorted_maxL[1][1]>=1:
            #         D = math.ceil(sorted_maxL[1][1])
            #     else: 
            #         D = sorted_maxL[1][1]+ (sorted_maxL[0][0] - sorted_maxL[1][1])/2
            #         print("Dis les than 1", D)
            #     sp_dist[Backbone_node[a],Backbone_node[b]] = D
            #     sp_dist[Backbone_node[b],Backbone_node[a]] = D
            #     # VE LIEN KET TRUC TIEP
            #     c = Backbone_node[a]
            #     d = Backbone_node[b]
            #     print("THEM LIEN KET TRUC TIEP GIUA ",c," va ",d)
            #     # print(c)
            #     temp_x_node = [x_node[c-1]]
            #     temp_x_node.append(x_node[d-1])
                
            #     temp_y_node = [y_node[c-1]]
            #     temp_y_node.append(y_node[d-1])

            #     # print(temp_y_node)
            #     axarr.plot(temp_x_node,temp_y_node,color='blue',linewidth=3)
            #     ultis.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])

            # elif len(sorted_maxL) == 1:
            #     print("????????")
            #     print(sorted_maxL)
            #     sp_dist[Backbone_node[a],Backbone_node[b]] = sorted_maxL[0][1]-1
            #     sp_dist[Backbone_node[b],Backbone_node[a]] = sorted_maxL[0][1]-1
            #     # VE LIEN KET TRUC TIEP
            #     c = Backbone_node[a]
            #     d = Backbone_node[b]
            #     print("THEM LIEN KET TRUC TIEP GIUA ",c," va ",d)
            #     # print(c)
            #     temp_x_node = [x_node[c-1]]
            #     temp_x_node.append(x_node[d-1])
                
            #     temp_y_node = [y_node[c-1]]
            #     temp_y_node.append(y_node[d-1])

            #     # print(temp_y_node)
            #     axarr.plot(temp_x_node,temp_y_node,color='green',linewidth=3)
            #     ultis.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])


            # else:
            #     print("No maxL")



    







        maxHop = 0
        for i in range(len(Backbone_node)):
            for j in range(i+1,len(Backbone_node)):
                if Hop_Backbone[i,j] > maxHop:
                    a = i
                    b = j
                    maxHop = Hop_Backbone[i,j]
                if Hop_Backbone[i,j] == maxHop:
                    if sp_dist[Backbone_node[i],Backbone_node[j]] > sp_dist[Backbone_node[a],Backbone_node[b]]:
                        a = i
                        b = j

        # dua hops giua hai nut backbone co chi so a va b  bang 0
        Hop_Backbone[a,b] = 0
        Hop_Backbone[b,a] = 0

    



    graph.legend.location = "top_left"

    # add a title to your legend
    graph.legend.title = "Obervations"

    # change appearance of legend text
    graph.legend.label_text_font = "times"
    graph.legend.label_text_font_style = "italic"
    graph.legend.label_text_color = "navy"

    # change border and background of legend
    graph.legend.border_line_width = 3
    graph.legend.border_line_color = "navy"
    graph.legend.border_line_alpha = 0.8
    graph.legend.background_fill_color = "navy"
    graph.legend.background_fill_alpha = 0.2
    graph.legend.click_policy = "hide"

            # tim cap nut co hops lon nhat de xet
    #         if Hop_Backbone[i,j] > maxHop:
    #             a = i
    #             b = j
    #             maxHop = int(Hop_Backbone[i,j])

    #         # print(i,j,sp_dist[i,j])
    # Hop_Backbone[a,b] = 0
    









    

  
    # # mang luu cac thong tin sau: [nut backbone thu i , nut backbone thu j , n: so duong lien ket , U: do su dung]
    # ultis = []              
    # index = 0
    # while maxHop > 1:
    #     if Traffic_Backbone[a,b] != 0:

    #         # n = math.ceil(Traffic_Backbone[a,b]/C)
    #         # U = Traffic_Backbone[a,b]/(n*C)
    #         # Them lien ket truc tiep
    #         # if U>Umin:
    #             # c = Backbone_node[a]
    #             # d = Backbone_node[b]
    #             # print("THEM LIEN KET TRUC TIEP GIUA ",c," va ",d)
    #             # # print(c)
    #             # temp_x_node = [x_node[c-1]]
    #             # temp_x_node.append(x_node[d-1])
                
    #             # temp_y_node = [y_node[c-1]]
    #             # temp_y_node.append(y_node[d-1])

    #             # # print(temp_y_node)
    #             # axarr.plot(temp_x_node,temp_y_node,color='blue',linewidth=3)

    #             # ultis.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])
    #             # index += 1
            
    #         # else:
    #         Node_Between = node_between(a,b,Topology_Backbone)          # goi ham node between
    #             # Homing_cost = 99999
    #         #     # print("NODE BET \n",Node_Between)

    #         L = cost[Backbone_node[a]-1,Backbone_node[b]-1]

    #             # thuc hien lua cho nut home 
    #             # neu cost(n1,n3)+cost(n3,n2)<cost(n1,n4)+cost(n4,n2) chon n3
    #         for i in range(len(Node_Between)):
    #             # if sp_dist[i]
    #             # print(cost[Backbone_node[a]-1,Backbone_node[int(Node_Between[i])]-1] + cost[Backbone_node[int(Node_Between[i])]-1, Backbone_node[b]-1])
    #             if sp_dist > cost[Backbone_node[a]-1,Backbone_node[int(Node_Between[i])]-1] + cost[Backbone_node[int(Node_Between[i])]-1, Backbone_node[b]-1]:
    #                 Homing_cost = cost[Backbone_node[a]-1,Backbone_node[int(Node_Between[i])]-1] + cost[Backbone_node[int(Node_Between[i])]-1, Backbone_node[b]-1]  #Chon nut home de homing cost nho nhat
    #                 h = int(Node_Between[i])             # h la index trong mang Node_Between
    #                 # print(Homing_cost)
                

    #         # Thuc hien chuyen luu luong
    #         print("Chuyen luu luong giua 2 nut ",Backbone_node[a]," va ",Backbone_node[b]," ve nut home ",Backbone_node[h])
    #         Traffic_Backbone[a,h] = Traffic_Backbone[a,h] + Traffic_Backbone[a,b]
    #         Traffic_Backbone[b,h] = Traffic_Backbone[b,h] + Traffic_Backbone[a,b]
    #         Traffic_Backbone[h,a] = Traffic_Backbone[h,a] + Traffic_Backbone[a,b]
    #         Traffic_Backbone[h,b] = Traffic_Backbone[h,b] + Traffic_Backbone[a,b]

    #     # print(Traffic_Backbone)
    #     maxHop = 0
    #     for i in range(len(Backbone_node)):
    #         for j in range(i+1,len(Backbone_node)):
    #             if Hop_Backbone[i,j] > maxHop:
    #                 a = i
    #                 b = j
    #                 maxHop = Hop_Backbone[i,j]

    #     # dua hops giua hai nut backbone co chi so a va b  bang 0
    #     Hop_Backbone[a,b] = 0
    #     # print(Hop_Backbone)
    # # print(ultis)


    # # Xet 2 nut co hops bang 1 dau tien
    # n = math.ceil(Traffic_Backbone[a,b]/C)
    # U = Traffic_Backbone[a,b]/(n*C)
    # ultis.append([Backbone_node[a] ,Backbone_node[b] ,n ,U ,cost[Backbone_node[a]-1,Backbone_node[b]-1], cost[Backbone_node[a]-1,Backbone_node[b]-1]*n ])
    # index += 1

    # # Xet 2 nut co hops bang 1 tiep theo
    # for i in range(len(Backbone_node)):
    #     for j in range(i+1,len(Backbone_node)):
    #         if Hop_Backbone[i,j] == 1:
    #             n = math.ceil(Traffic_Backbone[i,j]/C)
    #             U = Traffic_Backbone[i,j]/(n*C)
    #             ultis.append([Backbone_node[i] ,Backbone_node[j] ,n ,U ,cost[Backbone_node[i]-1,Backbone_node[j]-1], cost[Backbone_node[i]-1,Backbone_node[j]-1]*n ])
    #             index += 1

    # # print(index)
    # # for u in ultis:
    # #     print(u)
    # # axarr.show()



    # # ----------------------------------- IN CAC KET QUA RA FILE ------------------------------


    # Cac nut backbone: Backbone_node
    # name of csv file 
    filename = "WEB\web\csv\Backbone_Node_2.csv"
        
    # writing to csv file 
    with open(filename, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["Backbone Node"]
        # writing the fields 
        csvwriter.writerow(fields) 
        # writing the data rows 
        for val in Backbone_node:
            csvwriter.writerow([val])

    # Luu luong thuc te BackBone: tTraffic_Backbone

    # name of csv file 
    filename1 = "WEB\web\csv\Traffic_Backbone_2.csv"
    print(Backbone_node)
        
    print(tTraffic_Backbone)
    # writing to csv file 
    with open(filename1, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["Luu Luong Thuc Te BackBone"]
        # writing the fields 
        csvwriter.writerow(fields) 
        # writing the data rows 
        csvwriter.writerows(tTraffic_Backbone)

    # Trong so tung nut: Node_Between

    # name of csv file 
    filename = "WEB\web\csv\Trong_so_node_2.csv"

    # print(Node_weight)
    # writing to csv file 
    with open(filename, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["Trong so nut"]
        # writing the fields 
        csvwriter.writerow(fields) 
        temp_write_idx = []
        for i in range(len(Node_weight)):
            temp_write_idx.append(i+1)
        
        csvwriter.writerow(temp_write_idx)

        # writing the data rows 
        csvwriter.writerows([Node_weight])
    # in ra so duong su dung tren moi lien ket va do su dung tren tung lien ket: ultis


    # name of csv file 
    filename = "WEB\web\csv\Do_su_dung_2.csv"

    # print(Node_weight)
    # writing to csv file 
    with open(filename, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["So duong su dung tren moi lien ket va do su dung tren tung lien ket"]
        # writing the fields 
    # mang luu cac thong tin sau: [nut backbone thu i , nut backbone thu j , n: so duong lien ket , U: do su dung]

        header = ["BackBone 1","BackBone 2","So duong lien ket n","Do su dung u","Chi phi 1 lien ket"," Tong chi phi "]

        csvwriter.writerow(fields)
        csvwriter.writerow(header) 
    

        

        # writing the data rows 
        csvwriter.writerows(ultis)


    filename = "WEB\web\csv\Chi_phi_cu.csv"

    with open(filename, 'w', newline="") as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        fields = ["So duong su dung tren moi lien ket va do su dung tren tung lien ket"]
        # writing the fields 
    # mang luu cac thong tin sau: [nut backbone thu i , nut backbone thu j , n: so duong lien ket , U: do su dung]

        header = ["BackBone 1","BackBone 2"," Tong chi phi "]

        csvwriter.writerow(fields)
        csvwriter.writerow(header) 
    

        

        # writing the data rows 
        csvwriter.writerows(ultis_2)




    # # Tim cac nut truy nhap ung voi backbone
    # access = []
    # id = 0
    # for i in range(len(Backbone_node)):
    #     for j in range(len(Member_node)):
    #         if(root[Member_node[j]-1] == Backbone_node[i]):
    #             access.append([Backbone_node[i], Member_node[j]])
    #             id +=1

    # axarr.show()
    # # for a in access:
    # #     print(a)
    # show(graph)
    # plt.show()
    # display legend in top left corner (default is top right corner)
   
    return graph




if __name__ == '__main__':
    # fig_size = (1000, 1000)
    # f = axarr.figure()
    source_func(Node,umin,alpha,fig=f,graph=graph)
    # source_func_2(Node,0.8,0.5,fig=f,graph=graph,New_trafic=1)

    # print("TEST",f)
    # print(ax)

  
