<template>
  <div class="autocomplete-input">
    <h1>Author</h1>
    <input class="input is-large" placeholder="Search..." :value="value.query" @input="updateData()" ref="aComplete">
    <ul class="options-list">
      <li is="author-option" :input="value.query" v-for="item in value.items" @click.native="optionClicked(item)" :author="item"></li>
    </ul>
  </div>
</template>

<script>
  import AuthorOption from '~components/authorRelated/AuthorOption.vue'
  export default {
    props: ['value', 'callback'],
    components: {
      AuthorOption
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
    width: 100%;
  }

  .autocomplete-input {
    position: relative;
    height: 20px;
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
