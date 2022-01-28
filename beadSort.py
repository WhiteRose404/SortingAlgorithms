from time import sleep,time

def cuttingoff(tab):
    for i in range(len(tab)):
        tab[i]=max(tab[i],0)

def filling(beads,tab):
    j=0
    for i in tab:
        #print(i,end=' ')
        for k in range(i):
            beads[j][k] = 1
        #print(beads[j])
        j+=1

def refillandcheack(tab,beads):
    flag = False
    #print("Start")
    for i in range(len(tab)):
        #print(i,sum(beads[i]),beads[i])
        tab[i] = sum(beads[i])
        if(i!=0 and tab[i-1]<tab[i]):
            flag = True
    #print("End")
    return flag

def algo(beads,tab,maxi):
    while(refillandcheack(tab,beads)):
        for i in range(len(tab)-1,0,-1):
            k=0
            fall = i
            while(k<maxi and beads[i][k]==1):
                while fall > 0 and beads[fall-1][k]==0: fall-=1
                if(beads[fall][k]==0):
                    beads[fall][k],beads[i][k]=beads[i][k],beads[i-1][k]
                k+=1

tab = [int(input(f"enter the {i+1} number :")) for i in range(10)]
print("addjesting the data ...")
cuttingoff(tab)
maxi = max(tab)
beads = [[0]*maxi for i in range(len(tab))]
filling(beads,tab)
start = time()
algo(beads,tab,maxi)
end = time()
print(tab,f"took around {end-start:.3f}")