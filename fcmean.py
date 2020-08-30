import random
import matplotlib.pyplot as plt
def fcmean(c,it,data):
    f = 0
    it1 = 0
    tempd = data
    U0 = []
    I = []
    list = []
    m = len(tempd[0])
    mp = 2
    eps = 0.01
    for x in range(c):
        list.append(x)
    for z in range(c,len(data)):
        z = random.randrange(0,c,1);
        list.append(z)
    random.shuffle(list)
    #print(list)
   # list = [0,0,0,1]

    for x2 in range(c):
        temp = []
        for x1 in range(len(data)):
            if (list[x1] == x2):
                temp.append(1)
            else :
                temp.append(0)
        U0.append(temp)
  #  print(U0)
    for iteration in range(it):
        v = []
        for i in range(c):
            tmp = []
            for j in range(m):
                sum = 0.0
                sum2= 0.0
                for t in range(len(data)):
                    pw =(pow(U0[i][t],mp))
                    sum =  sum + (tempd[t][j]* pw)
                    sum2 = sum2 + (pow(U0[i][t],mp))
                vt = sum/sum2
                tmp.append(vt)
            v.append(tmp)
     #   print(v)
        d = []
        I0 = []
        for i in range(c):
            tmp = []
            tmp2 = []
            for k in range(len(data)):
                sum = 0.0
                for j in range(m):
                    sum = sum + pow((tempd[k][j] - v[i][j]),2)
                sum = pow(sum,0.5)
                tmp.append(sum)
                if (sum == 0):
                    tmp2.append(1)
                else :
                    tmp2.append(0)
            I0.append(tmp2)
            d.append(tmp)
      #  print(d)
      #  print(I0)
        U1 = []
        for i in range(c):
            tmp = []
            for k in range(len(data)):
                sum = 0.0
                l = 0
                for j in range(c):
                    if (d[j][k]==0):
                        if (I0[i][k] == 0):
                             tmp.append(0)
                        else:
                            t=0
                            for x in range(c):
                                if (I0[x][k] == 1):
                                    t= t+1
                            tmp.append(1/t)
                        l = 1
                        break;
                    else:
                        sum = sum + pow(d[i][k]/d[j][k],2/(mp-1))
                if (l==0):
                    sum = pow(sum,-1)
                    tmp.append(sum)
            U1.append(tmp)
     #   print(U1)
        minus = []
        max = 0
        for l in range(c):
            tmp = []
            for k in range(len(data)):
                tmp.append(abs(U1[l][k] - U0[l][k]));
                if (abs(U1[l][k] - U0[l][k]) >= max ):
                    max = abs(U1[l][k] - U0[l][k])
            minus.append(tmp)
        if (max < eps):
            f = 1
            it1 = iteration
            break;
        U0 = U1
    if (f == 1):
        print("reached epsilon at iteration ",iteration+1)
    else:
        print("Done ", it , "iterations ")
    print("Final classification matrix:")
    print(U1)
    print("Final cluster centers:")
    print(v)

    xs1 = [x[0] for x in tempd]
    ys1 = [x[1] for x in tempd]
    plt.plot(xs1,ys1,'go')
    xs = [x[0] for x in v]
    ys = [x[1] for x in v]
    plt.plot(xs,ys,'ro')
    plt.axis([-100, 100, -100, 100])
    plt.show()
    return ;



n = 5
d = 2
data = []
for n1 in range(n):
    tmp = []
    for d1 in range(d):
        tmp.append(random.randrange(-100,100,1))
    data.append(tmp)
print(data)
#data = [[1,3],[1.5,3.2],[1.3,2.8],[3,1]]
fcmean(2,5,data)