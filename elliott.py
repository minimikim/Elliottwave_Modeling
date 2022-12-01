### elliott main py
import os
import time
import random

from data.simulator import simulator
from models.wave_detector import monowave


data_path=os.path.join(os.getcwd(),'data/btcusd.csv')
def main():
    #simulator setting
    sim=simulator(data_path)
    sim()
    #detector setting
    mon=monowave()

    while True:
        time.sleep(1)
        #1. simulator bring realtime price data
        price=sim.gen()
        mon.add(price)

        #2. detector save the price data and fit monowave
        price,label=mon.analyze()

        #3. plot the elliott wave as graph and update log
        #plotting output
        print(sim.gen_list[-1],price,label)

if __name__=="__main__":
    print('start!')
    main()
