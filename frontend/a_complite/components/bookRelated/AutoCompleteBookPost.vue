<template>
  <div>
    <filter-book-list @filterBook="filterChanged" class="filterBookList"></filter-book-list>
    <div class="submitBookForm">
      <h1>Author</h1>
      <form ref="myform" @submit.prevent="submitBook" id="mainForm" >
        <p><input type="text" placeholder="Enter book title..." name="book" ref="book" v-model="formModel.name"></p>
        <p><input type="file" placeholder="load book image" name="image" accept="image/*" ref="image" v-on:change="fileChanged"></p>
        <input type="submit" name="btnSubmit" >
      </form>
    </div>

  </div>
</template>

<script>
  import { postBook } from '../../api/index.js'
  import FilterBookList from '~components/bookRelated/FilterBookList.vue'
  export default {
    data () {
      return {
        formModel: {
          author: '',
          publisher: '',
          name: '',
          image: ''
        }
      }
    },
    components: {
      FilterBookList
    },
    methods: {
      submitBook () {
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formModel) {
            data.append(key, this.formModel[key])
          }
          var promise = postBook(data)
          promise.then((response) => {
            this.clearForm()
          })
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
      }
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
