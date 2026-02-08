# Summaries of New Papers for Combined Review

## 1. APPA-3D: an autonomous 3D path planning algorithm for UAVs in unknown complex environments
**Authors**: Jintao Wang et al. (Nature Scientific Reports)
**Problem Statement**: Path planning in unknown complex 3D environments is difficult due to the need for collision avoidance and handling unknown information.
**Methodology**:
- **Algorithm**: APPA-3D (Autonomous Path Planning Algorithm in 3D).
- **Technique**: Deep Reinforcement Learning (DRL) with a dynamic reward function.
- **Features**: Uses a collision safety envelope and an improved exploration strategy based on action selection probability.
**Innovations**:
- Dynamic reward function tailored to the flight environment.
- Optimized action exploration strategy.
**Results**: Comparative experiments show effective collision-free path planning from start to target in unknown 3D environments.
**Limitations**: Reliance on simulated environments for training; potential computational intensity of dynamic rewards.

## 2. Agile DQN: adaptive deep recurrent attention reinforcement learning for autonomous UAV obstacle avoidance
**Authors**: Fadi AlMahamid & Katarina Grolinger (Nature Scientific Reports)
**Problem Statement**: UAV obstacle avoidance in 3D environments with high-dimensional inputs and partial observability demands sophisticated handling of state representations.
**Methodology**:
- **Algorithm**: Agile DQN (AG-DQN).
- **Technique**: DRL with Attention and LSTM.
- **Architecture**: Synergizes Glimpse Network, LSTM Recurrent Network, Emission Network, and Q-Network.
**Innovations**:
- Dynamic focus on key visual features (Attention mechanism).
- Adaptive temporal attention strategy to balance recent and past observations.
**Results**: Improved performance over existing DRL methods in terms of navigation success and robustness in dynamic conditions.
**Limitations**: Complex architecture with multiple networks increases computational requirements.

## 3. Autonomous UAV Visual Navigation Using an Improved Deep Reinforcement Learning
**Authors**: Hussein Samma & Sami El-Ferik (IEEE Access)
**Problem Statement**: Navigating in dynamic environments (e.g., with moving pedestrians) is challenging and traditional DRL suffers from slow learning rates.
**Methodology**:
- **Algorithm**: Improved DQN with Self-Supervised Learning.
- **Technique**: Two-stage learning: (1) Reinforced learning (DQN with Bellman loss), (2) Self-supervised learning (Contrastive loss) to fine-tune the backbone.
**Innovations**:
- Integration of self-supervised learning to speed up encoding of input scenes.
- Use of obstacle detection to enhance performance.
**Results**: Faster learning and better navigation performance in dynamic situations compared to standard DQN.
**Limitations**: Two-stage training process adds complexity to the pipeline.

## 4. SIGN: Safety-Aware Image-Goal Navigation for Autonomous Drones via Reinforcement Learning
**Authors**: Yibing Yan et al.
**Problem Statement**: Image-Goal Navigation in cluttered environments where collisions are costly and safety is paramount.
**Methodology**:
- **Algorithm**: SIGN (Safety-Aware Image-Goal Navigation).
- **Technique**: Reinforcement Learning with safety constraints.
**Innovations**:
- Safety-aware mechanism integrated into the navigation policy.
- End-to-end image-based navigation.
**Results**: Achieved navigation goals while minimizing collision risks.
**Limitations**: Image-based navigation can be sensitive to lighting and texture variations; "blind" spots in safety awareness depending on sensor setup.

## 5. Autonomous localized path planning algorithm for UAVs based on TD3 strategy
**Authors**: Zhao Feiyu et al. (Nature Scientific Reports)
**Problem Statement**: Local path planning in unfamiliar environments faces issues of poor consistency and influence by native controllers.
**Methodology**:
- **Algorithm**: TD3 (Twin Delayed Deep Deterministic Policy Gradient).
- **Technique**: Continuous control DRL.
**Innovations**:
- Application of TD3 strategy for autonomous local path planning.
- Addressed overestimation bias of DDPG.
**Results**: Success rate of 93% (no obstacles) and 92% (with obstacles) in Gazebo simulations.
**Limitations**: Focuses on local path planning; might need integration with global planner for large-scale missions.

## 6. Deep reinforcement learning-based controller for path following of an unmanned surface vehicle
**Authors**: Joohyun Woo et al. (Ocean Engineering)
**Problem Statement**: Path following for Unmanned Surface Vehicles (USV) in complex environments.
**Methodology**:
- **Algorithm**: DDPG (Deep Deterministic Policy Gradient).
- **Technique**: Actor-Critic based RL.
- **Context**: Markov Decision Process (MDP) designed for USV dynamics.
**Innovations**:
- Validated through full-scale free-running tests of a USV (rare for RL papers).
- Self-development of path following capability.
**Results**: Successful path following in simulation and real-world tests.
**Limitations**: Application is USV (2D water surface), not UAV (3D air), though methodology is transferrable.

## 7. A multi-critic deep deterministic policy gradient UAV path planning
**Authors**: Runjia Wu et al. (IEEE CIS)
**Problem Statement**: Environmental sensitivity and slow convergence in DDPG-based path planning.
**Methodology**:
- **Algorithm**: Multi-Critic DDPG.
- **Technique**: Extension of DDPG with multiple critic networks.
**Innovations**:
- Multi-critic mechanism to reduce variance and improve stability.
**Results**: Improved convergence speed and stability compared to standard DDPG.
**Limitations**: Increased computational cost due to multiple critic networks during training.

## 8. Unmanned Aerial Vehicle Path Planning Algorithm Based on Deep Reinforcement Learning in Large-Scale and Dynamic Environments
**Authors**: Ronglei Xie et al. (IEEE Access)
**Problem Statement**: Path planning in large-scale, dynamic environments with limited sensor capabilities (Partial Observability).
**Methodology**:
- **Algorithm**: DRL with Recurrent Neural Network (RNN).
- **Technique**: POMDP formulation. Adaptive experience replay based on failure frequency.
**Innovations**:
- Use of RNN for temporal memory in large-scale environments.
- Adaptive experience replay mechanism.
**Results**: Significant improvements over DQN and DRQN in stability and efficiency.
**Limitations**: Partial observability makes optimal policy learning harder; large-scale environments increase training time.

## 9. Collaborative Path Planning for Multiple Unmanned Aerial Vehicles to Avoid Sudden Threats
**Authors**: Xia Chen & Miaoyan Zhao
**Problem Statement**: Multi-UAV path planning in the presence of sudden threats requires rapid re-planning and coordination.
**Methodology**:
- **Algorithm**: V-Diagram + Mission Assignment + Cubic Spline + Crowding Mechanism.
- **Technique**: **Non-DRL** (Heuristic/Optimization based).
**Innovations**:
- Combination of V-diagram for initial planning and local re-planning for threats.
- Secondary security screening using crowding mechanism.
**Results**: Effective avoidance of sudden threats with collaborative behavior.
**Limitations**: Relies on accurate threat detection; heuristic methods may not generalize as well as learning-based methods in unforeseen scenarios.

## 10. Cooperative control of UAV swarm via information measures
**Authors**: Haoyang Cheng et al. (International Journal of Intelligent Unmanned Systems)
**Problem Statement**: Decentralized control of UAV swarms for cooperative missions (ground target engagement).
**Methodology**:
- **Algorithm**: Rule-based Decentralized Control.
- **Technique**: **Non-DRL** (Information Theoretic Measures).
**Innovations**:
- Use of information measures to estimate the value of future actions without central authority.
**Results**: Highly cooperative performance achieved via local rules.
**Limitations**: Performance depends on the complexity of coupled constraints; rule-based systems may be brittle.
