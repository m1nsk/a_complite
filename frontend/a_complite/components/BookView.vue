<template>
  <div class="bookView">
    <div class="bookImage">
      <img :src="book['image']" style="width:60px;height:60px;">
    </div>
    <div class="bookData">
      <p v-for="item in bookBold" v-html="item"></p>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['book', 'highlighted', 'input'],
    data () {
      return {}
    },
    computed: {
      bookBold () {
        var bookBold = {}
        Object.keys(this.book).forEach((key) => {
          if (key === this.highlighted) {
            bookBold[key] = '<p>' + key + ': ' + this.book[key].replace(this.input, '<b>' + this.input + '</b>') + '</p>'
          } else if (key !== 'image') {
            bookBold[key] = '<p>' + key + ': ' + this.book[key] + '</p>'
          }
        })
        return bookBold
      }
    }
  }
</script>

<style>
  .bookImage {
    width: 20%;
  }

  .bookData {
    width: 80%;
  }

  .bookImage.img{
    width: 100%;
  }

  .bookView {
    width: 100%;
    flex-wrap: wrap;
    background: white;
    margin: 0;
    border-bottom: 1px solid #eee;
    color: #363636;
    padding: 7px;
    cursor: pointer;
  }

  .bookView:hover {
    background: #f8f8f8
  }
</style>
