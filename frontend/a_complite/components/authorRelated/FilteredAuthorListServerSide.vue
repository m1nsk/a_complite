<template>
    <div class="authorList">
        <auto-complete-author-input v-model="modelList" :callback="filterList" @option="onClicked" ></auto-complete-author-input>
    </div>
</template>

<script>
  import { getAuthorByName } from '../../api/index.js'
  import AutoCompleteAuthorInput from '~components/authorRelated/AutoCompleteAuthorInput.vue'
  export default {
    props: ['init'],
    data () {
      return {
        defaultList: {
          query: '',
          items: [],
          highlighted: 'name'
        }
      }
    },
    components: {
      AutoCompleteAuthorInput
    },
    methods: {
      filterList (input) {
        this.modelList.query = input
        this.$emit('publisher', '')
        let promise = getAuthorByName({'input': input})
        promise.then((response) => {
          this.modelList.items = response.data
        })
      },
      onClicked (item) {
        this.$emit('author', item)
      }
    },
    computed: {
      modelList () {
        if (this.init) {
          return this.init
        }
        return this.defaultList
      }
    }
  }
</script>

<style>
.authorList{
    display: inline-block;
}
</style>
