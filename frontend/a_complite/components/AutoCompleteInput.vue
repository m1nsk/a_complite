<template>
  <div class="autocomplete-input">
    <h1>{{title}}</h1>
    <input class="input is-large" placeholder="Search..." @input="updateData()" ref="aComplete">
    <ul class="options-list">
      <li is="book-view" v-for="item in value.items" @click="optionClicked(item)" :book="item"></li>
    </ul>
  </div>
</template>

<script>
  import BookView from '~components/BookView.vue'
  export default {
    props: ['value', 'callback', 'title'],
    methods: {
      updateData () {
        this.callback(this.$refs.aComplete.value)
        this.$emit('input', {
          query: this.$refs.aComplete.value,
          items: this.value.items
        })
      },
      optionClicked (item) {
        this.$emit('option', item)
      }
    },
    computed: {
      options () {
        var options = []
        for (var index in this.value.items) {
          options.push(this.value.items[index].name.replace(this.$refs.aComplete.value, '<b>' + this.$refs.aComplete.value + '</b>'))
        }
        return options
      }
    },
    components: {
      BookView
    }
  }
</script>

<style>
  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  input {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
  }

  .autocomplete-input {
    position: relative;
    height: 300px;
    width: 300px;
    display: inline-block;
  }

  ul.options-list {
    display: flex;
    flex-direction: column;
    border: 1px solid #dbdbdb;
    border-radius: 0 0 3px 3px;
    position: absolute;
    width: 100%;
    overflow: hidden;
  }

  ul.options-list li {
    width: 100%;
    flex-wrap: wrap;
    background: white;
    margin: 0;
    border-bottom: 1px solid #eee;
    color: #363636;
    padding: 7px;
    cursor: pointer;
  }

  ul.options-list li:hover {
    background: #f8f8f8
  }
</style>
