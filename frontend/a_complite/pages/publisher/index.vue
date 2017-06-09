<template>
    <div>
        <filtered-publisher-list class="iBlock"></filtered-publisher-list>
        <button @click="addPublisher" class="iBlock">Add New</button>
    </div>
</template>

<script>
  import FilteredPublisherList from '~components/publisherRelated/FilteredPublisherList.vue'
  export default {
    layout: 'default',
    components: {
      FilteredPublisherList
    },
    methods: {
      addPublisher () {
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
