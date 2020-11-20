import pandas as pd
import numpy as np
import random
import statistics
import time


class Diff_priv():

    def __init__(self, path, columns_name = ["respiration"], epsilon=[0.01]):
        self.__path = path
        self.__columns_name = columns_name
        self.__epsilon = epsilon
    
    
    def __laplaceMechanism(self, x, epsilon, sensib):
        rs = np.random.RandomState(int(time.time()))
        mt19937 = np.random.MT19937()
        mt19937.state = rs.get_state()
        rd = np.random.RandomState(mt19937)
        x +=  rd.laplace(0, (sensib/epsilon), 1)[0]
        return x
    
    
    def __sensitivity_avg(self, data):
        tam = len(data)
        dist = list()
        data_np = np.array(data)
        rs = np.random.RandomState(int(time.time()))
        mt19937 = np.random.MT19937()
        mt19937.state = rs.get_state()
        rd = np.random.RandomState(mt19937)
        pos_np = rd.randint(low=0,high=tam-2, size=100,dtype=int)
        pos = list(np.unique(pos_np))
        for i in pos:
            d1 = np.delete(data_np, [i])
            d2 = np.delete(data_np, [i+1])

            d = np.abs(np.mean(d1) - np.mean(d2))
            dist.append(d)
        
        return(max(dist))
    

    def apply_privacy_avg(self):
        record = open("avg.csv", "w")
        record.write("epsilon,avg,avg_DP\n")

        data = pd.read_csv(self.__path)[:5000]
        
        noise_data_by_ep = dict()

        original =  np.mean(data["respiration"])
        s = self.__sensitivity_avg(data["respiration"])


        for e in self.__epsilon:
            noise_data = dict()
            noise_data["respiration"] = self.__laplaceMechanism(original, e, s)
            noise_data_by_ep[str(e)] = noise_data

            formatted_e = "{:.3f}".format(e)
            record.write(str(formatted_e) + "," + str(original) + "," + str(noise_data["respiration"]) + "\n")
        
        record.close()


        return noise_data_by_ep

    
    def __sensitivity_median(self, data):
        tam = len(data)
        dist = list()
        data_np = np.array(data)
        rs = np.random.RandomState(int(time.time()))
        mt19937 = np.random.MT19937()
        mt19937.state = rs.get_state()
        rd = np.random.RandomState(mt19937)
        pos_np = rd.randint(low=0,high=tam-2, size=100,dtype=int)
        pos = list(np.unique(pos_np))
        for i in pos:
            d1 = np.delete(data_np, [i])
            d2 = np.delete(data_np, [i+1])

            d = np.abs(np.subtract(np.median(d1), np.median(d2)))
            dist.append(d)
        
        return(max(list(dist)))

    
    def apply_privacy_median(self):
        record = open("median.csv", "w")
        record.write("epsilon,median,median_DP\n")

        data = pd.read_csv(self.__path)[:5000]
        
        noise_data_by_ep = dict()

        original = np.median(data["respiration"])
        s = self.__sensitivity_avg(data["respiration"])

        for e in self.__epsilon:
            noise_data = dict()
            noise_data["respiration"] = self.__laplaceMechanism(original, e, s)
            noise_data_by_ep[str(e)] = noise_data


            formatted_e = "{:.3f}".format(e)
            record.write(str(formatted_e) + "," + str(original) + "," + str(noise_data["respiration"]) + "\n")
        
        record.close()

        return noise_data_by_ep