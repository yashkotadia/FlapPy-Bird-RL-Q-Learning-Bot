# FlapPy-Bird-Q-Learning-Bot
### A Q-Learning Bot to play the game Flappy Bird
![300000 crossed!](https://github.com/yashkotadia/FlapPy-Bird-Q-Learning-Bot/blob/master/Results/High-Score.png)

# Files
1. assets: Sounds and images required to run the game

2. flappy.py: Flappy Bird Clone (Credit: https://github.com/sourabhv/FlapPyBird)

3. flappy-bot.py: Modification of flappy.py to incorporate the Q-Learning Bot (bot.py).

4. bot.py: A bot(class) that takes care of Reinforcement Learning and generates results.

5. plot-scores.py: Plotting the training curve from the scores file generated.

6. scores.pkl: List of scores from the previous session

# What is Q-Learning?


## Intuition
The bird creates experiences tuples from all the <states,action,reward> tuples collected while playing.  
The bot learns from the positive/negative experiences.  
It chooses action for the current state based on the experience.


## Certain Descriptions:

### Q-Value 
It indicates the benefits of taking an action. Higher the Q-value, higher the benefits.
### State
It is a tuple of values used to disctinctly identify the state of the model (here, the bird).
In our case the state tuple is made of three values:
<y-distance between the player and lower_pipe, x-distance between the player and pipes, player y-velocity>
### Action
It is a set of legal actions the model may take
### Reward
It is a constant value which is used indicate the positivity or negativity of taking an action.
Here, Die Reward = -10; Point Scored Reward = 1; Upper pipe Crash Reward = -15(Discussed further)
### Experience Tuple
It is a tuple <state, action, reward>.
Reward of choosing a particular action from a state and the rewards associated with it.
It is only used to update the Q-Table.
### Q-Table
It is essentially an experience table.
It contains the Q-value associated with a <state, action> pair.
### Discount Rate (gamma):
It decides how important a future reward is.
### Learning Rate (alpha):
It decides how much a newly learned experience influences the Q-Table(model).
### Episode
The model takes an action and updates a Q-Table value accordingly, once within each episode.


## Algorithm:

### 1. Initialize gamma, alpha and rewards.
The strategy for selecting each of the parameters is discussed further.
### 2. Initialize matrix Q to zero.
### 3. For each episode:
#### i.   Select one among all possible actions for the current state.(Here, epsilon strategy)
#### ii.  Using this possible action, consider going to the next state.
#### iii. Get maximum Q value for this next state based on all possible actions.
#### iv.  Compute: Q(state, action) := (1-alpha)*Q(state, action)  + alpha * [R(state, action) + Gamma * Max[Q(next state, all actions)]]
#### v.   Set the next state as the current state


## Strategies Used

### Discount Rate
The Discount rate is chosen to be 0.9 on the assumption that it would be foresighted.

### Learning Rate
The learning rate is a constant 0.7

### Rewards
Score Point: 1, a reward of 1 is allocated for scoring a point.  
Die: -10, punishes the model for crash.  
Upper Pipe Crash: -15, penalises the last jump that led to a crash into the upper pipe. This is done to overcome the tendency of the model to hit the upper pipe.  

### Epsilon-Greedy Q-Learning
It is used to adjust the exploitation-exploration component.  
The algorithm starts with exploration which over time is converted to exploitation.

### Reversal of list of Experience Tuples
The list of experience tuples is reversed during updation of Q-Table.  
This enables a faster propagation of Q-Values across the table.  
The list of experience tuples starts with the first action being taken and ends with the last.  
If the updation occurs in the reverse manner, the future data is updated first.  
Hence, during the processing of past data, the values of recently updated tuple allows for faster propagation of Q-values across the table.  

### Discretisation
Divide the screen into grids of size n, hence n is the size of each discrete pixel group.  
This Reduces the state space and hence reduces the time required to learn.
Discretisation = 4 gives the best result on the game. Probable explantation would be that the game advances by 4 pixels in each episode.


# Results

### Note

#### 1. Scoring is Learning
The x-axis represents the number of games played. However this is not exactly an appropriate metric.  
This is because the more it scores in a game, the more it learns from it.  
The computation done over a period of time is same for both a low scoring model and a high scoring model.  
However the higher scoring model will have played fewer games over that period than a higher scoring model.  
This is an important point to consider when comparing models.
#### 2. Exploration and Exploitation
The model is coded to explore more in the start and hence will score lower.  
The actual results will only be visible once it starts exploiting.  

### Discretisation=10
![Training Curve Discretisation-10](https://github.com/yashkotadia/FlapPy-Bird-Q-Learning-Bot/blob/master/Results/10.png)  
It converges to an average score of 25 which is too less for a bot.  
However it is quick and is useful for debugging.

### Discretisation=4
Here's where things start getting interesting!  
![Training Curve Discretisation-4](https://github.com/yashkotadia/FlapPy-Bird-Q-Learning-Bot/blob/master/Results/4.png)
The model does fairly well until 32,500.  
However it spikes up after that leading to an average score of 30,000 and probably more.  
The scores start cross 1,00,000 mark. At this point it takes over a day to play 50 games.
The model still doesnt seem to have converged and probably will do even better.  
The reason for spiking could be a combined effect of learning and exploiting. Since the model has had over 3 billion episodes and epsilon has been reduced to a small value.

### Discretisation=1
![Training Curve Discretisation-1](https://github.com/yashkotadia/FlapPy-Bird-Q-Learning-Bot/blob/master/Results/1.png)
The model has learnt at a constant rate.
However since the state space is too large, it would take too much time to train it.  

# Try it yourself
1. Make sure the discretisation in flappy-bot.py, scores.pkl and Q-Table.pkl is the same
2. Simply run flappy-bot.py to start with the pretrained model
3. Delete the files(scores.pkl, Q-Table.pkl) and then run flappy-bot.py to train from start.

# Improvisation
### 1. Learning Rate
The current learning rate is purely based on my intuition.
A strategy which reduces learning rate over time would make the model more stable.

### 2. Discount Rate
Discount Rate is set to 0.9 assuming that the model should always be thinking about the future.  
However the future consciousness must vary over an entire point.  
That is the future is more important when pipe is far away, however when it is closer factoring the future would involve trying to figure out where the next pipe would be which of course is placed randomly.  
Hence the discount rate must be made to vary over the course of scoring a point which is 24 episodes.

### 3. Efficiency
The model is currently really slow to train.
The graphical window part could be made optional so that it may be shut during training.
It shall definitely make the model faster.

## Credits
1. Clone of Flappy Bird: https://github.com/sourabhv/FlapPyBird
2. Reversal of experience list, Tendency to hit Upper Pipe: https://github.com/chncyhn/flappybird-qlearning-bot
3. For a detailed and intuitive explanation on Q-Learning: http://mnemstudio.org/path-finding-q-learning-tutorial.htm
