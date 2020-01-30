import random as rand
# import matplotlib.pyplot as plt

# CP Tables for every node (A, G are always True, no tables needed)
# Able to get proper index by mapping vals by their truth table
# Ex. B_TABLE:
#   - First 4 vals are C=F, Last 4 are C=T
#   - This is why we multiply the node C val (0 or 1) by 4 for B_TABLE indexes
#   - Every 2 vals switch between D=F and D=T (i.e. F, F, T, T, F, F, T, T)
#   - This is why we multiply the node D val (0 or 1) by 2 for B_TABLE indexes
#   - Every other val switches bewteen E=F and E=T
#   - This is why we just use the node value of E for B_TABLE indexes
#   - For P(B|A,C,!D,E), we have:
#       - C (node[1]) * 4 + D (node[2]) * 2 + E (node[3])
#       - 1 * 4 + 0 * 2 + 1 = 5
#       - The probabilty for the assignment P(B|A,C,!D,E) is at pos 5 -> .129
B_TABLE = [.092, .28, .061, .2, .08, .129, .053, .087]
C_TABLE = [.125, .75, .109, .533]
D_TABLE = [.308, .348, .222, .255]
E_TABLE = [.058, .069, .565, .391, .192, .222, .69, .727]


# Generates a T/F value (1/0) based on whether or not the probability
#   input is <= a randomly generated float between 0 and 1
def biasedNumGen(prob):
    result = rand.uniform(0, 1)
    if result <= prob:
        return 1
    return 0


# These functions all perform the same way
#   Input: Current assignment of nodes
#   Actions:
#       - Generates postion (index) based on Truth values
#       - Updates appropriate truth val based on biased number generator
# ------------------------------------------------------------------------------
def getValB(nodes):
    pos = nodes[1] * 4 + nodes[2] * 2 + nodes[3]
    assignments[0] = biasedNumGen(B_TABLE[pos])


def getValC(nodes):
    pos = nodes[0] * 2 + nodes[3]
    assignments[1] = biasedNumGen(C_TABLE[pos])


def getValD(nodes):
    pos = nodes[0] * 2 + nodes[3]
    assignments[2] = biasedNumGen(D_TABLE[pos])


def getValE(nodes):
    pos = nodes[0] * 4 + nodes[1] * 2 + nodes[2]
    assignments[3] = biasedNumGen(E_TABLE[pos])


# ------------------------------------------------------------------------------

'''
Commented out, matplotlib works in pycharm but not through command line for me
# This shows a graph of the ratios of B=T for every run
def showGraph(vals):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # line 1 points
    y1 = []
    for val in vals[0]:
        y1.append(val)

    # line 2 points
    y2 = []
    for val in vals[1]:
        y2.append(val)

    # line 3 points
    y3 = []
    for val in vals[2]:
        y3.append(val)

    # line 4 points
    y4 = []
    for val in vals[3]:
        y4.append(val)

    # line 5 points
    y5 = []
    for val in vals[4]:
        y5.append(val)

    # plotting the line points
    plt.plot(x, y1, label="Run 1")
    plt.plot(x, y2, label="Run 2")
    plt.plot(x, y3, label="Run 3")
    plt.plot(x, y4, label="Run 4")
    plt.plot(x, y5, label="Run 5")

    # naming the x-axis
    plt.xlabel('Instances (1=1000)')
    # naming the y-axis
    plt.ylabel('Ratio of B=T to total instances')
    # plot title
    plt.title('Approximation Values')
    # plot legend
    plt.legend()
    # function to show the plot
    plt.show()
'''

if __name__ == '__main__':
    assignments = [0, 0, 0, 0]  # Initialize the assignments [B, C, D, E]

    # Array to keep track of ratio vals for each run
    runVals = [[], [], [], [], []]

    # Do 5 runs
    i = 0
    while i < 5:
        print("Run: " + str(i + 1))

        # Create random base assigment
        k = 0
        while k < 4:
            assignments[k] = biasedNumGen(.5)  # .5 used for 50/50 chance
            k += 1

        numTrue = 0  # Counter for the number of times B is true

        # Do 10,000 instances each run
        j = 1
        while j <= 10000:
            # Record the ratio of B=T to total instances every 1000 instances
            if j % 1000 == 0:
                ratio = round((float(numTrue) / j), 3)
                print('After ' + str(j) + ' instances: ' + str(ratio))
                runVals[i].append(ratio)

            # Increment numTrue every run based on B=T (+1) or B=F (+0)
            numTrue += assignments[0]

            # Evaluate the values for each node based on current assignments
            getValB(assignments)
            getValC(assignments)
            getValD(assignments)
            getValE(assignments)
            j += 1

        i += 1
    # showGraph(runVals)
