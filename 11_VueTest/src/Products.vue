<template>
     <div>
        <h1>Products</h1>
        <h2>{{ id }}</h2>
        <h2>{{ queryStr }}</h2>
    </div>
</template>

<script>
    const products = {
        18: 'Shoes',
        26: 'T-shit',
        37: 'Pants',
    };

    export default {
        computed: {
            id() {
                return products[this.$route.params.sn];
            },
            queryStr() {
                return products[this.$route.query.id];
            }
        }
    }
</script>