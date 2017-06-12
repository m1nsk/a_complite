<template>
    <div>
        <auto-complete-book-put-server-side></auto-complete-book-put-server-side>
    </div>
</template>

<script>
  import AutoCompleteBookPutServerSide from '~components/bookRelated/AutoCompleteBookPutServerSide.vue'
  export default {
    layout: 'default',
    validate ({ params }) {
      // Must be a number
      return /^\d+$/.test(params.id)
    },
    components: {
      AutoCompleteBookPutServerSide
    }
  }
</script>

<style>

</style>
