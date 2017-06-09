<template>
  <div>
    <filtered-author-list></filtered-author-list>
    <filtered-publisher-list></filtered-publisher-list>
    <auto-complete-book-post></auto-complete-book-post>
  </div>
</template>

<script>
  import AutoCompleteBookPost from '~components/bookRelated/AutoCompleteBookPost.vue'
  import FilteredAuthorList from '~components/authorRelated/FilteredAuthorList.vue'
  import FilteredPublisherList from '~components/publisherRelated/FilteredPublisherList.vue'

  export default {
    layout: 'default',
    components: {
      AutoCompleteBookPost,
      FilteredAuthorList,
      FilteredPublisherList
    }
  }
</script>

<style>

</style>
