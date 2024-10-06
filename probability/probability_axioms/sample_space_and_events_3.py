
import matplotlib.pyplot as plt


sample_space_die = [1, 2, 3, 4, 5, 6]

event_A_die = [1]

event_B_die = [2]

def visualize_mutually_exclusive_events(sample_space, event_A, event_B):
    plt.figure(figsize=(10, 6))
    
    plt.bar(sample_space, [1]*len(sample_space), color='lightgrey', edgecolor='black')
    
    for e in event_A:
        plt.bar(e, 1, color='skyblue', edgecolor='black')
    
    for e in event_B:
        plt.bar(e, 1, color='lightgreen', edgecolor='black')
    
    plt.xlabel('Outcomes')
    plt.ylabel('Indicator')
    plt.title('Mutually Exclusive Events')
    plt.ylim(0, 1.5)
    plt.xticks(sample_space)
    plt.yticks([])
    
    plt.show()

visualize_mutually_exclusive_events(sample_space_die, event_A_die, event_B_die)
