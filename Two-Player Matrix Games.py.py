# -*- coding: utf-8 -*-
""" Reinforcement Learning 


---


1- Defining the required Libraries, Functions and do the necessary Preprocessing


---



The update rules for each player 𝑗 are:

$p{^{j}_c}(k+1) = p{^{j}_c}(k) + \alpha r^{j}(k) \Big[1 - p{^{j}_c}(k)\Big]$,      if action c is taken at time t


$p{^{j}_o}(k+1) = p{^{j}_o}(k) - \alpha r^{j}(k)p{^{j}_o}(k)$,    𝑓𝑜𝑟 𝑎𝑙𝑙 𝑜𝑡ℎ𝑒𝑟 𝑎𝑐𝑡𝑖𝑜𝑛𝑠 𝑜 ≠ 𝑐
"""

""" Libraries """
import sys
import time
import numpy as np
import matplotlib.pyplot as plt


"""
Defining all three games in one function.
This function Returns a dictionary object of parameters for each game.
"""

def Game(NumG):
  
        #  Numg values (Number of Game) [1-3] indicate the set of parameters to be returned, where
        #  1 is prisoner's dilemma
        #  2 is matching pennies
        #  3 is rock paper scissors  

    # Reward matrice of prisoner's dilemma
     PrsDil_R = np.array([
        [5, 0],
        [10, 1]
        ])
    
    # Reward matrice of matching pennies
     MatPen_R = np.array([
        [1, -1],
        [-1, 1]
        ])
     
     # Reward matrice of rock paper scissors
     RoPaSci_R = np.array([
        [0, -1, 1],
        [1, 0, -1],
        [-1, 1, 0]
        ])

     # Policy updating matrices:
     # Contain arrays which are used during the policy update equation, where 1 in the array
     # corresponds to the action to be increased and 0 indicates the action(s) to be decreased
     # in the policy update.    
     Unit2d = np.array([
        [1, 0],
        [0, 1]
        ])
     
     Unit3d = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
        ])


     # Graph labels:
     # Arrays of labels for graphing the experimental results for each game.
     if NumG < 3:
        GraphLabels1 = [
        ['Prisoner\'s Dilemma', 'Player1 Prb(Coop)', 'Player2 Prb(Coop)'],
        ['Matching Pennies', 'Player1 Prb(Head)', 'Player2 Prb(Head)'],
        ]
     else:
        GraphLabels1 = [
        ['Prisoner\'s Dilemma', 'Player1 Prb(Coop)', 'Player2 Prb(Coop)'],
        ['Matching Pennies', 'Player1 Prb(Head)', 'Player2 Prb(Head)'],
        ['Rock Paper Scissors', 'Prb(Rock)', 'Prb(Paper)','Prb(Scissor)'],
        ]

     GraphLabels2 = ['Value of Players','Iteration']


     # Logical (switch) statement to determine parameter selection.
     if NumG == 1: # Prisoner's Dilemma
        R1 = PrsDil_R
        R2 = PrsDil_R.T
        Unit = Unit2d
     elif NumG == 2: # Matching Pennies
        R1 = MatPen_R
        R2 = -MatPen_R
        Unit = Unit2d
     elif NumG == 3: # Rock Paper Scissors
        R1 = RoPaSci_R
        R2 = -RoPaSci_R
        Unit = Unit3d
     else:           # Default
        print('Enter the Game {1 2 3}')


     return {'r1': R1, 'r2': R2, 'Unit': Unit, 'labels1': GraphLabels1[NumG-1], 'labels2': GraphLabels2}


"""
 Since we need to play for different intial policies, we define a function 
 to generate different initial policies for each trial of each game.

"""
def InitPolicies(size, trial, game):
    
    # Returns a Initial Policy p_i for each player with a random uniform distribution scaled to [0, 1).
    # It is then normalize to sum to 1 for trial 1 to 5. 
    # 'size' is the number of actions in the policies, 'trial' is the number of playing 
    # and 'game' is the number of game {1 2 3}
    
    pi1 = np.abs(np.random.randn(len(R1))).astype(np.half)
    pi2 = np.abs(np.random.randn(len(R1))).astype(np.half)

    return pi1/pi1.sum(), pi2/pi2.sum()


"""
 Normalize the policies to ensure the values are in [0,1)
"""
def NormPolicies(p1, p2):
 
       # p1: an array representing player 1's policy
       # p2: an array representing player 2's policy
    
    # Restrict the polices to [0, 1].
    p1 = np.clip(p1, a_min=0, a_max=1)
    p2 = np.clip(p2, a_min=0, a_max=1)
    
    # Restrict the polices to sum to 1, and the resulting normalized polices to [0, 1].
    p1 = np.clip(p1/p1.sum(), a_min=0, a_max=1)
    p2 = np.clip(p2/p2.sum(), a_min=0, a_max=1)
    
    return p1, p2

"""2- The main algorithm and policy update loop is given here, this include the modification for the added Expectation term for all games



---



The update rules for each player 𝑗 are:

$p{^{j}_c}(k+1) = p{^{j}_c}(k) + \alpha r^{j}(k) \Big[1 - p{^{j}_c}(k)\Big]$,      if action c is taken at time t


$p{^{j}_o}(k+1) = p{^{j}_o}(k) - \alpha r^{j}(k)p{^{j}_o}(k)$,    𝑓𝑜𝑟 𝑎𝑙𝑙 𝑜𝑡ℎ𝑒𝑟 𝑎𝑐𝑡𝑖𝑜𝑛𝑠 𝑜 ≠ 𝑐


---
Modify the algorithm so another term is added:

$p{^{j}_c}(K+1) = p{^{j}_c}(K) + \alpha r^{j}(K) \Big[1 - p{^{j}_c}(K)\Big] + \alpha \Big\{E \Big[p{^{j}_c}(K)\Big] - p{^{j}_c}(K)\Big\}$, 𝑖𝑓 𝑎𝑐𝑡𝑖𝑜𝑛 𝑐 𝑖𝑠 𝑡𝑎𝑘𝑒𝑛 𝑎𝑡 𝑡𝑖𝑚𝑒 𝑡


$p{^{j}_o}(K+1) = p{^{j}_o}(K) - \alpha r^{j}(K)p{^{j}_o}(K) + \alpha \Big\{E \Big[p{^{j}_o}(K)\Big] - p{^{j}_o}(K)\Big\}$, 𝑓𝑜𝑟 𝑎𝑙𝑙 𝑜𝑡ℎ𝑒𝑟 𝑎𝑐𝑡𝑖𝑜𝑛𝑠 𝑜 ≠ 𝑐


 
"""

# The random generator with the ability to reproduce the Initial Policies for 
# different runs
np.random.seed(1000)

if __name__ == "__main__":

    # Learning Parameters
    Iteration = 40000
    Alpha = 0.01
    
    # Selecting True yields the policy update with the expected value term, and
    # False without.
    ExpectedValue = False
    

    # Get final policies for each game and graph the results.
    for NumG in range(1,4):

        # Initialize pyplot's subplot feature that will show graphs for each Trial
        if NumG < 3: # For the first two games
            fig, ax = plt.subplots(1,5,figsize=(17,3), constrained_layout=True)
        else: # For Rock Paper Scissors we a graph for each player
            plt.rcParams.update({'font.size': 8})
            fig = plt.figure(figsize=(19.,3.3), dpi=300, linewidth=0.2)


        # Initialize pyplots subplot for Value function graph for each Trial
        fig2, ax2 = plt.subplots(1,5,figsize=(17,3), constrained_layout=True)


        # GAME PARAMETERS

        # Get the parameters for the game.
        R1, R2, Unit, GraphLabels1, GraphLabels2 = Game(NumG).values()

        n_Choices = len(R1) # Number of possible actions in each player's policy

        Choices = np.arange(n_Choices) # An array of indexes corresponding to the possible actions
        print('\n********************************************************************************************')
        print('\t\t\t\t      %s ' % (GraphLabels1[0]))
        print('********************************************************************************************\n')

        # Run each Game for 5 Trials
        for Trial in range(5):
            
            # A Separate 3 dimensional graph axes is defined here for RPS Game
            if NumG == 3:
                ax = fig.add_subplot(1, 5, Trial+1, projection='3d')

            # EXPERIMENTAL TRIAL PARAMETERS

            # Initialize lists to store the data points to be plotted.
            pts_x = []
            pts_y = []
            pts_z = []
            V1 = []
            V2 = []
            Itr = []

            # Initialize the expected value terms of the update function to zeros
            Ex1, Ex2 = np.zeros(n_Choices), np.zeros(n_Choices)

            # Get the inital policies.
            p1, p2 = InitPolicies(n_Choices, Trial, NumG)

            # Show the initial policies for each trial for each game.
            print('@@@@@ Trial %d @@@@@' %(Trial + 1))
            print('\nInitial policy:\n  player 1', np.round(p1, 4),'\n  player 2', np.round(p2, 4))

            # Time execution.
            start = time.time()

            # Initialize the experimentally calculated value for the game for each player
            value_pl1 = 0
            value_pl2 = 0
            It = 0

            # Choose an action, get a reward and update the policies for 50000 iterations.
            for _ in range(Iteration):

                # Pick an action for each player randomly using their policy as the distribution function.
                Action1 = np.random.choice(Choices, p=p1)
                Action2 = np.random.choice(Choices, p=p2)

                # Determine the reward for each player.
                r1 = R1[Action1, Action2]
                r2 = R2[Action1, Action2]    

                # Keep a running total of the game's value for each player.
                value_pl1 += r1
                value_pl2 += r2
                # Value function after each Iteration
                Val1 = value_pl1/Iteration
                Val2 = value_pl2/Iteration
                It += 1

                # Update the policy for each player
                # Both actions are incorporated in the update las through 
                # through the Unit array  
                p1 = p1 + Alpha * r1 * (Unit[Action1] - p1)
                p2 = p2 + Alpha * r2 * (Unit[Action2] - p2)

                # Added the expected value term if required
                if ExpectedValue:
                    p1 = p1 + Alpha * (Ex1 - p1)
                    p2 = p2 + Alpha * (Ex2 - p2)


                # Normalize the policies
                p1, p2 = NormPolicies(p1, p2)

                # Update the expected value term with the previous policy
                Ex1 = Ex1 + Alpha*(p1 - Ex1)
                Ex2 = Ex2 + Alpha*(p2 - Ex2)

                
                # Collect data points for the all graphs
                if NumG < 3:
                    pts_y.append(p1[0])
                    pts_x.append(p2[0])
                    V1  = V1 +[Val1]
                    V2  = V2 + [Val2]
                    Itr = Itr + [It]
                else:
                    pts_y.append([p1[0], p2[0]])
                    pts_x.append([p1[1], p2[1]])
                    pts_z.append([p1[2], p2[2]])
                    V1  = V1 + [Val1]
                    V2  = V2 + [Val2]
                    Itr = Itr + [It]

            # Show the trial's execution time and the final policies and calculated values for each player.
            print('Finished in %.4f seconds: ' % (time.time() - start))
            print('Final policy:\n  player 1',np.round(p1,4),'\n  player 2', np.round(p2,4))
            print('Value of policy:\n  player 1: %.4f \n  player 2: %.4f \n' % (Val1, Val2))



            # Labels for the plots
            plotTitle = 'Trial %d' % (Trial + 1)
            if Trial == 5: # The last trial starts at the equilibrium point.
                plotTitle += '\nInitial Equilibrium Point'

            # Show a scatter plot of the policies, coloured by the iterations        
            if NumG < 3: # For the first two games
                title, yLabel, xLabel = GraphLabels1
                im = ax[Trial].scatter(pts_x, pts_y, c=np.arange(Iteration), cmap='jet',s=25)

                # Set the graph limits and labels
                ax[Trial].set_xlim(0,1)
                ax[Trial].set_ylim(0,1)
                ax[Trial].set_ylabel(yLabel)
                ax[Trial].set_xlabel(xLabel)
                ax[Trial].set_title(plotTitle)

                # Graph for Values of Players 
                yLabel, xLabel = GraphLabels2
                im2 = ax2[Trial].plot(Itr, V1, 'r-', label = "Player 1")
                im2 = ax2[Trial].plot(Itr, V2, 'b--', label = "Player 2")
                ax2[Trial].legend(loc="upper right")

                ax2[Trial].set_xlim(1,40000)
                ax2[Trial].set_ylim(-1.5,1.5)
                ax2[Trial].set_ylabel(yLabel)
                ax2[Trial].set_xlabel(xLabel)
                ax2[Trial].set_title(plotTitle)

                
                
            else: # For Rock Paper Scissor game, there are 3 Actions, so we need a graph for each player.
                # Graph for Player 1
                title, yLabel, xLabel, zLabel = GraphLabels1
                im = ax.scatter(np.array(pts_x)[:,0], np.array(pts_y)[:,0], np.array(pts_z)[:,0], c=np.arange(Iteration), cmap='jet',s=30)
                ax.set_title('Player 1 ' + plotTitle)

                # Graph for Player 2
                #ax.scatter(np.array(pts_x)[:,1], np.array(pts_y)[:,1], np.array(pts_z)[:,1], c=np.arange(Iteration), cmap='jet',s=30)
                #ax.set_title('Player 2 ' + plotTitle)

                # Set the graph limits and labels for both players
                ax.axes.set_xlim3d(0,1,emit=True)
                ax.axes.set_ylim3d(0,1,emit=True)
                ax.axes.set_zlim3d(0,1,emit=True)
                ax.axes.set_zlabel(zLabel,labelpad=0.7)
                ax.axes.set_ylabel(yLabel,labelpad=0.7)
                ax.axes.set_xlabel(xLabel,labelpad=0.7)
                
                # Graph for Value of Players
                yLabel, xLabel = GraphLabels2
                im2 = ax2[Trial].plot(Itr, V1, 'r-', label = "Player 1")
                im2 = ax2[Trial].plot(Itr, V2, 'b--', label = "Player 2")
                ax2[Trial].legend(loc="upper right")

                ax2[Trial].set_xlim(1,40000)
                ax2[Trial].set_ylim(-0.5,0.5)
                ax2[Trial].set_ylabel(yLabel)
                ax2[Trial].set_xlabel(xLabel)
                ax2[Trial].set_title(plotTitle)
                
        # Graphs are shown for each trial of games
        fig.colorbar(im, ax=ax, aspect=30,  cmap='jet' )
        # Update the title 
        if ExpectedValue:
            title += ' With Expected Value Term'
        fig.suptitle(title)
        plt.show()
