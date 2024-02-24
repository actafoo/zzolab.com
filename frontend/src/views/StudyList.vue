<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api/modules/study'

const studies = ref([])

onMounted(async () => {
  const response = await api.getStudylist()
  studies.value = response.data
})
</script>
