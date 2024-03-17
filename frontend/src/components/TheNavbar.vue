<script setup>
const tabs = [
  { name: '소개', href: '/' },
  { name: '스터디', href: '/study' },
  {
    name: '노션',
    href: 'https://zzolab.notion.site/728c5e3b6a9c4caea41e3ce3c09c1eb4',
    isNewTab: true,
  },
  { name: '블로그', href: 'https://medium.com/zzolab', isNewTab: true },
]
</script>

<template>
  <div class="flex h-16 mx-auto w-full px-4 sm:px-6 lg:px-8 bg-white shadow">
    <a href="/" class="flex flex-shrink-0 items-center">
      <img class="h-8 w-auto" src="/img/ko_logo.png" />
    </a>

    <div class="mx-2 flex space-x-2 sm:ml-6 sm:space-x-8">
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
