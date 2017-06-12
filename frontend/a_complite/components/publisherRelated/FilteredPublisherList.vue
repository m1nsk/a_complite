<template>
  <div>
    <auto-complete-publisher-input v-model="modelList" :callback="filterList" @option="onClicked" ></auto-complete-publisher-input>
  </div>
</template>

<script>
  import { getPublisherList } from '../../api/index.js'
  import AutoCompletePublisherInput from '~components/publisherRelated/AutoCompletePublisherInput.vue'
  export default {
    components: {
      AutoCompletePublisherInput
    },
    data () {
      return {
        modelList: {
          query: '',
          items: [],
          highlighted: 'name'
        },
        listData: []
      }
    },
    created: function () {
      var promise = getPublisherList()
      promise.then((response) => {
        for (var item in response.data) {
          this.listData.push(response.data[item])
        }
        this.filterList()
      })
    },
    methods: {
      filterList (input) {
        let list = []
        let pattern = new RegExp(input)
        this.listData.forEach((item) => {
          if (pattern.test(item.name) | !input) {
            list.push(item)
          }
        })
        this.modelList.items = list
      },
      onClicked (item) {
        this.$router.push(this.$route.path + '/' + item.id)
        this.modelList.author = item.id
      }
    }
  }
</script>

<style>

</style>
