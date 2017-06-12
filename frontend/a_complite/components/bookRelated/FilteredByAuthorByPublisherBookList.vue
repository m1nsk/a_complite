<template>
  <div>
    <auto-complete-publisher-input v-model="publisherList" :callback="filterPublisherList" @option="onPublisherClicked" ></auto-complete-publisher-input>
    <auto-complete-author-input v-model="authorList" :callback="filterAuthorList" @option="onAuthorClicked" ></auto-complete-author-input>
    <div class="bookList">
      <ul class="options-list">
        <li is="book-option" v-for="item in bookList" @click.native="onBookClicked" :book="item"></li>
      </ul>
    </div>
  </div>
</template>

<script>
  import { getPublisherList, getAuthorList } from '../../api/index.js'
  import AutoCompletePublisherInput from '~components/publisherRelated/AutoCompletePublisherInput.vue'
  import AutoCompleteAuthorInput from '~components/authorRelated/AutoCompleteAuthorInput.vue'
  import BookOption from '~components/bookRelated/BookOption.vue'
  export default {
    components: {
      AutoCompletePublisherInput,
      AutoCompleteAuthorInput,
      BookOption
    },
    data () {
      return {
        publisherList: {
          query: '',
          items: [],
          highlighted: 'name'
        },
        bookPublisherData: [],
        authorList: {
          query: '',
          items: [],
          highlighted: 'name'
        },
        bookAuthorData: [],
        bookData: []
      }
    },

    created: function () {
      var promisePublisher = getPublisherList()
      var promiseAuthor = getAuthorList()
      promisePublisher.then((response) => {
        for (var item in response.data) {
          this.bookPublisherData.push(response.data[item])
        }
        this.filterPublisherList()
      })
      promiseAuthor.then((response) => {
        for (var item in response.data) {
          this.bookAuthorData.push(response.data[item])
        }
        this.filterAuthorList()
      }),
    },
    methods: {
      filterPublisherList (input) {
        let list = []
        let pattern = new RegExp(input)
        this.bookPublisherData.forEach((item) => {
          if (pattern.test(item.name) | !input) {
            list.push(item)
          }
        })
        this.publisherList.items = list
      },
      filterAuthorList (input) {
        let list = []
        let pattern = new RegExp(input)
        this.bookAuthorData.forEach((item) => {
          if (pattern.test(item.name) | !input) {
            list.push(item)
          }
        })
        this.authorList.items = list
      },
      filterBookList (input) {
      },
      onAuthorClicked (item) {
        this.authorList.query = item.name
      },
      onPublisherClicked (item) {
        this.publisherList.query = item.name
      },
      onBookClicked (item) {
        console.log('bookClicked')
      }
    },
    computed: {
      bookList () {
        var result = unique(this.publisherList.items.concat(this.authorList.items))
        return result
        function unique (arr) {
          console.log(arr, 'arr')
          var arrDict = {}
          var result = []
          arr.forEach((item) => {
            if (!(item.id in arrDict)) {
              arrDict[item.id] = true
              result.push(item)
            }
          })
          return result
        }
      }
    }
  }
</script>

<style>
  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  input {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 100%;
  }

  .bookList {
    position: relative;
    height: 20px;
    width: 300px;
    display: inline-block;
  }

  ul.options-list {
    display: flex;
    flex-direction: column;
    border: 1px solid #dbdbdb;
    border-radius: 0 0 3px 3px;
    position: absolute;
    width: 100%;
    overflow: hidden;
  }
</style>
