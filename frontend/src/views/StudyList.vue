<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/modules/study'

const categories = ref([])
const studies = ref([])

const statusClass = {
  모집중: 'bg-pink-50 text-pink-800',
  진행중: 'bg-green-50 text-green-800',
  종료: 'bg-gray-200 text-gray-700',
}

const categoryClass = {
  웹개발: 'bg-indigo-100 text-indigo-800',
  업무자동화: 'bg-yellow-100 text-yellow-800',
  데이터분석: 'bg-blue-100 text-blue-800',
  알고리즘: 'bg-red-100 text-red-800',
  컴퓨터과학: 'bg-purple-100 text-purple-800',
  머신러닝: 'bg-green-100 text-green-800',
  딥러닝: 'bg-pink-100 text-pink-800',
  기초: 'bg-orange-100 text-orange-800',
}

onMounted(async () => {
  const categoryResponse = await api.getCategorylist()
  categories.value = categoryResponse.data

  const studyResponse = await api.getStudylist()
  studies.value = studyResponse.data
})
</script>

<template>
  <div class="relative bg-gray-50 px-4 sm:px-6 lg:px-8 py-10">
    <div class="relative mx-auto max-w-7xl">
      <div class="text-center bg-white p-10">
        <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
          🏆 쪼랩 스터디 전당 🏆
        </h2>
        <p class="mx-auto max-w-2xl text-xl text-gray-500 mt-6">
          2022년부터 시작된 쪼랩의 역대 스터디들을 소개합니다.
        </p>
      </div>

      <div class="flex flex-wrap items-center justify-center space-x-10">
        <span
          v-for="category in categories"
          :key="category.id"
          :class="[
            categoryClass[category.name],
            'inline-flex items-center rounded-md px-2 py-1 text-sm font-medium ring-1 ring-inset ring-gray-500/10 mt-10',
          ]"
          >{{ category.name }}
        </span>
      </div>

      <div
        class="mx-auto mt-16 grid gap-5 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
      >
        <div
          v-for="study in studies"
          :key="study.id"
          class="flex flex-col overflow-hidden rounded-lg shadow-lg bg-white"
        >
          <div class="flex flex-col space-y-6 justify-between bg-white p-6">
            <div class="flex justify-between">
              <span
                :class="[
                  categoryClass[study.category.name],
                  'inline-flex items-center rounded-md px-2 py-1 text-xs font-medium ring-1 ring-inset ring-gray-500/10',
                ]"
                >{{ study.category.name }}</span
              >

              <span
                :class="[
                  statusClass[study.status],
                  'inline-flex items-center rounded-md px-2 py-1 text-xs font-medium ring-1 ring-inset ring-gray-500/10',
                ]"
                >{{ study.status }}</span
              >
            </div>

            <p class="text-2xl font-bold text-gray-900 ml-1 p-2">
              {{ study.title }}
            </p>

            <div class="h-24 bg-gray-50 overflow-y-auto px-2">
              <p class="mt-3 text-base text-gray-500">
                {{ study.description }}
              </p>
            </div>

            <div class="p-2 flex flex-col space-y-3">
              <span class="text-gray-800">{{ study.leader }} </span>

              <div class="flex space-x-1 text-sm text-gray-500 mt-2">
                <time>
                  {{ study.start_date }} ~
                  {{ study.end_date ? study.end_date : '' }}
                </time>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
