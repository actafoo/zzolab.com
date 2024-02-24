import myAxios from '@/api/setAxios'
import urls from '@/api/urls'

export default {
  getCategorylist() { 
    return myAxios.get(urls.categoryList)
  },

    getStudylist() {
    return myAxios.get(urls.studyList)
  },
}
