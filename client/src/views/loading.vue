<template>
    <div>
        <h2>bars</h2>
    <vue-loading type="spin" color="#d9544e" :size="{ width: '50px', height: '50px' }">
    </vue-loading>
    </div>
</template>
<script>
    import { VueLoading } from 'vue-loading-template'
    export default {
    name: 'app',
    components: {
        VueLoading
    }
    }
</script>