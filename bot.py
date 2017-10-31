import pickle
import random
import time
from matplotlib import pyplot as plt


class Bot:

    def __init__(self):
        self.counter = 0
        self.alpha = 0.7
        self.discount = .9
        self.fileName = 'Q-table-discretisation-4.pkl'
        try:
            with open(self.fileName, 'rb') as f:
                self.Q = pickle.load(f)
        except FileNotFoundError:
            self.Q = {}
        self.noFlapBias = 0.05
        self.pipeReward = -15
        self.sumScore = 0
        self.scoreList = []
        self.sampleRate = 500
        self.epsilon = 0.001
        plt.ion()

    def maxQ(self, state):
        # Chooses the higher Q-value with a probability of (1-epsilon)
        max_val = max(self.Q[state])
        max_act = self.Q[state].index(max_val)

        if random.random()<self.epsilon:
            max_act = int(not max_act)
            max_val = self.Q[state][max_act]
        return max_act, max_val

    def appendState(self, state):
        # Add state to Q table if not already added
        if state not in self.Q:
            self.Q[state]=[]
            self.Q[state].append(0)
            self.Q[state].append(0)

# exp is a tuple(old_state, best_action, reward, new_state)

    def updateQ(self, exp, upCrash, score):
        self.sample(score)
        
        exp.reverse()

        # If crashed with upper pipe then tax the jump
        if upCrash:
            for i, xp in enumerate(exp):
                if xp[1]==1:
                    temp = list(exp[i])
                    temp[2] = self.pipeReward
                    exp[i] = tuple(temp)
                    break
        # For each entry calculate
        for xp in exp:
            s = xp[0]
            a = xp[1]
            r = xp[2]
            _, fut_r = self.maxQ(xp[3])
            self.Q[s][a] *= 1 - self.alpha
            self.Q[s][a] += self.alpha * (r + self.discount*fut_r )

    def sample(self, score):
        self.counter += 1
        print(self.counter, score)
        self.sumScore+= score
        plt.plot(self.counter, score, 'b.')

        if self.counter%self.sampleRate == 0:
            self.epsilon *= 0.8
            plt.plot(self.counter, self.sumScore/self.sampleRate, 'ro')
            self.sumScore = 0


    def saveQ(self):
        with open(self.fileName,'wb') as f:
            pickle.dump(self.Q, f)
        
