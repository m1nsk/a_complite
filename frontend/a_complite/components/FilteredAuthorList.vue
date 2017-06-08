<template>
  <div>
    <auto-complete-author-input v-model="myList" :callback="filterList" @option="onClicked" ></auto-complete-author-input>
  </div>
</template>

<script>
  import { getAuthorList } from '../api/index.js'
  import AutoCompleteAuthorInput from '~components/AutoCompleteAuthorInput.vue'
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
      AutoCompleteAuthorInput
    },
    created: function () {
      var promise = getAuthorList()
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
        this.myList.author = item.author_id
      }
    }
  }
</script>

<style>

</style>
