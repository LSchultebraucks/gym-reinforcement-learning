import gym
import random
from agent import Agent

def main():
    env = gym.make("CartPole-v1")
    
    print("Observation space: ", env.observation_space)
    print("Action space: ", env.action_space)
    
    agent = Agent(env)
    state = env.reset()

    for _ in range(1000):
        action = agent.get_action(state)
        state, reward, done, info = env.step(action)
        env.render() 


if __name__ == "__main__":
    main()