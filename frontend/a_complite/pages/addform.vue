<template>
  <div>
    <nuxt-link to="/">Add Book</nuxt-link></p>
    <add-author-form></add-author-form>
    <add-publisher-form></add-publisher-form>
  </div>
</template>

<script>
  import AddAuthorForm from '~components/authorRelated/PostAuthorForm.vue'
  import AddPublisherForm from '~components/publisherRelated/PostPublisherForm.vue'

  export default {
    components: {
      AddAuthorForm,
      AddPublisherForm
    }
  }
</script>

<style>

</style>
