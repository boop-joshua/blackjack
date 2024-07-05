<template>
    <div class="controls flex justify-center space-x-4 mb-8">
      <button @click="$emit('hit')" :disabled="gameOver" class="button bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Hit</button>
      <button @click="$emit('stand')" :disabled="gameOver" class="button bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600">Stand</button>
      <button @click="$emit('resetGame')" class="button bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">New Game</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      gameOver: Boolean,
    },
  };
  </script>
  
  <style scoped>
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
  </style>
  