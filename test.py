import numpy as np
import random
a = np.random.randn(3,3)
print (max(a[1,:]))
import gym
env = gym.make("FrozenLake-v0")

print ("\n")
for i in range(15):
    print(env.action_space.sample())
print ("\n")

for i in range(20):
    print (random.uniform(0,1))

print ("\n")
for i in range(20):
    print (random.random())

