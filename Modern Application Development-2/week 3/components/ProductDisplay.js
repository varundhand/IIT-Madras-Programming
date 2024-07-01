export default {
    props: {
        premium: {
            type: Boolean,
            required: true
        }
    },
    template: 
    /*html*/
    `<div class="product-display">
          <div class="product-container">
            <div class="product-image">
              <!-- image goes here , using V BIND DIRECTIVE --> 
               <!-- V BIND is used to dynamically bind an attribute to an expression -->
                <a :href="url">
                    <img v-bind:src="image" :alt="alternative" :class="[!inStock ? 'out-of-stock-img' : '']">
                </a>
               <!-- shorthand of v-bind: is just ':' -->
                <!-- <img :src="image" alt=""> -->
            </div>
            <div class="product-info">
              <h1>{{ title }}</h1>
              <p>{{description}}</p>
              <!-- CONDITIONAL RENDERING using v-if= and v-else-->
               <p v-if="inStock">In Stock</p>
               <p v-else="inStock">Out of Stock</p>

               <p>Shipping: {{shipping}}</p>

                <div class="sale">{{onSaleComputed}}</div>

               <!-- chained conditional logic -->
                <p v-if="inventory > 10">A lot of pieces left</p>
                <p v-else-if="inventory <= 10 && inventory > 0" style="color: red;"> Only a few pieces left. Hurry now!</p>
                <p v-else>No pieces left :(</p>

                <!-- Rendering a list using v-for directive -->
                 <!-- for looping over details collection -->
                <ul>
                    <li v-for="detail in details"> -> {{detail}}</li>
                </ul>

                <!-- we need to give unique key while using v-for loop -->
                <!-- @mouseover="updateImage(variant.image)"  -->
                <div 
                  v-for="(variant,index) in variants" 
                  :key="variant.id" 
                  @mouseover="updateVariant(index)" 
                  class="color-circle"
                  :style="{backgroundColor: variant.color}" 
                >
                    {{}}
                </div>
                <!-- <button class="button" v-on:click="cart += 1">Add to Cart</button> -->
                <!-- using a method "addToCart"  -->
                <!-- using custom class , we can also using ternary syntax-->
                <!-- <button :disabled="!inStock" :class="{disabledButton: !inStock}" class="button" v-on:click="addToCart">Add to Cart</button> -->
                <button :disabled="!inStock" :class="[!inStock ? 'disabledButton' : '']" class="button" v-on:click="addToCart">Add to Cart</button>
                <!-- inStock is now a computed property instead of a data property -->
            </div>
          </div>
    </div>`,
    data() {
        return {
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
            ],
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
        shipping(){
            if (this.premium){
                return 'Free'
            }
            return '$2.99'
        }
        },
}