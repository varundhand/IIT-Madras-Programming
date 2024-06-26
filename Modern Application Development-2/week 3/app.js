import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

createApp({
  setup() {
    const message = ref('Hello Vue!')
    return {
      message
    }
  },
  data() {
    return {
      cart: 0,
      product: 'Socks',
      description: 'A pair of warm, fuzzy socks',
      image: 'assets/images/socks_green.jpg',
      alternative: 'A pair of socks',
      url: 'https://www.google.com/',
      inStock: false,
      inventory: 10,
      details: ['50% cotton', '30% wool', '20% polyester'],
      variants: [
        { id: 2234, color: 'green' },
        { id: 2235, color: 'blue' }
      ]
    }
  }
}).mount('#app')
