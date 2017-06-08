<template>
  <div>
    <h1>Author</h1>
    <form ref="myform" @submit.prevent="addAuthor" method="POST" id="mainForm" enctype="multipart/form-data">
      <p><input type="text" placeholder="Enter author name..." v-model="formData.name"></p>
      <input type="submit" name="btnSubmit" >
    </form>
  </div>
</template>

<script>
  import { postAuthor } from '../api/index.js'
  export default{
    data () {
      return {
        formData: {
          name: ''
        }
      }
    },
    methods: {
      addAuthor () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formData) {
            data.append(key, this.formData[key])
          }
          var promise = postAuthor(data)
          promise.then((response) => {
            this.clearForm()
          })
        }
      },
      clearForm () {
        for (var key in this.formData) {
          this.formData[key] = ''
        }
      },
      validateForm () {
        return this.validateAuthor()
      },
      validateAuthor () {
        if (this.formData.name) {
          return true
        }
        return false
      }
    }
  }
</script>

<style>

</style>
