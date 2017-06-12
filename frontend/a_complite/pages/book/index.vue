<template>
    <div>
        <filtered-publisher-list-server-side @publisher="selectPublisher"></filtered-publisher-list-server-side>
        <filtered-author-list-server-side @author="selectAuthor"></filtered-author-list-server-side>
        <auto-complete-book-input v-model="book" :callback="filterBookList" @option="bookSelected"></auto-complete-book-input>
        <button @click="addBook">add New</button>
    </div>
</template>

<script>
  import FilteredAuthorListServerSide from '~components/authorRelated/FilteredAuthorListServerSide.vue'
  import FilteredPublisherListServerSide from '~components/publisherRelated/FilteredPublisherListServerSide.vue'
  import AutoCompleteBookInput from '~components/bookRelated/AutoCompleteBookInput.vue'

  import { getBookByFieldsId, baseHost } from '~/api/index.js'

  export default {
    layout: 'default',
    components: {
      FilteredAuthorListServerSide,
      FilteredPublisherListServerSide,
      AutoCompleteBookInput
    },
    data () {
      return {
        modelList: {
          author: '',
          publisher: ''
        },
        book: {
          query: '',
          items: [],
          highlighted: 'name'
        },
        bookList: []
      }
    },
    methods: {
      selectPublisher (item) {
        console.log(item, 'spub')
        this.modelList.publisher = item
        this.getBookList()
      },
      selectAuthor (item) {
        console.log(item, 'saut')
        this.modelList.author = item
        this.getBookList()
      },
      getBookList () {
        let data = {
          author_id: this.modelList.author.id,
          publisher_id: this.modelList.publisher.id
        }
        var promise = getBookByFieldsId(data)
        promise.then((response) => {
          this.bookList = []
          for (var item in response.data) {
            response.data[item].image = baseHost + response.data[item].image
            response.data[item].author = response.data[item].author.name
            response.data[item].publisher = response.data[item].publisher.name
            this.bookList.push(response.data[item])
          }
          this.filterBookList()
        })
      },
      bookSelected (item) {
        console.log(item, 'item')
        this.$router.push(this.$route.path + '/' + item.id)
      },
      filterBookList (input) {
        let list = []
        let pattern = new RegExp(input)
        this.bookList.forEach((item) => {
          if (pattern.test(item.name) | !input) {
            list.push(item)
          }
        })
        this.book.items = list
      },
      addBook () {
        this.$router.push(this.$route.path + '/add')
      }
    }
  }
</script>

<style>

</style>
