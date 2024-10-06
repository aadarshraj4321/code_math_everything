import matplotlib.pyplot as plt
import numpy as np


# Vizualize probabilities
def probVizual(probabilities):
    events = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(events, probs, color="purple")
    plt.xlabel("Events")
    plt.ylabel("Probability")
    plt.title("Probability Distribution")
    plt.ylim(0, 1)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axhline(1, color="black", linewidth=0.5)

    for i, prob in enumerate(probs):
        plt.text(i, prob + 0.02, f"{prob: .2f}", ha="center")
    plt.show()


def checkNormalization(probabilities):
    totalProb = sum(probabilities.values())
    plt.figure(figsize=(10, 6))
    plt.bar(["Total Probability"], [totalProb], color="orange")
    plt.axhline(1, color="black", linewidth=0.5, linestyle='--')
    plt.ylabel("Probability")
    plt.title("Total Probability Check")
    plt.text(0, totalProb + 0.02, f"{totalProb:.2f}", ha="center")
    plt.show()
    return totalProb


def additivityVizual(pa, pb):
    paOrpb = pa + pb
    plt.figure(figsize=(10, 6))
    events = ['P(A)', 'P(B)', 'P(A or B)']
    probs = [pa, pb, paOrpb]
    colors = ["blue", "blue", "green"]
    plt.bar(events, probs, color=colors)
    plt.xlabel("Events")
    plt.ylabel("Probability")
    plt.title("Additivity of Probabilities for Mutually Exclusive Events")
    plt.ylim(0, 1)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axhline(1, color="black", linewidth=0.5)

    for i, prob in enumerate(probs):
        plt.text(i, prob + 0.02, f"{prob:.2f}", ha="center")
    plt.show()    



prob = {'A': 0.5, 'B': 0.25, 'C': 0.25}
probVizual(prob)

totalProb = checkNormalization(prob)
print(f"Total Probability: {totalProb}")

pa = 0.4
pb = 0.3
additivityVizual(pa, pb)
print(f"P(A or B) = P(A) + P(B) = {pa + pb}")

