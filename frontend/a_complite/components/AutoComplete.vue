<template>
  <div>
    <p><nuxt-link to="/addbookform">Add new book</nuxt-link></p>
    <auto-complete-input v-model="author" :callback="getByAuthor" @option="onAuthorClicked" title="Author"></auto-complete-input>
    <auto-complete-input v-model="publisher" :callback="getByPublisher" @option="onPublisherClicked" title="Publisher"></auto-complete-input>
    <form ref="myform" @submit.prevent="submitBook" method="POST" id="mainForm" enctype="multipart/form-data">
      <p><input type="text" placeholder="Enter book title..." name="book" ref="book" v-model="formModel.name"></p>
      <p><input type="file" placeholder="load book image" name="image" accept="image/*" ref="image" v-on:change="fileChanged"></p>
      <input type="submit" name="btnSubmit" >
    </form>
  </div>
</template>

<script>
  import { getBookByField, addBookFrom, baseHost } from '../api/index.js'
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
        },
        formModel: {
          author: '',
          publisher: '',
          name: '',
          image: ''
        }
      }
    },
    components: {
      AutoCompleteInput
    },
    methods: {
      getByAuthor (input) {
        this.getByField(input, 'author')
      },
      getByPublisher (input) {
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
        }).catch(
          this[field].items = []
        )
      },
      onClicked () {
        console.log('clicked')
      },
      onAuthorClicked (item) {
        this.formModel.author = item
      },
      onPublisherClicked (item) {
        this.formModel.publisher = item
      },
      submitBook () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formModel) {
            data.append(key, this.formModel[key])
          }
          var promise = addBookFrom(data)
          promise.then((response) => {
            console.log(response.data)
            this.clearForm()
          }).catch(
            console.log('shit happens')
          )
        }
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
        if (this.formModel.author.author) {
          return true
        }
        return false
      },
      validatePublisher () {
        if (this.formModel.publisher.publisher) {
          return true
        }
        return false
      }
    }
  }
</script>

<style>

</style>
