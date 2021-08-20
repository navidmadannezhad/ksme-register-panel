<template>
    <div class="error-comp" ref="errorComp">

        <div class="errors">

            <div class="error" v-for="error in organizedErrorArray" v-bind:key="error">
                {{ error }}
            </div>  

        </div>

    </div>
</template>

<script>
export default {
    props: [
        'errors'
    ],


    methods:{
        displayErrors(){
            this.$refs.errorComp.style.transform = 'translateX(0vw)';
            setTimeout(() => {
                this.$refs.errorComp.style.transform = 'translateX(120vw)';
            }, 5000);
        }
    },

    computed:{
        // Turns django styled error array into a ordinary array
        organizedErrorArray(){
            let organizedErrorArray = [];
            Object.keys(this.errors).forEach(error => {
                organizedErrorArray.push(this.errors[error][0]);
            })

            return organizedErrorArray;
        }
    },


    watch:{
        errors(oldVal, newVal){
            this.displayErrors();
        }
    }
}
</script>

<style lang="scss" scoped>
div.error-comp{
    width: 50%;
    position: absolute;
    top: 0px;
    transform: translateX(120vw);
    transition: all 0.5s;
    div.errors{
        width: 100%;
        div.error{
            background-color: rgba(255, 79, 79, 0.5);
            color: white;
            font-size: $font2;
            padding: 5px;
            text-align: center;
            border-radius: 5px;
            margin-top: 10px;
        }
    }
}
</style>