<template>
    <div class="publisherList" >
        <auto-complete-publisher-input v-model="modelList" :callback="filterList" @option="onClicked" ></auto-complete-publisher-input>
    </div>
</template>

<script>
  import { getPublisherByName } from '../../api/index.js'
  import AutoCompletePublisherInput from '~components/publisherRelated/AutoCompletePublisherInput.vue'
  export default {
    props: ['init'],
    data () {
      return {
        defaultList: {
          query: '',
          items: [],
          highlighted: 'name'
        }
      }
    },
    components: {
      AutoCompletePublisherInput
    },
    methods: {
      filterList (input) {
        this.modelList.query = input
        this.$emit('publisher', '')
        let promise = getPublisherByName({'input': input})
        promise.then((response) => {
          this.modelList.items = response.data
        })
      },
      onClicked (item) {
        this.$emit('publisher', item)
      }
    },
    computed: {
      modelList () {
        if (this.init) {
          return this.init
        }
        return this.defaultList
      }
    }
  }
</script>

<style>
    .publisherList{
        display: inline-block;
    }
</style>
