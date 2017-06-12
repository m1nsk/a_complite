<template>
  <div>
    <filtered-by-author-by-publisher-book-list></filtered-by-author-by-publisher-book-list>
  </div>
</template>

<script>
  import FilteredByAuthorByPublisherBookList from '~components/bookRelated/FilteredByAuthorByPublisherBookList.vue'

  export default {
    layout: 'default',
    components: {
      FilteredByAuthorByPublisherBookList
    }
  }
</script>

<style>

</style>
