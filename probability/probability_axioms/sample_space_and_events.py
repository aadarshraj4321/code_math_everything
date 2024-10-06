import matplotlib.pyplot as plt


sampleSpace = [1, 2, 3, 4, 5, 6]

evenEvent = [2, 4, 6]
oddEvent = [1, 3, 5]



def vizualSampleSpaceAndEvent(sampleSpace, event):
    plt.figure(figsize=(10, 6))

    plt.bar(sampleSpace, [1]*len(sampleSpace), color="lightgrey", edgecolor="black")

    for e in event:
        plt.bar(e, 1, color="skyblue", edgecolor="black")

    plt.xlabel("Outcomes")
    plt.ylabel("Indicator")
    plt.title("Sample Space and Event")
    plt.ylim(0, 1.5)
    plt.xticks(sampleSpace)
    plt.show()


vizualSampleSpaceAndEvent(sampleSpace, evenEvent)
