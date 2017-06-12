<template>
    <div>
        <filtered-publisher-list-server-side :init="initialPublisher" @publisher="setPublisher" ref="first"></filtered-publisher-list-server-side>
        <filtered-author-list-server-side :init="initialAuthor" @author="setAuthor"></filtered-author-list-server-side>
        <div class="submitBookForm">
            <h1>Book</h1>
            <form ref="myform" @submit.prevent="submitBook" id="mainForm" >
                <p><input type="text" placeholder="Enter book title..." name="book" ref="book" v-model="formModel.name"></p>
                <p><input type="file" placeholder="load book image" name="image" accept="image/*" ref="img" v-on:change="fileChanged"></p>
                <input type="submit" name="btnSubmit" >
            </form>
            <button @click="deleteBook">Delete</button>
        </div>
    </div>
</template>

<script>
  import { deleteBookById, putBook, getBookById, getAuthorById, getPublisherById, baseURL } from '../../api/index.js'
  import FilterBookList from '~components/bookRelated/FilterBookList.vue'
  import FilteredAuthorListServerSide from '~components/authorRelated/FilteredAuthorListServerSide.vue'
  import FilteredPublisherListServerSide from '~components/publisherRelated/FilteredPublisherListServerSide.vue'
  export default {
    components: {
      FilterBookList,
      FilteredAuthorListServerSide,
      FilteredPublisherListServerSide
    },
    data () {
      return {
        formModel: {
          author: '',
          publisher: '',
          name: '',
          image: ''
        },
        initialAuthor: {
          query: '',
          items: [],
          highlighted: 'name'
        },
        initialPublisher: {
          query: '',
          items: [],
          highlighted: 'name'
        }
      }
    },
    methods: {
      submitBook () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formModel) {
            data.append(key, this.formModel[key])
          }
          var promise = putBook(this.$route.params['id'], data)
          promise.then((response) => {
            this.$router.go(-1)
          })
        }
      },
      deleteBook () {
        var promise = deleteBookById(this.$route.params['id'])
        promise.then((response) => {
          this.$router.go(-1)
        })
      },
      clearForm () {
        for (var key in this.formModel) {
          this.formModel[key] = ''
        }
      },
      fileChanged (e) {
        this.formModel.image = e.target.files[0]
      },
      validateForm () {
        return this.validateBook() & this.validateAuthor() & this.validatePublisher()
      },
      validateBook () {
        if (this.formModel.name) {
          return true
        }
        return false
      },
      validateAuthor () {
        if (this.formModel.author) {
          return true
        }
        return false
      },
      validatePublisher () {
        if (this.formModel.publisher) {
          return true
        }
        return false
      },
      filterChanged (filter) {
        for (var key in filter) {
          this.formModel[key] = filter[key]
        }
      },
      setAuthor (item) {
        this.formModel.author = item.id
      },
      setPublisher (item) {
        this.formModel.publisher = item.id
      }
    },
    mounted: function () {
      var promise = getBookById(this.$route.params['id'])
      promise.then((response) => {
        response.data.image = baseURL + response.data.image
        console.log(this.$refs.img.files[0])
        this.formModel = response.data
        this.formModel.image = ''
        return getAuthorById(this.formModel.author)
      }).then((response) => {
        console.log(response.data)
        this.initialAuthor.items = [response.data]
        this.initialAuthor.query = response.data.name
        this.initialAuthor.highlighted = 'name'
        return getPublisherById(this.formModel.publisher)
      }).then((response) => {
        console.log(response.data)
        this.initialPublisher.items = [response.data]
        this.initialPublisher.query = response.data.name
        this.initialPublisher.highlighted = 'name'
      })
        .catch((error) => {
          if (error.response.status === 404) {
            this.$router.push('my-new-404-page')
          }
        })
    }
  }
</script>

<style>
    .filterBookList{
        display: inline-block;
        vertical-align: top;
    }
    .submitBookForm{
        display: inline-block;
        vertical-align: top;
    }
</style>
