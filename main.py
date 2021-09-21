import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.activations import sigmoid
import gym


class A3C:
    def __init__(self, state_size, action_size):
        self.n_actions = action_size
        self.lr = 0.01
        self.memory_buffer = 2000
        self.state_size = state_size
        self.gamma = 0.5
        self.probs = []
        self.actions = []
        self.rewards = []

    def model_maker(self):
        model = tf.keras.Sequetial(
            Dense(units=100, input_dim=self.state_size, activation="relu"),
            Dense(units=50, activation="relu"),
            Dense(units=self.n_actions, activation=sigmoid)
        )

    def compute_action(self, model, state):
        probs = model.predict(state)
        action = np.random.choice(self.n_actions, p=probs)
        self.probs.append(probs)
        self.actions.append(action)

    def store_reward(self, reward):
        self.rewards.append(reward)

    def discounted_rwds(self):
        discounted_rewards = []
        for x in range(len(self.rewards)):
            Gt = 0
            dsc = 0
            for y in self.rewards[x:]:
                Gt=Gt+self.gamma**dsc*y
            discounted_rewards.append(Gt)

"""The Actor-Critic is basically like the brain of the A3C model. At it’s core it implements deep convolution Q learning
, however the neural network now outputs two different items. The Actor and the Critic.
The Critic measures how good the action taken is (value-based) V(s)
The Actor outputs a set of action probabilities the agent can take (policy-based) Q(s,a)"""
"""The Advantage is how the Critic tells the Actor that it’s predicted Q-values from the ANN are good or bad. It calculates the policy loss.
This is calculated through the Advantage equation."""