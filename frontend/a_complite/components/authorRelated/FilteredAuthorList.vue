<template>
  <div>
    <auto-complete-author-input v-model="modelList" :callback="filterList" @option="onClicked" ></auto-complete-author-input>
  </div>
</template>

<script>
  import { getAuthorList } from '../../api/index.js'
  import AutoCompleteAuthorInput from '~components/authorRelated/AutoCompleteAuthorInput.vue'
  export default {
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
    components: {
      AutoCompleteAuthorInput
    },
    created: function () {
      var promise = getAuthorList()
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
