<template>
  <div>
    <form ref="myform" @submit.prevent="addBook" method="POST" action="http://127.0.0.1:8000/api/book/add" id="mainForm" enctype="multipart/form-data">
      <p><input type="text" placeholder="Enter book title..." name="book" ref="book" v-model="bookFormData.book"></p>
      <p><input type="text" placeholder="Enter author name..." name="author" ref="author" v-model="bookFormData.author"></p>
      <p><input type="text" placeholder="Enter publisher..." name="publisher" ref="publisher" v-model="bookFormData.publisher"></p>
      <p><input type="file" placeholder="load book image" name="image" accept="image/*" ref="image" v-on:change="fileChanged"></p>
      <input type="submit" name="btnSubmit" >
    </form>
  </div>
</template>

<script>
  import { addBookFromForm } from '../api/index.js'
  export default{
    data () {
      return {
        bookFormData: {
          book: '',
          author: '',
          publisher: '',
          image: ''
        }
      }
    },
    methods: {
      addBook () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.bookFormData) {
            data.append(key, this.bookFormData[key])
          }
          var promise = addBookFromForm(data)
          promise.then((response) => {
            console.log(response.data)
          }).catch(
            console.log('shit happens')
          )
          this.clearForm()
        }
      },
      clearForm () {
        for (var key in this.bookFormData) {
          this.bookFormData[key] = ''
        }
      },
      fileChanged (e) {
        this.bookFormData.image = e.target.files[0]
      },
      validateForm () {
        return this.validateBook() & this.validateAuthor() & this.validatePublisher()
      },
      validateBook () {
        if (this.bookFormData.book) {
          return true
        }
        return false
      },
      validateAuthor () {
        if (this.bookFormData.author) {
          return true
        }
        return false
      },
      validatePublisher () {
        if (this.bookFormData.publisher) {
          return true
        }
        return false
      }
    }
  }
</script>

<style>

</style>
