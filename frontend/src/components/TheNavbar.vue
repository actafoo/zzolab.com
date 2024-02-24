<script setup>
const tabs = [
  { name: '운영진 소개', href: '/' },
  { name: '스터디 소개', href: '/' },
  {
    name: '노션',
    href: 'https://surish.notion.site/e0f18c1af4f64ecab7f68463fa666726',
    isNewTab: true,
  },
  { name: '블로그', href: 'https://medium.com/zzolab', isNewTab: true },
]
</script>

<template>
  <div class="flex h-16 mx-auto w-full px-4 sm:px-6 lg:px-8 bg-white shadow">
    <div class="flex flex-shrink-0 items-center">
      <img class="h-8 w-auto" src="/img/ko_logo.png" />
    </div>

    <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
      <a
        v-for="tab in tabs"
        :key="tab.name"
        :href="tab.href"
        :target="tab.isNewTab ? '_blank' : '_self'"
        :class="[
          false ? 'border-b-2 border-indigo-500' : '',
          'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium',
        ]"
      >
        {{ tab.name }}
      </a>
    </div>
  </div>
</template>
