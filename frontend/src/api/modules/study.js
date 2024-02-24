import myAxios from '@/api/setAxios'
import urls from '@/api/urls'

export default {
    getStudylist() {
    return myAxios.get(urls.studyList)
  },
}
