filename_prefix = "experiment_170105_4_"

fl = [filename_prefix+'coex.txt',
filename_prefix+'ifc.txt',
filename_prefix+'ipark.txt',
filename_prefix+'townsquare.txt']

fl = [filename_prefix+'coex.txt']


 
for fn in fl:
    placeness = ['weekday-evening-autumn-fashion&beauty']
    

    for pla in placeness: 
        t= open(fn+"_imgurls_" + pla+ ".txt", "w")
    
        f = open(fn, "r")
        
        res = {}
        
        for line in f:
            
            st = line.strip().split('_')[0]
            imgurl = line.strip().replace(line.strip().split('_')[0]+'_','')
            
            st = st.replace(',','-')
            
            if st==pla:
                t.write(imgurl + '\n')
    
    t.close()
            
            
            


