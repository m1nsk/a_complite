<template>
  <div>
    <filtered-author-list></filtered-author-list>
    <filtered-publisher-list></filtered-publisher-list>
    <auto-complete></auto-complete>
  </div>
</template>

<script>
  import AutoComplete from '~components/bookRelated/AutoCompleteBookPost.vue'
  import FilteredAuthorList from '~components/authorRelated/FilteredAuthorList.vue'
  import FilteredPublisherList from '~components/publisherRelated/FilteredPublisherList.vue'

  export default {
    layout: 'default',
    components: {
      AutoComplete,
      FilteredAuthorList,
      FilteredPublisherList
    }
  }
</script>

<style>

</style>
