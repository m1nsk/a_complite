export const state = () => ({
  counter: 0,
  model: {
    query: 'sadasd',
    items: ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard']
  }
})

export const mutations = {
  increment (state) {
    state.counter++
  },
  setQuery (state, newQuery) {
    console.log(newQuery)
    state.model.items = newQuery
    console.log(state.model.items)
  }
}

export const actions = {
  setQuery (context, newQuery) {
    console.log('hello')
    context.commit('setQuery', newQuery)
  }
}
