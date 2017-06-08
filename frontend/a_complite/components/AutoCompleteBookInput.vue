<template>
  <div class="autocomplete-input">
    <h1>{{title}}</h1>
    <input class="input is-large" placeholder="Search..." :value="value.query" @input="updateData()" ref="aComplete">
    <ul class="options-list">
      <li is="book-option" :highlighted="value.highlighted" :input="value.query" v-for="item in value.items" @click.native="optionClicked(item)" :book="item"></li>
    </ul>
  </div>
</template>

<script>
  import BookOption from '~components/BookOption.vue'
  export default {
    props: ['value', 'callback', 'title'],
    components: {
      BookOption
    },
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
