'''
Created on Feb 8, 2019

@author:  
'''

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy as np
import matplotlib.pyplot as plt

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import tensorflow as tf
from skimage.transform import resize
from graphviz import Graph, render
from collections import defaultdict 
import queue as Q
class NGraph:
    def __init__(self):
        self.graph = defaultdict(dict)
        self.path = ""
        self.paths = []
        self.total  = 0
        self.pq = Q.PriorityQueue()
        
    def addEdge(self, u, v, w):
        self.graph[u][v] = w
    def visit(self):
        maxu = None
        maxf = 0
        for u in self.graph:
            #print(u)
            if u[0][0:2] != "x_":
                continue
            for v in self.graph[u]:
                if u[1]*self.graph[u][v] > maxf:
                    maxf = self.graph[u][v]
                    maxu = u
            #if maxu != None and maxu[1] < u[1]:
            #    maxu = u
            #elif maxu == None:
            #    maxu = u
        #print(maxu, "Maxu here ")
        self.findpath(maxu)
        #for u in self.graph:
        #    for v in self.graph[u]:
        #        print(u, v, self.graph[u][v])

    def dfs(self, u, path):
        pass
    def findpath(self, u):
        #print("Path ",u)
        if u == None:
            return
        l, n = u[0].split("_")
        if(l == "x"):
            l = "I"
        elif ( l == "x1"):
            l = "L1"
        elif l == "x2":
            l = "O"
        self.path += l+"N"+n + "->"
        maxv = None
        maxf = 0
        if u not in self.graph:
            return
        for v in self.graph[u]:
            if len(self.graph[v]) == 0:
                if maxv != None and maxv[1] < v[1]:
                    maxv = v
                elif maxv == None:
                    maxv = v
            for w in self.graph[v]:
                if v[1]*self.graph[v][w] > maxf:
                    print(v, w, maxf, "MAF")
                    maxf = v[1]*self.graph[v][w]
                    maxv = v
            #if maxv != None and maxv[1] < v[1]:
            #    maxv = v
            #elif maxv == None:
            #    maxv = v
        self.findpath(maxv)
    def getPath(self):
        return self.path
class NetViz:
    def __init__(self, top = 3):
        self.name = ""
        self.top = top
    def softmax(self,x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0) # only difference
    def printdummy(self):
        return "Hello"
    def getLabel(self,y):
        one = [0, 1]
        zer = [1 , 0]
        if y == 1:
            return 1
        elif y == 0:
            return 0
        elif (y == one).all():
            return 1
        else:
            return 0
    def getLabel2(self, y):
        return y[0]
    def vispredictwights(self,nm, x, y,img_rows = 28, img_cols = 28):
        w1,b1 = nm.layers[1].get_weights()
        w2,b2 = nm.layers[2].get_weights()
        W1 = np.vstack([w1])
        print(W1.shape)
        X = x.reshape(img_rows*img_cols,)
        X1 = np.dot(X,W1)
        X1 = np.add(X1, b1)
        X1[X1<0]=0
        W2 = np.vstack([w2])
        X2 = np.dot(X1,W2)
        X2 = np.add(X2,b2)
        X2 = self.softmax(X2)
        dot = Graph(format='png')
        #dot.attr(bgcolor='purple:pink', kw = "edge", style = "invis",nodesep = "0")
        dot.attr(bgcolor='purple:pink', kw = "edge", color = "yellow",nodesep = "0")
        dot.attr(kw = "graph", nodesep = "0", ranksep = "0")
        
        color = ["red","green"]
        green = ["springgreen","springgreen1","springgreen2","springgreen3","springgreen4"]
        edgep = ["springgreen","springgreen1","springgreen2","springgreen3","springgreen4"]
        edgen = ["rosybrown1", "salmon", "orange", "orangered", "red", "red3"]
        dot.node('I',"",color = "black",style = "filled",**{'width':str(.2), 'height':str(.2)})
        maxa = np.amax(X)
        maxc = np.amax(W1)
        maxd = np.amax(W2)
        print(maxa,maxc,maxd)
        A = []
        s = .2
        
        
        for i in range(X.shape[0]):
            if X[i] > 0:
                ind = int((X[i])//(maxa/4))
                #print(ind,X[i])
                c = green[ind]
                dot.node('x_'+str(i), "", color = "black",fillcolor = "black", style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x_'+str(i), "", color = "black", style  = "filled",**{'width':str(s), 'height':str(s)})
        E = []
        total = 0
        for j in range(X.shape[0]):
            total += 1
            #if X[j] > 0:
            #E.append(('I','x_'+str(j))) # May need uncommenting
            dot.edge('I','x_'+str(j), style ="invis")
            
    
        #print(len(E),total,100*len(E)/total)
        #A.append(100*len(E)/total)
        #dot.edges(E) # My need uncommenting
        for i in range(X1.shape[0]):
            if X1[i] > 0:
                ind = int((X1[i])//(maxc/4))
                c = green[ind]
                dot.node('x1_'+str(i), "", color = "black", fillcolor = "black",style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x1_'+str(i),"", color = "black", fillcolor = "black", style  = "filled",**{'width':str(s), 'height':str(s)})
    
        E1 = []
        total = 0
        print(X1.shape," Here")
        minw = 0
        maxw = -1
        indices1 = []
        
        # Getting max w phase
        for j in range(W1.shape[1]):
            for i in range(X.shape[0]):
                if True:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = W1[i][j]
                    maxw = max(maxw,w)
                    minw = min(w, minw)
                    sw = w *255
        
        for j in range(W1.shape[1]):
            for i in range(X.shape[0]):
                total += 1
                if True:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = W1[i][j]
                    sw = w *255
                    if sw <= 0:
                        ind = int(abs(sw)/((abs(minw) * 255)/5))
                        c = edgen[ind]
                        dot.edge('x_'+str(i),'x1_'+str(j), color = c)
                        indices1.append("n{}".format(ind))
                    else:
                        ind = int(sw/((maxw * 255)/4))
                        #print(ind)
                        c = edgep[ind]
                        dot.edge('x_'+str(i),'x1_'+str(j), color = c)
                        indices1.append("p{}".format(ind))
        # Adding edges
        #print(len(E1),total,100*len(E1)/total)
        print(maxw, minw, "MINMAX W")
        A.append(100*len(E1)/total)
        #dot.edges(E1) # May need uncommenting
        for i in range(X2.shape[0]):
            if X2[i] > 0:
                ind = int((X2[i])//(maxd/4))
                c = green[ind]
                dot.node('x2_'+str(i), "", color = "black", fillcolor = "black", style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x2_'+str(i), "", color = "black", fillcolor = "black",style  = "filled",**{'width':str(s), 'height':str(s)})
        E2 = []
        total = 0
        minw = 0
        maxw = -1
        for j in range(W2.shape[1]):
            for i in range(X1.shape[0]):
                if True:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = W2[i][j]
                    maxw = max(maxw,w)
                    minw = min(w, minw)
                    sw = w *255
            
        indices2 = []
        for j in range(W2.shape[1]):
            for i in range(X1.shape[0]):
                total += 1
                if True:
                    w = W2[i][j]
                    sw = w *255
                    if sw <= 0:
                        ind = int(abs(sw)/((abs(minw) * 255)/5))
                        c = edgen[ind]
                        dot.edge('x1_'+str(i),'x2_'+str(j),color = c)
                        indices2.append("n{}".format(ind))
                    else:
                        ind = int(sw/((maxw* 255)/4))
                        #print(ind)
                        c = edgep[ind]
                        dot.edge('x1_'+str(i),'x2_'+str(j),color = c)
                        indices2.append("n{}".format(ind))
    
                    #E2.append(('x1_'+str(i),'x2_'+str(j))) # To be uncommented if needed 
        #print(len(E2), total, 100*len(E2)/total)
        print(maxw, minw, "MINMAX W")
        indices1 = set(indices1)
        indices2 = set(indices2)
        print(indices1, indices2)
        A.append(100*len(E2)/total)
        #dot.edges(E2) # To be uncommented if needed 
        return dot, A
    
    
    def vispredict(self,nm, x, y,img_rows = 28, img_cols = 28, ss = 0.2):
        graph = NGraph()
        w1,b1 = nm.layers[1].get_weights()
        w2,b2 = nm.layers[2].get_weights()
        W1 = np.vstack([w1])
        #print(W1.shape)
        X = x.reshape(img_rows*img_cols,)
        X1 = np.dot(X,W1)
        X1 = np.add(X1, b1)
        X1[X1<0]=0
        W2 = np.vstack([w2])
        X2 = np.dot(X1,W2)
        X2 = np.add(X2,b2)
        X2 = self.softmax(X2)
        dot = Graph(format='png')
        s = ss
        #dot.attr(bgcolor='purple:pink', kw = "edge", style = "invis",nodesep = "0")
        dot.attr(bgcolor='purple:pink', kw = "edge", color = "yellow",nodesep = "0")
        dot.attr(kw = "graph", nodesep = "0", ranksep = "0",ordering = "out")
        
        color = ["red","green"]
        green = ["springgreen","springgreen1","springgreen2","springgreen3","springgreen4"]
        edgep = ["springgreen","springgreen1","springgreen2","springgreen3","springgreen4"]
        edgen = ["rosybrown1", "salmon", "orange", "orangered", "red", "red3"]
        dot.node('I',str(self.getLabel2(y)),color = "blue",style = "filled",**{'width':str(s), 'height':str(s)})
        maxa = np.amax(X)
        maxc = np.amax(X1)
        maxd = np.amax(X2)
        #print(maxa,maxc,maxd)
        A = []
        
        
        valdic = {}
        for i in range(X.shape[0]):
            valdic['x_'+str(i)] = X[i]
            if X[i] > 0:
                ind = int((X[i])//(maxa/4))
                #print(ind,X[i])
                c = green[ind]
                dot.node('x_'+str(i), "", color = c,fillcolor = c, style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x_'+str(i),"", color = color[0], style  = "filled",**{'width':str(s), 'height':str(s)})
        E = []
        total = 0
        for j in range(X.shape[0]):
            total += 1
            #if X[j] > 0:
            #E.append(('I','x_'+str(j))) # May need uncommenting
            dot.edge('I','x_'+str(j), style ="invis")
            
    
        #print(len(E),total,100*len(E)/total)
        #A.append(100*len(E)/total)
        #dot.edges(E) # My need uncommenting
        
        for i in range(X1.shape[0]):
            valdic['x1_'+str(i)] = X1[i]
            if X1[i] > 0:
                ind = int((X1[i])//(maxc/4))
                c = green[ind]
                dot.node('x1_'+str(i), "", color = c, fillcolor = c,style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x1_'+str(i), "", color = color[0], fillcolor = color[0], style  = "filled",**{'width':str(s), 'height':str(s)})
    
        E1 = []
        total = 0
        #print(X1.shape," Here")
        minw = 0
        maxw = -1
        indices1 = []
        
        # Getting max w phase
        for j in range(X1.shape[0]):
            for i in range(X.shape[0]):
                if X[i] > 0:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = np.multiply(W1[i][j], X[i])
                    maxw = max(maxw,w)
                    minw = min(w, minw)
                    sw = w *255
        
        for j in range(X1.shape[0]):
            for i in range(X.shape[0]):
                total += 1
                if X[i] > 0:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = np.multiply(W1[i][j], X[i])
                    graph.addEdge(('x_'+str(i),valdic['x_'+str(i)]),('x1_'+str(j),valdic['x1_'+str(j)]),w)
                    sw = w *255
                    if sw <= 0:
                        ind = int(abs(sw)/((abs(minw) * 255)/5))
                        c = edgen[ind]
                        dot.edge('x_'+str(i),'x1_'+str(j), color = c)
                        indices1.append("n{}".format(ind))
                    else:
                        ind = int(sw/((maxw * 255)/4))
                        #print(ind)
                        c = edgep[ind]
                        dot.edge('x_'+str(i),'x1_'+str(j), color = c)
                        
                        indices1.append("p{}".format(ind))
        # Adding edges
        #print(len(E1),total,100*len(E1)/total)
        #print(maxw, minw, "MINMAX W")
        A.append(100*len(E1)/total)
        #dot.edges(E1) # May need uncommenting
        nodes_print = []
        d = 0
        for i in range(X2.shape[0]):
            valdic['x2_'+str(i)] = X2[i]
            nodes_print.append(X2[i])
            if X2[i] > 0:
                ind = int((X2[i])//(maxd/4))
                c = green[ind]
                
                d = d + 1
                dot.node('x2_'+str(i), "", color = c, fillcolor = c, style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x2_'+str(i), "", color = color[0], fillcolor = color[0],style  = "filled",**{'width':str(s), 'height':str(s)})
        E2 = []
        total = 0
        minw = 0
        maxw = -1
        for j in range(X2.shape[0]):
            for i in range(X1.shape[0]):
                if X1[i] > 0:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = np.multiply(W2[i][j], X1[i])
                    maxw = max(maxw,w)
                    minw = min(w, minw)
                    sw = w *255
            
        indices2 = []
        
        for j in range(X2.shape[0]):
            for i in range(X1.shape[0]):
                total += 1
                if X1[i] > 0:
                    w = np.multiply(W2[i][j], X1[i])
                    sw = w *255
                    graph.addEdge(('x1_'+str(i),valdic['x1_'+str(i)]),('x2_'+str(j),valdic['x2_'+str(j)]),w)
                    if sw <= 0:
                        ind = int(abs(sw)/((abs(minw) * 255)/5))
                        c = edgen[ind]
                        dot.edge('x1_'+str(i),'x2_'+str(j),color = c)
                        indices2.append("n{}".format(ind))
                    else:
                        ind = int(sw/((maxw* 255)/4))
                        #print(ind)
                        c = edgep[ind]
                        dot.edge('x1_'+str(i),'x2_'+str(j),color = c)
                        indices2.append("n{}".format(ind))
    
                    #E2.append(('x1_'+str(i),'x2_'+str(j))) # To be uncommented if needed 
        #print(len(E2), total, 100*len(E2)/total)
        #print(maxw, minw, "MINMAX W")
        indices1 = set(indices1)
        indices2 = set(indices2)
        #print(indices1, indices2)
        A.append(100*len(E2)/total)
        #dot.edges(E2) # To be uncommented if needed 
        nodesmax = [] 
        for n in nodes_print:
            nodesmax.append(n)
        nodesmax.sort()
        #print(nodesmax)
        k = 0 
        indiceskept = []
        for i in range(0, len(nodesmax) - self.top - 1):
            k = k + 1
            for j in range(0, len(nodes_print)):
                if  nodes_print[j] == nodesmax[i]:
                    nodes_print[j] = 0
        #print(k, "nodes removed")
        d = 0
        for n in nodes_print:
            #print("Digit  {0}, prob = {1}".format(d, n))
            d = d + 1
        return dot, A, graph, nodes_print
    
    
    def vispredictwithlabel(self, nm, x, y,img_rows = 28, img_cols = 28):
        w1,b1 = nm.layers[1].get_weights()
        w2,b2 = nm.layers[2].get_weights()
        W1 = np.vstack([w1])
        print(W1.shape)
        X = x.reshape(img_rows*img_cols,)
        X1 = np.dot(X,W1)
        X1 = np.add(X1, b1)
        X1[X1<0]= 0
        W2 = np.vstack([w2])
        X2 = np.dot(X1,W2)
        X2 = np.add(X2,b2)
        X2 = self.softmax(X2)
        dot = Graph(format='png')
        #dot.attr(bgcolor='purple:pink', kw = "edge", style = "invis",nodesep = "0")
        dot.attr(bgcolor='purple:pink', kw = "edge", color = "yellow",nodesep = "0",rankdir = "LR")
        dot.attr(kw = "graph", nodesep = "0", ranksep = "0",ordering = "out")
        dot.attr(kw = "node",rankdir = "LR")
        color = ["red","green"]
        green = ["springgreen","springgreen1","springgreen2","springgreen3","springgreen4"]
        edgep = ["springgreen","springgreen1","springgreen2","springgreen3","springgreen4"]
        edgen = ["rosybrown1", "salmon", "orange", "orangered", "red", "red3"]
        dot.node('I',str(self.getLabel2(y)),color = "blue",style = "filled",**{'width':str(.2), 'height':str(.2)})
        maxa = np.amax(X)
        maxc = np.amax(X1)
        maxd = np.amax(X2)
        print(maxa,maxc,maxd)
        A = []
        s = .2
        
        
        for i in range(X.shape[0]):
            if X[i] > 0:
                ind = int((X[i])//(maxa/4))
                #print(ind,X[i])
                c = green[ind]
                dot.node('x_'+str(i), str(X[i]), color = c,fillcolor = c, style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x_'+str(i), str(X[i]), color = color[0], style  = "filled",**{'width':str(s), 'height':str(s)})
        E = []
        total = 0
        for j in range(X.shape[0]):
            total += 1
            #if X[j] > 0:
            #E.append(('I','x_'+str(j))) # May need uncommenting
            dot.edge('I','x_'+str(j), style ="invis")
            
    
        #print(len(E),total,100*len(E)/total)
        #A.append(100*len(E)/total)
        #dot.edges(E) # My need uncommenting
        for i in range(X1.shape[0]):
            if X1[i] > 0:
                ind = int((X1[i])//(maxc/4))
                c = green[ind]
                dot.node('x1_'+str(i), str(X1[i]), color = c, fillcolor = c,style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x1_'+str(i), str(X1[i]), color = color[0], fillcolor = color[0], style  = "filled",**{'width':str(s), 'height':str(s)})
    
        E1 = []
        total = 0
        print(X1.shape," Here")
        minw = 0
        maxw = -1
        indices1 = []
        
        # Getting max w phase
        for j in range(X1.shape[0]):
            for i in range(X.shape[0]):
                if X[i] > 0:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = np.multiply(W1[i][j], X[i])
                    maxw = max(maxw,w)
                    minw = min(w, minw)
                    sw = w *255
        
        for j in range(X1.shape[0]):
            for i in range(X.shape[0]):
                total += 1
                if X[i] > 0:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = np.multiply(W1[i][j], X[i])
                    sw = w *255
                    if sw <= 0:
                        ind = int(abs(sw)/((abs(minw) * 255)/5))
                        c = edgen[ind]
                        dot.edge('x_'+str(i),'x1_'+str(j), color = c)
                        indices1.append("n{}".format(ind))
                    else:
                        ind = int(sw/((maxw * 255)/4))
                        #print(ind)
                        c = edgep[ind]
                        dot.edge('x_'+str(i),'x1_'+str(j), color = c)
                        indices1.append("p{}".format(ind))
        # Adding edges
        #print(len(E1),total,100*len(E1)/total)
        print(maxw, minw, "MINMAX W")
        A.append(100*len(E1)/total)
        #dot.edges(E1) # May need uncommenting
        print("X1", X1)
        print("X2", X2)
        for i in range(X2.shape[0]):
            if X2[i] > 0:
                ind = int((X2[i])//(maxd/4))
                c = green[ind]
                dot.node('x2_'+str(i), str(X2[i]), color = c, fillcolor = c, style  = "filled",**{'width':str(s), 'height':str(s)})
            else :
                dot.node('x2_'+str(i), str(X2[i]), color = color[0], fillcolor = color[0],style  = "filled",**{'width':str(s), 'height':str(s)})
        E2 = []
        total = 0
        minw = 0
        maxw = -1
        for j in range(X2.shape[0]):
            for i in range(X1.shape[0]):
                if X1[i] > 0:
                    #E1.append(('x_'+str(i),'x1_'+str(j))) # May need uncommenting
                    w = np.multiply(W2[i][j], X1[i])
                    maxw = max(maxw,w)
                    minw = min(w, minw)
                    sw = w *255
            
        indices2 = []
        for j in range(X2.shape[0]):
            for i in range(X1.shape[0]):
                total += 1
                if X1[i] > 0:
                    w = np.multiply(W2[i][j], X1[i])
                    sw = w *255
                    if sw <= 0:
                        ind = int(abs(sw)/((abs(minw) * 255)/5))
                        c = edgen[ind]
                        dot.edge('x1_'+str(i),'x2_'+str(j),color = c)
                        indices2.append("n{}".format(ind))
                    else:
                        ind = int(sw/((maxw* 255)/4))
                        #print(ind)
                        c = edgep[ind]
                        dot.edge('x1_'+str(i),'x2_'+str(j),color = c)
                        indices2.append("n{}".format(ind))
    
                    #E2.append(('x1_'+str(i),'x2_'+str(j))) # To be uncommented if needed 
        #print(len(E2), total, 100*len(E2)/total)
        print(maxw, minw, "MINMAX W")
        indices1 = set(indices1)
        indices2 = set(indices2)
        print(indices1, indices2)
        A.append(100*len(E2)/total)
        #dot.edges(E2) # To be uncommented if needed 
        return dot, A
