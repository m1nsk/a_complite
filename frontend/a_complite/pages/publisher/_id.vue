<template>
    <div>
        <put-publisher-form></put-publisher-form>
    </div>
</template>

<script>
  import PutPublisherForm from '~components/publisherRelated/PutDeletePublisherForm.vue'
  export default {
    validate ({ params }) {
      // Must be a number
      return /^\d+$/.test(params.id)
    },
    components: {
      PutPublisherForm
    }
  }
</script>

<style>

</style>
