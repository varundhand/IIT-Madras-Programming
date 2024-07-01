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
      brand: 'VROON',
      description: 'A pair of warm, fuzzy socks',
      // image: 'assets/images/socks_green.jpg',
      // inStock: false,
      selectedVariant: 0,
      onSale: true,
      alternative: 'A pair of socks',
      url: 'https://www.google.com/',
      inventory: 10,
      details: ['50% cotton', '30% wool', '20% polyester'],
      variants: [
        { id: 2234, color: 'green', image: 'assets/images/socks_green.jpg', quantity: 50 },
        { id: 2235, color: 'blue', image: 'assets/images/socks_blue.jpg', quantity: 0}
      ]
    }
  },
  methods: {
    addToCart(){
      this.cart += 1
    },
    // updateImage(variantImage){
    //   this.image = variantImage
    // },
    updateVariant(index){
      this.selectedVariant = index
    }
    },
    // computed properties are cached based on their dependencies
    computed: {
      title(){{
        return this.brand + ' ' + this.product
      }},
      image(){
        return this.variants[this.selectedVariant].image
      },
      inStock(){
        return this.variants[this.selectedVariant].quantity
      },
      onSaleComputed(){
        if (this.onSale){
          return this.brand + ' ' + this.product + ' is on sale!'
        }
      },
    },
}).mount('#app');
