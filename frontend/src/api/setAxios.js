import axios from 'axios'
import urls from '@/api/urls'

function createAxiosInstance(baseUrl, timeOut) {
  const axiosInstance = axios.create({
    baseURL: baseUrl,
    timeout: timeOut,
  })
  return axiosInstance
}

function setInterceptors(axiosInstance) {
//   axiosInstance.interceptors.request.use()

//   axiosInstance.interceptors.response.use()

  return axiosInstance
}

const myAxios = setInterceptors(createAxiosInstance(urls.Django_API, 1000))

export default myAxios
