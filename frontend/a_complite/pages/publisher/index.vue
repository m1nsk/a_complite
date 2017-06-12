<template>
    <div>
        <filtered-publisher-list-server-side @publisher="selectPublisher"></filtered-publisher-list-server-side>
        <button @click="addPublisher" class="iBlock">Add New</button>
    </div>
</template>

<script>
  import FilteredPublisherListServerSide from '~components/publisherRelated/FilteredPublisherListServerSide.vue'
  import FilteredPublisherList from '~components/publisherRelated/FilteredPublisherList.vue'
  export default {
    layout: 'default',
    components: {
      FilteredPublisherList,
      FilteredPublisherListServerSide
    },
    methods: {
      addPublisher () {
        this.$router.push(this.$route.path + '/' + 'add')
      },
      selectPublisher (item) {
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
