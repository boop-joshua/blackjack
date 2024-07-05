<template>
    <div class="card animated" :class="`suit-${card.suit}`">
      <div class="card-content">
        <div class="card-value top">{{ card.value }}</div>
        <div class="card-suit">{{ card.symbol }}</div>
        <div class="card-value bottom">{{ card.value }}</div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      card: Object,
      isDarkMode: Boolean,
    },
  };
  </script>
  
  <style scoped>
  .card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    width: 60px;
    height: 90px;
    margin: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.3s ease;
  }
  
  .card.animated {
    animation: draw-card 0.5s ease-out;
  }
  
  @keyframes draw-card {
    from {
      transform: translateY(-20px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
  
  .dark .card {
    background-color: #666;
    border: 1px solid #444;
  }
  
  .card-content {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: bold;
  }
  
  .card-value {
    position: absolute;
  }
  
  .card-value.top {
    top: 5px;
    left: 5px;
  }
  
  .card-value.bottom {
    bottom: 5px;
    right: 5px;
  }
  
  .suit-Hearts .card-value,
  .suit-Hearts .card-suit,
  .suit-Diamonds .card-value,
  .suit-Diamonds .card-suit {
    color: red;
  }
  
  .suit-Clubs .card-value,
  .suit-Clubs .card-suit,
  .suit-Spades .card-value,
  .suit-Spades .card-suit {
    color: black;
  }
  </style>
  