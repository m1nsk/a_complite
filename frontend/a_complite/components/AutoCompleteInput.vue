<template>
  <div class="autocomplete-input">
    <input class="input is-large" placeholder="Search..." list="itemList" @input="updateData()" ref="aComplete">
    <ul class="options-list">
      <li v-for="item in value.items" @click="optionClicked(item)">{{item.name}}</li>
    </ul>
  </div>
</template>

<script>
  export default {
    props: ['value', 'callback'],
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
