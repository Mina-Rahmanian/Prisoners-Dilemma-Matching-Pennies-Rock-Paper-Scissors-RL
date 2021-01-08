
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


&nbsp;&nbsp;Where the first row represents cooperation with the accomplice and lying to the police, whereas the second row represents defection and confession to the police. The rewards are from player1’s perspective. Therefore, if both players cooperate (element 𝑟1,1), both go to jail for a short period and have a large reward. If player1 cooperates and player2 does not, player1 goes to jail for several years and has a very small reward (element 𝑟1,2). If player1 confesses and player2 cooperates (element 𝑟1,2), player1 has a very large reward, i.e., it does not go to jail at all. Finally, if player1 and 2 confess (element 𝑟2,2), both of them have a small reward, i.e., they go to jail for a couple of years. It should be clear that the reward matrix for player 2 is: <br /> 

<p align="center">
<img width="175" height="66" alt="2mat" src="https://user-images.githubusercontent.com/71558720/103111884-82f5a800-461f-11eb-9dbe-cfd290a89a6b.PNG"><br />
<p align="center">

It turns out that this same approach can be used for several other games.<br /> <br /> 


2) **``Matching pennies``**: In this game the two players hold a penny each. They independently show one side of the penny (actions are “head” or “tail”). If both pennies show the same figure (two heads or two tails), player1 wins the penny and has a reward of 1. If the pennies show different figures, player2 wins the penny and player1 has a reward of -1. The reward matrix for player1 is;<br />

<p align="center">
<img width="155" height="57" alt="33" src="https://user-images.githubusercontent.com/71558720/103926500-ffd85580-50e6-11eb-9745-48107f8edd31.PNG"> 
<p align="center">
  
Then, player2’s reward matrix is 𝑅2 = −𝑅1. <br /> <br />  


3) **``Rock-Paper-Scissors``**: The idea for this game is to display your hand as either a rock, scissors, or paper. Then, paper covers rock, rock breaks scissors, and scissors cuts paper. If both players display the same thing, it is a tie. The reward matrix for player 1 is:

<p align="center">
<img width="155" height="67" alt="44" src="https://user-images.githubusercontent.com/71558720/103928504-edabe680-50e9-11eb-9d78-4d7e0ed0d9a4.PNG">
<p align="center">
  
Again, player2’s reward matrix is 𝑅2 = −𝑅1. <br />  <br /> 


We implemented an algorithm to iteratively calculate the optimal policies and the value of the game for each player in all three games and also we use ``Python 3`` as Programming language to solve thease games in one function.<br />  <br /> 



## Algorithm

The algorithm is an every-visit update algorithm that does policy iteration. Observe that this is not an associative problem, therefore, states do not need to be represented. The update rules for each player 𝑗 are:

<p align="center">
<img width="520" height="80" alt="55" src="https://user-images.githubusercontent.com/71558720/103961884-7a26cb00-5123-11eb-891e-4ba84526c178.PNG">
<p align="center">
  
  

## Introduction 

I should note that for all games, selected parameters are identical. The learning rate alpha = 0:01, the iteration is 40,000 and each Game is learned for 5 Trials. This provides the neater coding as well as better comparison. I also preferred to put the extra graphs for value trends in the end of this report which is provided for more information and
is also useful to support some explanation. 













