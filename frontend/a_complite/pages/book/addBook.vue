<template>
    <div>
        <filtered-author-list></filtered-author-list>
        <button @click="addAuthor">Add New</button>
    </div>
</template>

<script>
  import FilteredAuthorList from '~components/authorRelated/FilteredAuthorList.vue'
  export default {
    layout: 'default',
    components: {
      FilteredAuthorList
    },
    methods: {
      addAuthor () {
        this.$router.push('addBook')
      }
    }
  }
</script>

<style>

</style>
