import itertools
import matplotlib.pyplot as plt


sampleSpaceCoins = list(itertools.product(["H", "T"], repeat = 2))

eventA = [outcome for outcome in sampleSpaceCoins if outcome[0] == "H"]
eventB = [outcome for outcome in sampleSpaceCoins if outcome[1] == "H"]


def independentEventVizual(sampleSpace, eventA, eventB):
    plt.figure(figsize=(10, 6))
    plt.bar(["".join(outcome) for outcome in sampleSpace], [1]*len(sampleSpace), color="lightgrey", edgecolor="black")

    for outcome in eventA:
        plt.bar("".join(outcome), 1, color="lightgreen", edgecolor="black")

    for outcome in eventB:
        plt.bar("".join(outcome), 1, color="lightgreen", edgecolor="black")
        


    plt.xlabel("Outcomes")
    plt.ylabel("Indicator")
    plt.title("Independent Events")
    plt.ylim(0, 1.5)
    plt.xticks(["".join(outcome) for outcome in sampleSpace])
    plt.yticks([])
    plt.show()



independentEventVizual(sampleSpaceCoins, eventA, eventB)
