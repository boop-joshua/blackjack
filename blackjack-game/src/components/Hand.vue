<template>
    <div class="hand bg-gray-100 dark:bg-gray-800 p-4 rounded-lg shadow-md w-1/2 mx-2">
      <h2 class="text-xl font-semibold mb-4 text-center">{{ title }}</h2>
      <div class="card-container">
        <Card v-for="card in cards" :key="card.value + card.suit" :card="card" :isDarkMode="isDarkMode" />
      </div>
      <div class="total mt-4 text-lg font-semibold text-center">Total: {{ total }}</div>
    </div>
  </template>
  
  <script>
  import Card from './Card.vue';
  
  export default {
    components: {
      Card,
    },
    props: {
      title: String,
      cards: Array,
      total: Number,
      isDarkMode: Boolean,
    },
  };
  </script>
  
  <style scoped>
  .hand {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 8px;
    width: 45%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    min-height: 250px; /* Ensure consistent height */
  }
  
  .dark .hand {
    background-color: #555;
  }
  
  .card-container {
    display: flex;
    flex-wrap: nowrap; /* Prevent cards from wrapping */
    justify-content: center;
    align-items: center;
    overflow-x: auto; /* Allow horizontal scrolling if needed */
  }
  </style>
  