import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import ProductDisplay from './components/ProductDisplay.js'

const app = createApp({
  // setup() {
  //   const message = ref('Hello Vue!')
  //   return {
  //     message
  //   }
  // },
  data() {
    return {
      cart: 0,
      premium: true,
    }
  },
  methods: {
  },
})

app.component('product-display', ProductDisplay)
app.mount('#app')
