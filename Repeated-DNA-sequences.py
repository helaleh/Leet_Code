import collections
    def findRepeatedDnaSequences(s):
        result= []
        dict= collections.defaultdict(int)
        for i in range(len(s)-9):
            sub= s[i:i+10]
            dict[sub]+= 1

        return [k for k,v in dict.items() if v>1]
