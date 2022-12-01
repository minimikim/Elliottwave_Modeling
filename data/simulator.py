import os
import random
import numpy as np
import pandas as pd


class simulator:
    def __init__(self,data_path,value='open'):
        #datapath is for simulation

        self.dataframe=pd.read_csv(data_path)
        self.gen_list=list()
        self.value='open'

    def __call__(self):
        #call function sets an initial price index for the price generation process
        self.data=self.dataframe[self.value]
        self.init_idx=random.choice(range(len(self.data)))
        self.gen_list.append(self.init_idx)

    def __len__(self):
        return len(self.gen_list)
    def gen(self):
        #gen fuction save index records in gen_list and generate the price
        out_idx=self.gen_list[-1]
        next_idx=int(out_idx)+1
        self.gen_list.append(next_idx)

        #logger False:renew everytime
        os.makedirs('data/logs',exist_ok=True)
        cwd=os.getcwd()+'/data/logs'
        filename = os.path.join(cwd, 'log.txt')
        with open(filename,'w') as f:
            for idx in self.gen_list:
                f.write(str(idx)+'\n')

        return self.data[out_idx]
