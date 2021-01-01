
# 3-games-in-one-function--Reinforcement-Learning
<br />

## Description

In this project, we did three games in one function. These games or two-player matrix games include: <br /> 
**Prisoner’s Dilemma**, **Matching pennies** & **Rock-Paper-Scissors** <br />

Useful bits of knowledge before start:
<br /> 

1) **Prisoner’s Dilemma**: a game involving two criminals that need to decide whether they will cooperate with the police and defect on the accomplice or whether they will
cooperate with the accomplice and lie to the police. The rewards for this game can be represented in matrices: 𝑅1 for player 1, and 𝑅2 for player 2. One example of reward matrix for this game is: <br /> 


<p align="center">
<img width="140" height="65" alt="1mat" src="https://user-images.githubusercontent.com/71558720/103111885-82f5a800-461f-11eb-8c23-55a24ccaa44c.PNG"><br />
<p align="center">


Where the first row represents cooperation with the accomplice and lying to the police, whereas the second row represents defection and confession to the police. The rewards are from player 1’s perspective. Therefore, if both players cooperate (element 𝑟1,1), both go to jail for a short period and have a large reward. If player 1 cooperates and player 2 does not, player 1 goes to jail for several years and has a very small reward (element 𝑟1,2). If player 1 confesses and player 2 cooperates (element 𝑟1,2), player 1 has a very large reward, i.e., it does not go to jail at all. Finally, if player 1 and 2 confess (element 𝑟2,2), both of them have a small reward, i.e., they go to jail for a couple of years. It should be clear that the reward matrix for player 2 is: <br /> 

<p align="center">
<img width="185" height="76" alt="2mat" src="https://user-images.githubusercontent.com/71558720/103111884-82f5a800-461f-11eb-9dbe-cfd290a89a6b.PNG"><br />
<p align="center">

  
## Introduction 

I should note that for all games, selected parameters are identical. The learning rate alpha = 0:01, the iteration is 40,000 and each Game is learned for 5 Trials. This provides the neater coding as well as better comparison. I also preferred to put the extra graphs for value trends in page 4 which is provided for more information and
is also useful to support some explanation. 


