import operator 

filename_prefix = "experiment_170105_3_"
 
fl = [filename_prefix+'coex.txt',
filename_prefix+'ifc.txt',
filename_prefix+'ipark.txt',
filename_prefix+'townsquare.txt']



for fn in fl:
    f = open(fn, "r")
    
    res = {}
    
    for line in f:
        st = line.strip().replace(',','-')
        if res.has_key(st):
            res[st] += 1
        else:
            res[st] =1

    f.close()
    
        
    g = open("res_"+fn, "w")
    for key in sorted(res, key=res.get, reverse=True):
        if res[key] > 400:
            g.write(key + "," + str(res[key]) + '\n')
    g.close()
    
    