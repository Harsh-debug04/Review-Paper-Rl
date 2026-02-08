import os
import re

keywords = {
    "Network Architecture": ["network", "layer", "neuron", "activation", "hidden", "ReLU", "tanh", "LSTM", "CNN", "RNN", "fully connected", "dense"],
    "Hyperparameters": ["learning rate", "batch size", "gamma", "discount factor", "buffer size", "replay memory", "epsilon", "optimizer", "Adam", "RMSProp"],
    "Reward Function": ["reward", "penalty", "function", "equation", "collision", "goal", "distance", "step", "energy", "smoothness"],
    "Results": ["success rate", "collision rate", "training steps", "episode", "convergence", "performance", "average reward", "crash rate"],
    "Simulator": ["Gazebo", "Unity", "AirSim", "MATLAB", "ROS", "V-REP", "Unreal Engine", "simulation"],
    "Deployment": ["real-world", "experiment", "hardware", "field test", "outdoor", "indoor", "prototype", "DJI", "Crazyflie"]
}

extracted_dir = "extracted_text"
output_file = "detailed_extraction_summary.txt"

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in sorted(os.listdir(extracted_dir)):
        if not filename.endswith(".txt"): continue

        filepath = os.path.join(extracted_dir, filename)
        outfile.write(f"\n{'='*50}\nAnalysis for: {filename}\n{'='*50}\n")

        try:
            with open(filepath, "r", encoding="utf-8") as infile:
                lines = infile.readlines()

            for category, keys in keywords.items():
                outfile.write(f"\n--- {category} ---\n")
                count = 0
                for i, line in enumerate(lines):
                    if any(k.lower() in line.lower() for k in keys):
                        # Extract context (line before and after)
                        context = "".join(lines[max(0, i-1):min(len(lines), i+2)]).strip()
                        outfile.write(f"Line {i}: {context}\n...\n")
                        count += 1
                        if count > 10: break # Limit output per category

        except Exception as e:
            outfile.write(f"Error reading file: {e}\n")

print(f"Detailed extraction summary saved to {output_file}")
