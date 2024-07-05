<template>
    <div id="app" class="container mx-auto p-4 flex-grow relative flex flex-col justify-center items-center w-full h-full">
      <div class="absolute top-4 right-4">
        <label class="switch">
          <input type="checkbox" @change="$emit('toggleDarkMode')" :checked="isDarkMode">
          <span class="slider round"></span>
        </label>
      </div>
      <h1 class="text-4xl font-bold mb-8 text-center">Blackjack</h1>
      <div class="game flex justify-around mb-8 w-full">
        <Hand title="Dealer's Hand" :cards="dealerHand" :total="dealerTotal" :isDarkMode="isDarkMode" />
        <Hand title="Your Hand" :cards="playerHand" :total="playerTotal" :isDarkMode="isDarkMode" />
      </div>
      <Controls @hit="hit" @stand="stand" @resetGame="resetGame" :gameOver="gameOver" />
      <Result :result="result" />
    </div>
  </template>
  
  <script>
  import Hand from '../components/Hand.vue';
  import Controls from '../components/Controls.vue';
  import Result from '../components/Result.vue';
  
  export default {
    components: {
      Hand,
      Controls,
      Result,
    },
    props: {
      isDarkMode: Boolean,
    },
    data() {
      return {
        deck: [],
        playerHand: [],
        dealerHand: [],
        gameOver: false,
        result: '',
      };
    },
    computed: {
      playerTotal() {
        return this.calculateHand(this.playerHand);
      },
      dealerTotal() {
        return this.calculateHand(this.dealerHand);
      }
    },
    methods: {
      initializeDeck() {
        const suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'];
        const symbols = {
          'Hearts': '♥',
          'Diamonds': '♦',
          'Clubs': '♣',
          'Spades': '♠'
        };
        const values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
        this.deck = [];
  
        for (let suit of suits) {
          for (let value of values) {
            this.deck.push({
              value: value,
              suit: suit,
              symbol: symbols[suit]
            });
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
          let value = card.value;
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
  .container {
    text-align: center;
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 100%;
    height: 100%; /* Ensure the container takes full height */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  .dark .container {
    background: #444;
    color: #fff; /* Ensure text is white in dark mode */
  }
  
  h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
  }
  
  .game {
    display: flex;
    justify-content: space-around;
    margin-bottom: 20px;
    width: 100%;
    min-height: 200px; /* Set a minimum height to prevent shifting */
  }
  
  .controls {
    margin: 20px 0;
  }
  
  .switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
  }
  
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: 0.4s;
    border-radius: 34px;
  }
  
  .slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: 0.4s;
    border-radius: 50%;
  }
  
  input:checked + .slider {
    background-color: #2196F3;
  }
  
  input:checked + .slider:before {
    transform: translateX(26px);
  }
  
  .slider.round {
    border-radius: 34px;
  }
  
  .slider.round:before {
    border-radius: 50%;
  }
  </style>
  