
f = open("experiment_170107_3_coex.txt", "r")
t= open("experiment_170107_3_coex_childcare_weekday.txt", "w")

res = {"monday":0,"tuesday":0,"wednesday":0,"thursday":0,"friday":0,"saturday":0,"sunday":0}
tot = 0;
for line in f:
    activity = line.strip().split(",")[0]
    hour = line.strip().split(",")[1]
    
    if activity=='childcare':
        res[hour] += 1
        tot += 1

    else:
        a =1
        #print activity
    
for d in res:
    print d +"\n" + str(float(res[d]/float(tot)));
 
            
            


