<template>
    <div>
        <put-delete-publisher-form></put-delete-publisher-form>
    </div>
</template>

<script>
  import PutDeletePublisherForm from '~components/publisherRelated/PutDeletePublisherForm.vue'
  export default {
    validate ({ params }) {
      // Must be a number
      return /^\d+$/.test(params.id)
    },
    components: {
      PutDeletePublisherForm
    }
  }
</script>

<style>

</style>
