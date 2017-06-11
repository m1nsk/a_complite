<template>
    <div>
        <h1>Edit Publisher</h1>
        <form ref="myform" @submit.prevent="putPublisher" id="mainForm" class="putDeleteForm">
            <p><input type="text" placeholder="Enter publisher name..." v-model="formData.name"></p>
            <input type="submit" name="btnSubmit" >
        </form>
        <button @click="deletePublisher">Delete</button>
    </div>
</template>

<script>
  import { putPublisher, getPublisherById, deletePublisherById } from '../../api/index.js'
  export default{
    data () {
      return {
        formData: {
          name: '',
          id: this.$route.params
        }
      }
    },
    methods: {
      putPublisher () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formData) {
            console.log(key)
            data.append(key, this.formData[key])
          }
          var promise = putPublisher(this.formData.id, data)
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
        return this.validatePublisher()
      },
      validatePublisher () {
        if (this.formData.name) {
          return true
        }
        return false
      },
      deletePublisher () {
        var promise = deletePublisherById(this.formData.id)
        promise.then((response) => {
          this.$router.go(-1)
        })
      }
    },
    created: function () {
      console.log(this.$route.params['id'])
      var promise = getPublisherById(this.$route.params['id'])
      promise.then((response) => {
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
