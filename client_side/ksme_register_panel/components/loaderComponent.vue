<template>
    <div class="loader">
        <svg viewBox="0 0 100 100" class="svg">
            <path id="loader-itself" class="loader-level2" d="
                M 37, 25
                m -25, 25
                a 32.5,32.5 0 1,0 75,0
                a 32.5,32.5 0 1,0 -75,0
            " fill="none" stroke-width="5" stroke="#FFF85C"/>
            <path id="loader-background" d="
                M 37, 25
                m -25, 25
                a 32.5,32.5 0 1,0 75,0
                a 32.5,32.5 0 1,0 -75,0
            " fill="none" stroke-width="5" stroke="rgba(0,0,0,0.3)"/>

        </svg>

        <div class="status">
        
            <div class="level-message">
                <p v-if="!isLoading">اطلاعات اولیه</p>
                <p v-else>منتظر بمانید</p>
            </div>
    
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'loaderState',
        'loaderMessage',
        'loaderBarAmount'
    ],

    computed:{
        isLoading(){
            return this.$store.state.isLoading;
        }
    }
}
</script>


<style lang="scss" scoped>

</style>
