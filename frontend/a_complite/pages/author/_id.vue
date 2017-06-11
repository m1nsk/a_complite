<template>
    <div>
        <put-author-form></put-author-form>
    </div>
</template>

<script>
  import PutAuthorForm from '~components/authorRelated/PutDeleteAuthorForm.vue'
  export default {
    validate ({ params }) {
      // Must be a number
      return /^\d+$/.test(params.id)
    },
    components: {
      PutAuthorForm
    }
  }
</script>

<style>

</style>
