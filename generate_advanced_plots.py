import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.rcParams.update({'font.size': 12})

# Data for Radar Chart (Normalized scores 0-10 based on analysis)
# Categories: Safety, Sample Efficiency, Scalability, Real-World Potential, Compute Efficiency
labels = ['Safety', 'Sample Efficiency', 'Scalability', 'Real-World Pot.', 'Compute Eff.']
num_vars = len(labels)

# Example Algorithms to compare
# 1. Standard DQN (Baseline)
# 2. TD3 / DDPG (Continuous Control)
# 3. Hybrid / Hierarchical (RLPlanNav)
# 4. Non-DRL Heuristic (V-Diagram)

values_dqn = [6, 4, 5, 5, 7]
values_td3 = [7, 6, 6, 8, 6]
values_hybrid = [9, 7, 5, 6, 5]
values_heuristic = [8, 10, 8, 9, 9]

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1] # Close the loop

values_dqn += values_dqn[:1]
values_td3 += values_td3[:1]
values_hybrid += values_hybrid[:1]
values_heuristic += values_heuristic[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values_dqn, color='skyblue', linewidth=2, label='Standard DQN')
ax.fill(angles, values_dqn, color='skyblue', alpha=0.25)

ax.plot(angles, values_td3, color='orange', linewidth=2, label='Continuous (TD3/DDPG)')
ax.fill(angles, values_td3, color='orange', alpha=0.25)

ax.plot(angles, values_hybrid, color='green', linewidth=2, label='Hybrid (RL+Planner)')
ax.fill(angles, values_hybrid, color='green', alpha=0.25)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title('Algorithm Performance Profile', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('comparison_assets/radar_chart.png')
print("Generated comparison_assets/radar_chart.png")

# Stacked Bar Chart: Reward Function Components
# Data: Count of papers using each component
components = ['Goal/Target', 'Collision', 'Smoothness/Energy', 'Time/Step', 'Special (FOV/Attn)']
counts = [14, 13, 6, 8, 5]

plt.figure(figsize=(10, 6))
bars = plt.bar(components, counts, color=['#4daf4a', '#e41a1c', '#377eb8', '#ff7f00', '#984ea3'])
plt.title('Frequency of Reward Function Components', fontsize=16)
plt.ylabel('Number of Papers', fontsize=12)
plt.ylim(0, 16)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('comparison_assets/reward_components.png')
print("Generated comparison_assets/reward_components.png")

# Grouped Bar Chart: Simulator Usage
simulators = ['Gazebo', 'Unity/AirSim', 'Custom/MATLAB', 'Real-World/Other']
counts_sim = [4, 4, 7, 1]

plt.figure(figsize=(8, 6))
plt.pie(counts_sim, labels=simulators, autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3'])
plt.title('Simulation Environments Used', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.savefig('comparison_assets/simulator_usage.png')
print("Generated comparison_assets/simulator_usage.png")
