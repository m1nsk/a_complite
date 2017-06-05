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
          items: [],
          highlighted: 'author'
        },
        publisher: {
          query: '2',
          items: [],
          highlighted: 'publisher'
        },
        book: {
          query: '3',
          items: [],
          highlighted: 'name'
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
          console.log(response.data)
          this.author.items = []
          for (var item in response.data) {
            console.log(response.data)
            this.author.items.push(response.data[item])
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
            this.publisher.items.push(response.data[item])
          }
        }).catch(
          this.publisher.items = []
        )
      },
      getBookByResult (input) {
        var result = this.author.items.concat(this.publisher.items)
        var pattern = new RegExp('(.)*' + input + '(.)*')
        result = arrayUnique(result, 'name')
        result = result.filter((item) => { return pattern.test(item.name) })
        this.book.items = result

        function arrayUnique (array, key) {
          var arrDict = {}
          var result = []
          for (var index in array) {
            if (!(array[index][key] in arrDict)) {
              arrDict[array[index][key]] = true
              result.push(array[index])
            }
          }
          return result
        }
      },
      onOptionClicked (item) {
        console.log(item.name)
      }
    }
  }
</script>

<style>

</style>
