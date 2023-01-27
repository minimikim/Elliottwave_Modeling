# wave detector classses
import os



class monowave:
    def __init__(self):
        self.price=list()
        self.idx=1
        self.status=str()
        self.label=list()
        self.time=list()
        self.set_time()
        self.direction=list()

    def add(self,price):
        self.price.append(price)
        self.time.append(len(self.price))
        #self.time=self.timestamp*self.time_price_ratio*self.time

    #indexing monowaves as M1 M2 M3 M4 ...
    #at this time we do not mind the direction
    #analyze function starts when length is over 3

    def set_time(self):
        '''
        suppose data is loading by daily
        default = day
        unix timestamp day : 86400
        '''
        self.timestamp=86400
        self.time_price_ratio=10/86400

    def rule_of_proportion(self):
        '''
        algorithm on given set of label and price

        '''

        unique_item=list(set(self.label))
        for i in range(1,len(unique_item)):
            unique=unique_item[i]
            idx_monofin=self.label.index(unique)-1
            label=self.label[idx_monofin]
            idx_monosta=self.label.index(label)
            price_mono_fin=self.price(idx_monofin)
            price_mono_sta=self.price(idx_monosta)
            price_mono_new=self.price(idx_monofin+1)

            if 0.618*abs(price_mono_fin-price_mono_sta)<abs(price_mono_new-price_mono_fin):
                t=idx_monofin-idx_monosta
                while t:
                    self.direction.append('non_dir')
                    t-=1
            else:
                t-idx_monofin-idx_monosta
                while t:
                    self.direction.append('dir')
                    t-=1
        print('this is direction state')
        print(self.direction)

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

        if len(set(self.label))>2:
            self.rule_of_proportion()

        #logger
        os.makedirs('models/logs',exist_ok=True)
        cwd=os.getcwd()+'/models/logs'

        filename = os.path.join(cwd, 'log.txt')

        with open(filename,'w') as f:
            for i in range(len(self.price)):
                f.write("%s, %s\n"%(self.price[i],self.label[i]))

        return price,label
