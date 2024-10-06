import math


def checkProbabilityAximos(prob):
    # non-negativity
    for event, prob in prob.items():
        if prob < 0:
            return f"Probability of event {event} is negative which violates the non-negativity axom."

    # Normalization
    totalProb = sum(prob.values())
    if not math.isclose(totalProb, 1):
        return f"The total probability is {totalProb}, which violates the normalization axiom."

    return "All probability axioms are satisfied."



prob = {'A': 0.3, 'B': 0.4, 'C': 0.3}
print(checkProbabilityAximos(prob))
