
# 3 games (two player matrix) in one function using Reinforcement Learning
<br />

Useful bits of knowledge before start:
+ First of all, please read The Reinforcment Learning book in second edition from this link ["Sutton & Barto" ](https://www.dbooks.org/reinforcement-learning-0262039249/).
+ There are absolutely free resources for Reinforcement Learning in [here](https://medium.com/datadriveninvestor/absolutely-free-resources-for-reinforcement-learning-d16a5230cb0f).
+ Also if you want to work with MATLAB you can read this link [RL with MATLAB](https://github.com/MinaR-90/Self-Driving-Cab-Using-Reinforcement-Learning/issues/1) too. 
<br /><br /><br />

## Games' Description

In this project, we did three games in one function. These games or two-player matrix games include: <br /> 
**Prisoner’s Dilemma**, **Matching pennies** & **Rock-Paper-Scissors** <br /><br />


1) **``Prisoner’s Dilemma``**: It is a game involving two criminals that need to decide whether they will cooperate with the police and defect on the accomplice or whether they will
cooperate with the accomplice and lie to the police. The rewards for this game can be represented in matrices: 𝑅1 for player1, and 𝑅2 for player2. One example of reward matrix for this game is: <br /> 


<p align="center">
<img width="140" height="65" alt="1mat" src="https://user-images.githubusercontent.com/71558720/103111885-82f5a800-461f-11eb-8c23-55a24ccaa44c.PNG"><br />
<p align="center">


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Where the first row represents cooperation with the accomplice and lying to the police, whereas the second row represents defection and confession to the police. The rewards are from player1’s perspective. Therefore, if both players cooperate (element 𝑟1,1), both go to jail for a short period and have a large reward. If player1 cooperates and player2 does not, player1 goes to jail for several years and has a very small reward (element 𝑟1,2). If player1 confesses and player2 cooperates (element 𝑟1,2), player1 has a very large reward, i.e., it does not go to jail at all. Finally, if player1 and 2 confess (element 𝑟2,2), both of them have a small reward, i.e., they go to jail for a couple of years. It should be clear that the reward matrix for player 2 is: <br /> 

<p align="center">
<img width="175" height="66" alt="2mat" src="https://user-images.githubusercontent.com/71558720/103111884-82f5a800-461f-11eb-9dbe-cfd290a89a6b.PNG"><br />
<p align="center">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It turns out that this same approach can be used for several other games.<br /> <br /> 


2) **``Matching pennies``**: In this game the two players hold a penny each. They independently show one side of the penny (actions are “head” or “tail”). If both pennies show the same figure (two heads or two tails), player1 wins the penny and has a reward of 1. If the pennies show different figures, player2 wins the penny and player1 has a reward of -1. The reward matrix for player1 is;<br />

<p align="center">
<img width="155" height="57" alt="33" src="https://user-images.githubusercontent.com/71558720/103926500-ffd85580-50e6-11eb-9745-48107f8edd31.PNG"> 
<p align="center">
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then, player2’s reward matrix is 𝑅2 = −𝑅1. <br /> <br />  


3) **``Rock-Paper-Scissors``**: The idea for this game is to display your hand as either a rock, scissors, or paper. Then, paper covers rock, rock breaks scissors, and scissors cuts paper. If both players display the same thing, it is a tie. The reward matrix for player 1 is:

<p align="center">
<img width="155" height="67" alt="44" src="https://user-images.githubusercontent.com/71558720/103928504-edabe680-50e9-11eb-9d78-4d7e0ed0d9a4.PNG">
<p align="center">
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Again, player2’s reward matrix is 𝑅2 = −𝑅1. <br /> <br /> <br /> 



We implemented an algorithm to iteratively calculate the optimal policies and the value of the game for each player in all three games and also we use ``Python 3`` as Programming language to solve thease games in one function.<br />  <br /> 



## Algorithm

The algorithm is an every-visit update algorithm that does policy iteration. Observe that this is not an associative problem, therefore, states do not need to be represented. The update rules for each player 𝑗 are:

<p align="center">
<img width="520" height="80" alt="55" src="https://user-images.githubusercontent.com/71558720/103961884-7a26cb00-5123-11eb-891e-4ba84526c178.PNG">
<p align="center">
  
This algorithm works directly on the policies. We implemented the algorithm and for each one of the three games described above, calculate: 

a) The policies for each player. We show graphs in different initial policy distributions. We explain, If the policies calculated are optimal.
b) Modify the algorithm so another term is added:

<p align="center">
<img width="720" height="80" alt="66" src="https://user-images.githubusercontent.com/71558720/103961889-7c892500-5123-11eb-84ee-19d72f528b43.PNG">
<p align="center">

Then, we calculate the policies for each player. Also, we show graphs in different initial policy distributions. And, We explain If the policies calculated are optimal.

c) We show the value of the game and we also say why the results are different. <br /> <br /> <br /><br /> <br /> 


# Solving

## Introduction 

We should note that for all games, selected parameters are identical. The learning rate alpha = 0:01, the iteration is 40,000 and each Game is learned for 5 Trials. This provides the neater coding as well as better comparison. We also preferred to put the extra graphs for value trends in the end of this report which is provided for more information and is also useful to support some explanation. <br /> 

#### **Game 1 : Prisoner’s Dilemma**


+ Table 1 shows the initial and final policies for each player in 5 Trials. The figure below that shows the
policy trends for cooperation of both players. As we see the probability of Cooperation in both players
goes to zero which means the probability of Defection settles in 1.
+ Players are playing simultaneously without knowing each others actions. Although the policies converge,
the obtained results **are not** optimal. The reason is this policies do not results in achieving maximized
long-run rewards. We can also interpret that by looking at the Value figures in the last page. It is clear
that this values have not converged to a constant point, hence the taken policy is not optimal. One main
reason is the policy update for all games is a predefined function, which means the policies are not
determined such that the value function raises. The best reward seems to be obtained when Player 1
decides to Defect and Player 2 tends to Cooperate. This is not what we achieve in this policy iteration.
+ Adding the Expectation term leaves the final Policies unchanged.
+ As shown in Table 2 and the graph below, again the policies are not optimal because of the same reasons
mentioned in second item. The value in the last iteration is 1 for both players. This has been verified in 
the Simulation and also can be proved mathematically by calculating the accumulated rewards. The Value is obtained by
averaging the cumulative Rewards over the number of iteration to reach the final policy.
+ After adding the additional term, the final results in this game are the same, but the speed of convergence
decreases. That is mainly because of the lag created by the Expectation term in the update rule.


<p align="center">
<img width="850" height="260" alt="tabel1" src="https://user-images.githubusercontent.com/71558720/103963602-b0664980-5127-11eb-8a00-0ce50be3dcc9.PNG">
<p align="center"><br />  

______________________________________________________________________

<p align="center">
<img width="850" height="260" alt="table2" src="https://user-images.githubusercontent.com/71558720/103963607-b2c8a380-5127-11eb-9c5c-e2e43f292233.PNG">
<p align="center"><br /><br />
  
  
  
#### **Game 2 : Matching pennies**
  
  
- As illustrated in Table 3, the final policies converge to different values for different initial Policies. Hence
based on the policy update rule, there is no unique final Policy that Players can take in this game.  
- Policies are not optimal. The main reason is the fluctuation occurring in the policy values. This instability
is maintained and there is no consistent point that the Policy can settle in. It should be mentioned that
the optimal policy is the one makes the long-term reward maximized for both players. This is only
feasible when the probability of each action for each player become 50% i.e., pi = [0:5; 0:5].
- As given in Table 4 and Figure below, the probability of both player approximately converges to a
constant point.   
- This policy **is** optimal since the value function and policies converge. 
- Value for both players after adding the additional term are zero (in the end of this page). That both intuitively and
mathematically expected since the base case scenario is when the coin drops unbalanced. That give a
zero reward for both players.The increasing trend shows the optimal policy of the Game as well.
- Adding the new term in the update rule, helps the policies to learn easier although the learning time
increases. After enough iterations, both Players probability converges to 50% of selecting either actions.
That is mainly because the probability of an action will increase if it had good reward in the previous
steps.
  
  
<p align="center">
<img width="850" height="330" alt="table3" src="https://user-images.githubusercontent.com/71558720/103966423-d7277e80-512d-11eb-80f8-506661b3e57c.PNG">
<p align="center"><br />  

_______________________________________________________________________

<p align="center">
<img width="850" height="330" alt="table4" src="https://user-images.githubusercontent.com/71558720/103966424-d8f14200-512d-11eb-9f80-2cf345d818d4.PNG">
<p align="center"><br /><br />  
  
  
  
#### **Game 3 : Rock-Paper-Scissors**  
  
_ The Table 5 and the table below show the numerical results of for the final Policies with picking different
Initial Policies. Again, different final Policies are obtained for different Initial Policies which shows the
Policies do not converge to the unique. In this game, each Player can take 3 actions. To show a better
graphical results, the Policy distribution of each action for individual Players 1 and 2 in separate Figures.
_ Policies **are not** optimal. because again there is no points the final policy converge.
_
_
_
