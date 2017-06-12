<template>
  <div class="authorView">
    <div class="authorData">
      <p v-for="item in authorBold" v-html="item"></p>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['author', 'input'],
    computed: {
      authorBold () {
        var authorBold = {}
        Object.keys(this.author).forEach((key) => {
          if (!(key === 'id')) {
            authorBold[key] = '<p>' + key + ': ' + this.author[key].replace(this.input, '<b>' + this.input + '</b>') + '</p>'
          }
        })
        return authorBold
      }
    }
  }
</script>

<style>

  .authorData {
    width: 80%;
  }

  .authorView {
    width: 100%;
    flex-wrap: wrap;
    background: white;
    margin: 0;
    border-bottom: 1px solid #eee;
    color: #363636;
    padding: 7px;
    cursor: pointer;
  }

  .authorView:hover {
    background: #f8f8f8
  }
</style>
