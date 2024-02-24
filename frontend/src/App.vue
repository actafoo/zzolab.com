<script setup>
import TheFooter from '@/components/TheFooter.vue'
import TheNavbar from '@/components/TheNavbar.vue'
</script>

<template>
  <div class="App">
    <nav>
      <TheNavbar />
    </nav>
    <main class="dark:bg-gray-900 py-16">
      <router-view />
    </main>
    <footer>
      <TheFooter />
    </footer>
  </div>
</template>

<style scoped>
nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 10;
}

footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  z-index: 10;
}
</style>
