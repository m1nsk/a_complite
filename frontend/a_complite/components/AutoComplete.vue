<template>
  <div>
    <auto-complete-input v-model="model" :callback="getQuery" @option="onOptionClicked"></auto-complete-input>
  </div>
</template>

<script>
  import { getAutoCopleteListQuery } from '../api/index.js'
  import AutoCompleteInput from '~components/AutoCompleteInput.vue'
  export default {
    data () {
      return {
        model: {
          query: '',
          items: []
        }
      }
    },
    components: {
      AutoCompleteInput
    },
    methods: {
      getQuery (input) {
        var promise = getAutoCopleteListQuery(input)
        promise.then((response) => {
          this.model.items = []
          console.log(response.data)
          for (var item in response.data) {
            console.log(item)
            this.model.items.push(response.data[item].fields)
          }
        }).catch(
          this.model.items = []
        )
      },
      onOptionClicked (item) {
        console.log(item.name)
      }
    }
  }
</script>

<style>

</style>
