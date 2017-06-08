<template>
  <div>
    <p><nuxt-link to="/addform">Add new book</nuxt-link></p>
    <filtered-author-list></filtered-author-list>
    <filtered-publisher-list></filtered-publisher-list>
    <auto-complete></auto-complete>
  </div>
</template>

<script>
  import AutoComplete from '~components/AutoComplete.vue'
  import FilteredAuthorList from '~components/FilteredAuthorList.vue'
  import FilteredPublisherList from '~components/FilteredPublisherList.vue'

  export default {
    components: {
      AutoComplete,
      FilteredAuthorList,
      FilteredPublisherList
    }
  }
</script>

<style>

</style>
