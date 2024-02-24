const DjangoBase = import.meta.env.PROD ? '' : 'http://127.0.0.1:8000'

export default {
    Django_API: `${DjangoBase}/api/`,

    /* Study */
    categoryList: 'study/category',
    studyList: 'study/list'
}