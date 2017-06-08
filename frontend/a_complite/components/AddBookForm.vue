<template>
  <div>
    <h1>Book</h1>
    <form ref="myform" @submit.prevent="addBook" method="POST" id="mainForm" enctype="multipart/form-data">
      <p><input type="text" placeholder="Enter book title..." name="book" ref="book" v-model="bookFormData.name"></p>
      <p><input type="text" placeholder="Enter author name..." name="author" ref="author" v-model="bookFormData.author"></p>
      <p><input type="text" placeholder="Enter publisher..." name="publisher" ref="publisher" v-model="bookFormData.publisher"></p>
      <p><input type="file" placeholder="load book image" name="image" accept="image/*" ref="image" v-on:change="fileChanged"></p>
      <input type="submit" name="btnSubmit" >
    </form>
  </div>
</template>

<script>
  import { addBookFrom } from '../api/index.js'
  export default{
    data () {
      return {
        bookFormData: {
          name: '',
          author: '',
          publisher: '',
          image: ''
        }
      }
    },
    methods: {
      submitBook () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.bookFormData) {
            if (key === 'image' & !this.bookFormData[key]) {
              continue
            }
            console.log(key, this.bookFormData[key])
            data.append(key, this.bookFormData[key])
          }
          var promise = addBookFrom(data)
          promise.then((response) => {
            this.clearForm()
          })
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
        if (this.bookFormData.name) {
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
