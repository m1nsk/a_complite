<template>
  <div class="publisherView">
    <div class="publisherData">
      <p v-for="item in publisherBold" v-html="item"></p>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['publisher', 'input'],
    computed: {
      publisherBold () {
        var publisherBold = {}
        Object.keys(this.publisher).forEach((key) => {
          if (!(key === 'id')) {
            publisherBold[key] = '<p>' + key + ': ' + this.publisher[key].replace(this.input, '<b>' + this.input + '</b>') + '</p>'
          }
        })
        return publisherBold
      }
    }
  }
</script>

<style>

  .publisherData {
    width: 80%;
  }

  .publisherView {
    width: 100%;
    flex-wrap: wrap;
    background: white;
    margin: 0;
    border-bottom: 1px solid #eee;
    color: #363636;
    padding: 7px;
    cursor: pointer;
  }

  .publisherView:hover {
    background: #f8f8f8
  }
</style>
