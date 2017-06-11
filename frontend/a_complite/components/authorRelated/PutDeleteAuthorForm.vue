<template>
    <div>
        <h1>Edit Author</h1>
        <form ref="myform" @submit.prevent="putAuthor" id="mainForm" class="putDeleteForm">
            <p><input type="text" placeholder="Enter author name..." v-model="formData.name"></p>
            <input type="submit" name="btnSubmit" >
        </form>
        <button @click="deleteAuthor">Delete</button>
    </div>
</template>

<script>
  import { putAuthor, getAuthorById, deleteAuthorById } from '../../api/index.js'
  export default{
    layout: 'default',
    data () {
      return {
        formData: {
          name: '',
          id: ''
        }
      }
    },
    methods: {
      putAuthor () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formData) {
            data.append(key, this.formData[key])
          }
          var promise = putAuthor(this.formData.id, data)
          promise.then((response) => {
            this.$router.go(-1)
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
      },
      deleteAuthor () {
        var promise = deleteAuthorById(this.formData.id)
        promise.then((response) => {
          this.$router.go(-1)
        })
      }
    },
    created: function () {
      var promise = getAuthorById(this.$route.params['id'])
      promise.then((response) => {
        console.log(response.data)
        this.formData = response.data
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
    input {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        width: 100%;
    }

    .putDeleteForm {
        width: 300px;
        display: block;
    }
</style>
