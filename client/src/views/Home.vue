

<template>
  <div class="home">
    <section class="hero is-small is-dark mb-2">
        <div class="hero-body has-text-centered">
            <p class="title mb-2">
                Welcome to TMS
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Order</h2>
      </div>

      <div 
        class = 'column is-3'
        v-for="product in orderDetailSerializer"
        v-bind:key="product.name"
        v-bind:product="product" 
      >
        <div class = "box">  
          <h3 class="is-size-4">{{product.name}}</h3>
          <p class="is-size-6 has-text-gray">order_id: {{ product.order_id }}</p>
          <p class="is-size-6 has-text-gray">quantity: {{ product.quantity }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script> 
import axios from 'axios'
// import ProductBox from '@/components/ProductBox'
export default {
  name: 'Home',
  data() {
    return {
      orderDetailSerializer: []
    }
  },
  components: {
  },
  mounted() {
    this.getOrderDetailSerializer()
  },
  methods: {
    getOrderDetailSerializer() {
      axios
        .get('/api/v1/order/')
        .then(response => {
          this.orderDetailSerializer = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script> 