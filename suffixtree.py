# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Node(object):
    def __init__(self,data=0,which_T=None):
        self.leaf = []
        self.data=data
        self.which_T=[]

class SuffixTree(object):
    def __init__(self):
        self.root = Node()

    def add(self,s,which_T):
        s+="$"
        for i in range(0,len(s)):
            current=self.root
            for sub in s[i:]:
                if len(current.leaf)!=0:
                    havechoose=0
                    for leafs in current.leaf:
                        if sub == leafs.data:
                            current=leafs
                            leafs.which_T.append(which_T)
                            havechoose=1
                            break
                    if havechoose==0:
                        newleaf=Node()
                        newleaf.data=sub
                        newleaf.which_T.append(which_T)
                        print newleaf.data
                        print newleaf.which_T
                        current.leaf.append(newleaf)
                        current=newleaf
                else:
                    newleaf=Node()
                    newleaf.data=sub
                    newleaf.which_T.append(which_T)
                    print newleaf.data
                    print newleaf.which_T
                    current.leaf.append(newleaf)
                    current=newleaf

def main():
    tree = SuffixTree()
    with open('t2.txt','r') as f:
        for line in f.readlines():
            print line.strip()
            s=line.strip().split(':')
            tree.add(s[1].split(','),s[0])
    while (True):
        x = raw_input("Search for: ")
        x=x.split(',')
        now=tree.root
        stop=0
        result=0
        for i in x:
            stop+=1
            for leafs in now.leaf:
                if i == leafs.data:
                    now=leafs
                    break
            if stop==len(x):
                for each in now.leaf:

                    print "find in "
                    print each.which_T
                    result+=len(each.which_T)
        print result

if __name__ == '__main__':
    main()
