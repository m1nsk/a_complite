<template>
  <div>
    <h1>Publisher</h1>
    <form ref="myform" @submit.prevent="addPublisher" id="mainForm" class="postForm">
      <p><input type="text" placeholder="Enter publisher name..." v-model="formData.name"></p>
      <input type="submit" name="btnSubmit" >
    </form>
  </div>
</template>

<script>
  import { postPublisher } from '../../api/index.js'
  export default{
    data () {
      return {
        formData: {
          name: ''
        }
      }
    },
    methods: {
      addPublisher () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formData) {
            data.append(key, this.formData[key])
          }
          var promise = postPublisher(this.formData.id, data)
          promise.then((response) => {
            console.log(response.data)
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
        return this.validatePublisher()
      },
      validatePublisher () {
        if (this.formData.name) {
          return true
        }
        return false
      }
    }
  }
</script>

<style>
  input {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    width: 100%;
  }

  .postForm {
    width: 300px;
    display: block;
  }
</style>
