# FlapPy-Bird-Q-Learning-Bot
A Q-Learning Bot to play the game Flappy Bird

# Files
1. assets: Sounds and images required to run the game

2. flappy.py: Flappy Bird Clone (Credit: https://github.com/sourabhv/FlapPyBird)

3. flappy-bot.py: Modification of flappy.py to incorporate the Q-Learning Bot (bot.py).

4. bot.py: A bot(class) that takes care of Reinforcement Learning and generates results.

# What is Q-Learning?


## Intuition
#### The bird creates experiences tuples from all the <states,action> tuples and the associated rewards.
#### The bot learns from the rewards positive/negative.
#### It chooses action for the current state based on the experience.


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
#### The strategy for selecting each of the parameters is discussed further.
### 2. Initialize matrix Q to zero.
### 3. For each episode:
#### i.   Select one among all possible actions for the current state.(Here, epsilon strategy)
#### ii.  Using this possible action, consider going to the next state.
#### iii. Get maximum Q value for this next state based on all possible actions.
#### iv.  Compute: Q(state, action) := (1-alpha)*Q(state, action)  + alpha * [R(state, action) + Gamma * Max[Q(next state, all actions)]]
#### v.   Set the next state as the current state


## Strategies Used
