<template>
    <div>
        <filtered-publisher-list-server-side @publisher="setPublisher" ref="first"></filtered-publisher-list-server-side>
        <filtered-author-list-server-side @author="setAuthor"></filtered-author-list-server-side>
        <div class="submitBookForm">
            <h1>Book</h1>
            <form ref="myform" @submit.prevent="submitBook" id="mainForm" >
                <p><input type="text" placeholder="Enter book title..." name="book" ref="book" v-model="formModel.name"></p>
                <p><input type="file" placeholder="load book image" name="image" accept="image/*" ref="img" v-on:change="fileChanged"></p>
                <input type="submit" name="btnSubmit" >
            </form>
        </div>
    </div>
</template>

<script>
  // import { putBook, getBookById, getAuthorById, getPublisherById, baseURL } from '../../api/index.js'
  import { postBook } from '../../api/index.js'
  import FilterBookList from '~components/bookRelated/FilterBookList.vue'
  import FilteredAuthorListServerSide from '~components/authorRelated/FilteredAuthorListServerSide.vue'
  import FilteredPublisherListServerSide from '~components/publisherRelated/FilteredPublisherListServerSide.vue'
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
      FilterBookList,
      FilteredAuthorListServerSide,
      FilteredPublisherListServerSide
    },
    methods: {
      submitBook () {
        console.log(this.formModel, 'fmodel')
        if (this.validateForm()) {
          let data = new FormData()
          for (var key in this.formModel) {
            data.append(key, this.formModel[key])
          }
          var promise = postBook(data)
          promise.then((response) => {
            this.$router.go(-1)
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
      },
      setAuthor (item) {
        this.formModel.author = item.id
      },
      setPublisher (item) {
        this.formModel.publisher = item.id
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
