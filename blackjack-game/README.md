# Blackjack Game

This is a simple Blackjack game implemented using Vue.js. The game includes both player and dealer hands, with functionalities to hit, stand, and start a new game. The game also supports dark mode.

## Overview

- **Framework**: Vue.js
- **Styling**: Tailwind CSS
- **Functionality**: Hit, Stand, New Game, Dark Mode

## Changes Made Today

### 1. Improved Layout Stability

- **Issue**: The player and dealer hand components shifted up when the player busted or the result was displayed.
- **Solution**: Added fixed heights to the hand components and result component to ensure the layout remains static.

### 2. Improved Dark Mode Visibility

- **Issue**: The cards and text were not clearly visible in dark mode.
- **Solution**: Updated the styling to ensure better visibility in dark mode by adjusting card and text colors.

### 3. Horizontal Display of Cards

- **Change**: Modified the hand components to display cards horizontally instead of vertically to save space.

### 4. Adjusted Main Frame

- **Change**: Ensured the main game container fills the entire viewport for a better user experience.

### 5. Added Dark/Light Mode Toggle

- **Feature**: Added a modernized switch for toggling between dark and light modes. The switch is located in the top-right corner of the screen.

## How to Run the Project

### Prerequisites

- Node.js and npm installed on your machine

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/boop-joshua/blackjack-game.git
   cd blackjack-game
  
2. Install dependencies
   ```bash
   npm install

3. Run the development server
  ```bash
  npm run serve
  ```
4. Open browser
   Navigate to http://localhost:8080 to see the application in action.

Project Structure:

```text
src/
├── assets/
│   └── styles/
│       └── main.css
├── components/
│   ├── Card.vue
│   ├── Hand.vue
│   ├── Controls.vue
│   └── Result.vue
├── views/
│   └── Blackjack.vue
├── App.vue
└── main.js
```
Components
Card.vue: Represents a single card.
Hand.vue: Represents a hand of cards (either dealer's or player's hand).
Controls.vue: Contains the control buttons (Hit, Stand, New Game).
Result.vue: Displays the game result (e.g., "You Busted!", "You Win!", "Dealer Wins!").


