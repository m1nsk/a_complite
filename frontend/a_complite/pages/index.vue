<template>
  <div>
    <p><nuxt-link to="/addform">Add new book</nuxt-link></p>
    <auto-complete></auto-complete>
  </div>
</template>

<script>
  import AutoComplete from '~components/AutoComplete.vue'

  export default {
    components: {
      AutoComplete
    }
  }
</script>

<style>

</style>
