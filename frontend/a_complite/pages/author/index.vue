<template>
    <div>
        <filtered-author-list-server-side @author="selectAuthor"></filtered-author-list-server-side>
        <button @click="addAuthor" class="iBlock">Add New</button>
    </div>
</template>

<script>
  import FilteredAuthorListServerSide from '~components/authorRelated/FilteredAuthorListServerSide.vue'
  import FilteredAuthorList from '~components/authorRelated/FilteredAuthorList.vue'
  export default {
    layout: 'default',
    components: {
      FilteredAuthorList,
      FilteredAuthorListServerSide
    },
    methods: {
      addAuthor () {
        this.$router.push(this.$route.path + '/' + 'add')
      },
      selectAuthor (item) {
        this.$router.push(this.$route.path + '/' + item.id)
      }
    }
  }
</script>

<style>
    .iBlock{
        display: inline-block;
    }
</style>
