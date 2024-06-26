<template>
  <div id="app" class="container mx-auto p-4">
    <h1 class="text-4xl font-bold mb-8">Blackjack</h1>
    <div class="game flex justify-around mb-8">
      <div class="hand bg-gray-100 p-4 rounded-lg shadow-md w-1/2 mr-2">
        <h2 class="text-xl font-semibold mb-4">Dealer's Hand</h2>
        <div v-for="card in dealerHand" :key="card" class="card bg-white border border-gray-300 rounded p-2 mb-2 shadow-sm">{{ card }}</div>
      </div>
      <div class="hand bg-gray-100 p-4 rounded-lg shadow-md w-1/2 ml-2">
        <h2 class="text-xl font-semibold mb-4">Your Hand</h2>
        <div v-for="card in playerHand" :key="card" class="card bg-white border border-gray-300 rounded p-2 mb-2 shadow-sm">{{ card }}</div>
      </div>
    </div>
    <div class="controls flex justify-center space-x-4 mb-8">
      <button @click="hit" :disabled="gameOver" class="button bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Hit</button>
      <button @click="stand" :disabled="gameOver" class="button bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600">Stand</button>
      <button @click="resetGame" class="button bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">New Game</button>
    </div>
    <div v-if="gameOver" class="result text-2xl font-bold text-center">
      <h2>{{ result }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      deck: [],
      playerHand: [],
      dealerHand: [],
      gameOver: false,
      result: ''
    };
  },
  methods: {
    initializeDeck() {
      const suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'];
      const values = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
      ];
      this.deck = [];

      for (let suit of suits) {
        for (let value of values) {
          this.deck.push(`${value} of ${suit}`);
        }
      }

      this.deck = this.shuffle(this.deck);
    },
    shuffle(deck) {
      for (let i = deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [deck[i], deck[j]] = [deck[j], deck[i]];
      }
      return deck;
    },
    drawCard() {
      return this.deck.pop();
    },
    calculateHand(hand) {
      let total = 0;
      let aces = 0;

      for (let card of hand) {
        let value = card.split(' ')[0];
        if (isNaN(value)) {
          if (value === 'A') {
            aces += 1;
            total += 11;
          } else {
            total += 10;
          }
        } else {
          total += parseInt(value);
        }
      }

      while (total > 21 && aces > 0) {
        total -= 10;
        aces -= 1;
      }

      return total;
    },
    hit() {
      this.playerHand.push(this.drawCard());
      if (this.calculateHand(this.playerHand) > 21) {
        this.result = 'You Busted!';
        this.gameOver = true;
      }
    },
    stand() {
      while (this.calculateHand(this.dealerHand) < 17) {
        this.dealerHand.push(this.drawCard());
      }
      this.checkWinner();
      this.gameOver = true;
    },
    checkWinner() {
      const playerTotal = this.calculateHand(this.playerHand);
      const dealerTotal = this.calculateHand(this.dealerHand);

      if (dealerTotal > 21 || playerTotal > dealerTotal) {
        this.result = 'You Win!';
      } else if (playerTotal < dealerTotal) {
        this.result = 'Dealer Wins!';
      } else {
        this.result = 'It\'s a Tie!';
      }
    },
    resetGame() {
      this.initializeDeck();
      this.playerHand = [this.drawCard(), this.drawCard()];
      this.dealerHand = [this.drawCard(), this.drawCard()];
      this.gameOver = false;
      this.result = '';
    }
  },
  created() {
    this.resetGame();
  }
};
</script>

<style scoped>
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f0f0f0;
  color: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

#app {
  text-align: center;
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.game {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.hand {
  background-color: #f9f9f9;
  padding: 15px;
  border-radius: 8px;
  width: 45%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  margin: 5px 0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.controls {
  margin: 20px 0;
}

.button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  margin: 5px;
}

.button:disabled {
  background-color: #6c757d;
}

.button.new-game {
  background-color: #28a745;
}

.result {
  margin-top: 20px;
  font-size: 1.5rem;
}
</style>
