<template>
  <div>
    <auto-complete-input v-model="author" :callback="getByAuthor" @option="onAuthorClicked" title="Author"></auto-complete-input>
    <auto-complete-input v-model="publisher" :callback="getByPublisher" @option="onPublisherClicked" title="Publisher"></auto-complete-input>
  </div>
</template>

<script>
  import { getBookByField, baseHost } from '../api/index.js'
  import AutoCompleteInput from '~components/AutoCompleteInput.vue'
  export default {
    data () {
      return {
        author: {
          query: '',
          items: [],
          highlighted: 'author'
        },
        publisher: {
          query: '',
          items: [],
          highlighted: 'publisher'
        },
        formModel: {
          author: '',
          publisher: ''
        }
      }
    },
    components: {
      AutoCompleteInput
    },
    methods: {
      getByAuthor (input) {
        this.formModel.author = ''
        this.getByField(input, 'author')
      },
      getByPublisher (input) {
        this.formModel.publisher = ''
        this.getByField(input, 'publisher')
      },
      getByField (input, field) {
        var data = {
          input: input,
          field: field
        }
        var promise = getBookByField(data)
        promise.then((response) => {
          this[field].items = []
          for (var item in response.data) {
            response.data[item]['image'] = baseHost + response.data[item]['image']
            response.data[item]['author'] = response.data[item]['author']['name']
            response.data[item]['publisher'] = response.data[item]['publisher']['name']
            this[field].items.push(response.data[item])
          }
          console.log(this[field].items)
        }).catch(
          this[field].items = []
        )
      },
      onAuthorClicked (item) {
        this.formModel.author = item.author_id
        this.updateFilterBook()
      },
      onPublisherClicked (item) {
        this.formModel.publisher = item.publisher_id
        this.updateFilterBook()
      },
      updateFilterBook () {
        this.$emit('filterBook', {
          author: this.formModel.author,
          publisher: this.formModel.publisher
        })
      }
    }
  }
</script>

<style>

</style>
