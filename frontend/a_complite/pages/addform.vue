<template>
  <div>
    <nuxt-link to="/">Add Book</nuxt-link></p>
    <add-author-form></add-author-form>
    <add-publisher-form></add-publisher-form>
  </div>
</template>

<script>
  import AddAuthorForm from '~components/AddAuthorForm.vue'
  import AddPublisherForm from '~components/AddPublisherForm.vue'

  export default {
    components: {
      AddAuthorForm,
      AddPublisherForm
    }
  }
</script>

<style>

</style>
