<template>
  <div>
    <auto-complete-publisher-input v-model="myList" :callback="filterList" @option="onClicked" ></auto-complete-publisher-input>
  </div>
</template>

<script>
  import { getPublisherList } from '../api/index.js'
  import AutoCompletePublisherInput from '~components/AutoCompletePublisherInput.vue'
  export default {
    data () {
      return {
        myList: {
          query: '',
          items: [],
          highlighted: 'name'
        },
        listData: []
      }
    },
    components: {
      AutoCompletePublisherInput
    },
    created: function () {
      var promise = getPublisherList()
      promise.then((response) => {
        for (var item in response.data) {
          this.listData.push(response.data[item])
        }
      })
    },
    methods: {
      filterList (input) {
        let list = []
        let pattern = new RegExp(input)
        this.listData.forEach((item) => {
          if (pattern.test(item.name)) {
            list.push(item)
          }
        })
        this.myList.items = list
      },
      onClicked (item) {
        this.myList.publisher = item.publisher_id
      }
    }
  }
</script>

<style>

</style>
