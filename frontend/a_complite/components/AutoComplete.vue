<template>
  <div>
    <auto-complete-input v-model="author" :callback="getByAuthor" @option="onOptionClicked" title="Author"></auto-complete-input>
    <auto-complete-input v-model="publisher" :callback="getByPublisher" @option="onOptionClicked" title="Publisher"></auto-complete-input>
    <auto-complete-input v-model="book" :callback="getBookByResult" @option="onOptionClicked" title="Book"></auto-complete-input>
  </div>
</template>

<script>
  import { getBookByAuthor, getBookByPublisher } from '../api/index.js'
  import AutoCompleteInput from '~components/AutoCompleteInput.vue'
  export default {
    data () {
      return {
        author: {
          query: '1',
          items: []
        },
        publisher: {
          query: '2',
          items: []
        },
        book: {
          query: '3',
          items: []
        }
      }
    },
    components: {
      AutoCompleteInput
    },
    methods: {
      getByAuthor (input) {
        var promise = getBookByAuthor(input)
        promise.then((response) => {
          this.author.items = []
          for (var item in response.data) {
            console.log(response.data)
            this.author.items.push(response.data[item].fields)
          }
        }).catch(
          this.author.items = []
        )
      },
      getByPublisher (input) {
        var promise = getBookByPublisher(input)
        promise.then((response) => {
          this.publisher.items = []
          for (var item in response.data) {
            this.publisher.items.push(response.data[item].fields)
          }
        }).catch(
          this.publisher.items = []
        )
      },
      getBookByResult (input) {
        var result = this.author.items.concat(this.publisher.items)
        var pattern = new RegExp('(.)*' + input + '(.)*')
        result = result.filter((item) => { return pattern.test(item.name) })
        this.book.items = result
      },
      onOptionClicked (item) {
        console.log(item.name)
      }
    }
  }
</script>

<style>

</style>
