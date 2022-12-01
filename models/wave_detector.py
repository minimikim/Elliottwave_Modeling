# wave detector classses
import os

class monowave:
    def __init__(self):
        self.price=list()
        self.idx=1
        self.status=str()
        self.label=list()
    def add(self,price):
        self.price.append(price)

    #indexing monowaves as M1 M2 M3 M4 ...
    #at this time we do not mind the direction
    #analyze function starts when length is over 3
    def analyze(self):
        self.init_price=self.price[0]

        if len(self.price)<3:
            label='M'+str(self.idx)
            price=self.price[-1]

            if self.price[0]<self.price[-1]:
                self.status='inc'
            else:
                self.status='dec'

        else:
            # keep increasing
            if self.status=='inc':
                if self.price[-2]<=self.price[-1]:
                    label='M'+str(self.idx)
                    price=self.price[-1]
                else:
                    self.idx+=1
                    label='M'+str(self.idx)
                    price=self.price[-1]
                    self.status='dec'
            elif self.status=='dec':
                if self.price[-2]<=self.price[-1]:
                    self.idx+=1
                    label='M'+str(self.idx)
                    price=self.price[-1]
                    self.status='inc'
                else:
                    label='M'+str(self.idx)
                    price=self.price[-1]
        self.label.append(label)

        #logger
        os.makedirs('models/logs',exist_ok=True)
        cwd=os.getcwd()+'/models/logs'

        filename = os.path.join(cwd, 'log.txt')

        with open(filename,'w') as f:
            for i in range(len(self.price)):
                f.write("%s, %s\n"%(self.price[i],self.label[i]))

        return price,label
