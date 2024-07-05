<template>
    <div class="result text-2xl font-bold text-center h-16 flex items-center justify-center">
      <h2>{{ result }}</h2>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      result: String,
    },
  };
  </script>
  
  <style scoped>
  .result {
    margin-top: 20px;
    font-size: 1.5rem;
    height: 4rem; /* Fixed height to prevent movement */
    display: flex;
    align-items: center;
    justify-content: center;
  }
  </style>
  