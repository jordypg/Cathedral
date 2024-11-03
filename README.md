## INTRODUCTION:
Cathedral is a deterministic board game in which players take turns placing pieces on a board, trying to block their opponent from doing the same. It is simple to learn and difficult to master, but as a relatively unknown game, I don't have enough people to play with at a high level!

The mission goal is simple: create an agent that can beat me at Cathedral.

## CHALLENGES:
The traditional technique for playing deterministic turn-based board games that stretch over many turns is Monte Carlo Tree search. The most recent major success of Monte Carlo was for Google Deepmind's AlphaGo. Go took longer to beat the human benchmark compared to other similar games (e.g. Chess) in part because of its large branching factor. There are 361 squares on a Go board – there are 2,141 possible first moves in Cathedral<sup>*</sup>. This means that traditional techniques will need to be modified to solve this problem.

To make matters worse, engines like AlphaGo and Stockfish relied on training from vast training sets of sample games. As much as I would personally love there to be, there is nothing of the sort for Cathedral.

## PLAN:
Fortunately, I am afforded the benefit of a deterministic space. For MDP problems, Q-Learning is the standard prescription. My current plan is to implement a modified version of Deep-Q Learning or Approximate Q-Learning. Normal Q-Learning struggles with larger state and action spaces, and both of these spaces are far beyond the scope for which Q-Learning could be feasable.

This doesn't mean that MCTS is off the table. The problem of Cathedral is similar enough to Go that it would make a lot of sense to try it. I would need to use my knowledge of the state space to reduce the number of nodes via some sort of manual weighting and a very quick pruning algorithm, but I would like the agent's play to arise as naturally as possible, so I am hesistant about this.

There is one more hidden concern – updating the board and calculating ownership can be computationally expensive, which would make the act of playing out each leaf with MCTS slow. My current work is on implementing the game in as lightweight a way as possible.


I hope to become the world's greatest Cathedral player, but I'll need a superhuman training partner to get there!
- Jordan

<sup>*</sup>slightly fewer, depending on the placement of the cathedral
