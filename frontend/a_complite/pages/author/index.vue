<template>
    <div>
        <filtered-author-list class="iBlock"></filtered-author-list>
        <button @click="addAuthor" class="iBlock">Add New</button>
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
          this.$router.push(this.$route.path + '/' + 'add')
        }
      }
    }
</script>

<style>
    .iBlock{
        display: inline-block;
    }
</style>
