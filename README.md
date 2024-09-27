# Blackjack Game

Welcome to the Blackjack Game implemented using Vue.js! This repository contains the source code for a Blackjack game I created.

## How to Download and Use This Code

### Prerequisites

- **Node.js**: Make sure you have Node.js installed on your machine. You can download it from [nodejs.org](https://nodejs.org/).

### Steps to Download and Run the Code

1. **Clone the Repository**

   Open your terminal or command line interface and run the following command to clone the repository:

   ```bash
   git clone https://github.com/your-username/blackjack-game.git

  Navigate to the project directory:
  ```bash
  cd blackjack-game
```
2. Install Dependencies
```bash
npm install
```
3. Run the dev server
```bash
npm run serve
```
4. Open the application
Open your web browser and navigate to http://localhost:8080 to see the application in action.

**How to Play Blackjack**
The objective of Blackjack is to beat the dealer by having a hand value closer to 21 without exceeding 21.

Basic Rules
Each card has a value:

Number cards are worth their face value.
Face cards (King, Queen, Jack) are worth 10.
Aces can be worth 1 or 11, depending on which value benefits the hand more.
Players are dealt two cards at the start of the game. The dealer also gets two cards, with one card face up and one card face down.

Players can choose to "Hit" (take another card) or "Stand" (end their turn).

If the player's hand exceeds 21, they "Bust" and lose the game.

Once the player stands, the dealer reveals their hidden card and must hit until their hand value is at least 17.

The player wins if their hand value is closer to 21 than the dealer's hand, or if the dealer busts.

Controls
Hit: Draw a card.
Stand: End your turn.
New Game: Start a new game.


If you want to add a PR, follow the steps below:

```bash
git checkout master
git pull origin master
git add .
git commit -m
git push origin master
```
