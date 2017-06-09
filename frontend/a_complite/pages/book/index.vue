<template>
    <div>
        <filtered-author-list></filtered-author-list>
    </div>
</template>

<script>
    import FilteredAuthorList from '~components/authorRelated/FilteredAuthorList.vue'
    export default {
      layout: 'default',
      components: {
        FilteredAuthorList
      }
    }
</script>

<style>

</style>
