<script>
import Typed from 'typed.js'

document.addEventListener('DOMContentLoaded', () => {
  new Typed('#typed', {
    strings: [
      'print("Hello, World!")',
      'print("Hello, Teachers!")',
      'print("Hello, Developers!")',
    ],
    typeSpeed: 50,
    backSpeed: 30,
    loop: true,
  })
})
</script>

<template>
  <div class="mx-auto max-w-7xl px-4 sm:mt-24 sm:px-6">
    <div class="text-center">
      <h1
        class="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl"
      >
        <span class="block">쪼랩</span>
        <span class="block md:text-5xl text-sky-500 mt-4"
          >선생님🧑🏻‍🏫 <span class="text-gray-400">+</span>
          IT전문가🧑🏻‍💻 커뮤니티
        </span>
      </h1>
      <p
        class="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl"
      >
        코딩에 관심이 있는 공교육 <strong>선생님</strong>과 공교육에 관심이 있는
        <strong>IT전문가</strong>가<br />함께 모여 배우고, 성장하고, 기여하는
        <strong>커뮤니티</strong>
      </p>
    </div>

    <div class="terminal-window mx-auto relative max-w-2xl mb-24 top-24">
      <header>
        <div class="terminal-button terminal-button-green"></div>
        <div class="terminal-button terminal-button-yellow"></div>
        <div class="terminal-button terminal-button-red"></div>
      </header>
      <section class="terminal">
        <span id="typed"></span>
      </section>
    </div>
  </div>
</template>

<style scoped>
@import '@/assets/css/terminal.scss';
</style>
