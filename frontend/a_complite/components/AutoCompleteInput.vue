<template>
  <div class="autocomplete-input">
    <h1>{{title}}</h1>
    <input class="input is-large" placeholder="Search..." :value="value.query" @input="updateData()" ref="aComplete">
    <ul class="options-list">
      <li :highlighted="value.highlighted" :input="value.query" is="book-view" v-for="item in value.items" @click.native="optionClicked(item)" :book="item"></li>
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
          items: this.value.items,
          highlighted: this.value.highlighted
        })
      },
      optionClicked (item) {
        this.$emit('option', item)
        this.value.query = item[this.value.highlighted]
        this.value.items = [item]
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
</style>
