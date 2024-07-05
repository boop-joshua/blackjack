<template>
  <div :class="{ dark: isDarkMode }" class="min-h-screen flex flex-col">
    <Blackjack :isDarkMode="isDarkMode" @toggleDarkMode="toggleDarkMode" />
  </div>
</template>

<script>
import Blackjack from './views/Blackjack.vue';

export default {
  components: {
    Blackjack,
  },
  data() {
    return {
      isDarkMode: false,
    };
  },
  methods: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
    },
  },
};
</script>

<style>
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f0f0f0;
  color: #333;
  margin: 0;
  height: 100vh; /* Ensure the body takes full height */
  width: 100vw; /* Ensure the body takes full width */
  overflow: hidden; /* Remove any scrollbar */
}

.dark body {
  background-color: #333;
  color: #fff;
}
</style>
