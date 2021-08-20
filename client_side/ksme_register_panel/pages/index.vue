<template>
    <div class="panel">

        <div class="form-section">
            <Nuxt></Nuxt>
        </div>

        <div class="loader-section">
            <loader-component></loader-component>
        </div>

        <error-component :errors="errors"></error-component>

    </div>
</template>

<script>
import errorComponentVue from '../components/errorComponent.vue';
import loaderComponentVue from '../components/loaderComponent.vue';
export default{
    components:{
      'loader-component': loaderComponentVue,
      'error-component': errorComponentVue
    },

    data(){
      return{
        level1: {
          message: 'اطلاعات اولیه',
          class: 'loader-level1'
        },
        level2:{
          message: 'توانایی ها',
          class: 'loader-level2'
        },
        level3:{
          message: 'اطلاعات جانبی',
          class: 'loader-level3'
        } ,
        level4:{
          message: '<i class="fas fa-check"></i>',
          class: 'loader-level4'
        },

        errors: {}
      }
    },

    methods:{
      addLoader(){
        document.querySelector('#loader-itself').classList.add('loader-stroke-rotate');
        document.querySelector('.svg').classList.add('svg-rotate');
      },
      
      removeLoader(){
        document.querySelector('#loader-itself').classList.remove('loader-stroke-rotate');
        document.querySelector('.svg').classList.remove('svg-rotate');
      },

      removeLoaderClasses(){
        let loaderPathClasses = document.querySelector('#loader-itself').classList;
        loaderPathClasses.forEach(className => {
          loaderPathClasses.remove(className);
        })
      },

      goToLevel(num, nextRoute){
          document.querySelector('.level-message').innerHTML = eval(`this.level${num}`).message;
          this.removeLoaderClasses();
          document.querySelector('#loader-itself').classList.add(eval(`this.level${num}`).class);   
      },

      LevelIsLocked(num){
        //return eval(`this.$store.state.level${num}Lock`); 
        return eval(`this.$store.state.level${num}Lock`);
      },

      changeLoadingState(){
        this.$store.commit('changeLoadingState');
      },

    },

    computed:{
      isLoading(){
        return this.$store.state.isLoading;
      }
    },

    mounted(){
        this.$router.push({path: 'level1'});
        this.goToLevel(1); 

        this.$router.beforeEach((to, from, next) => {
      
          switch(to.path){

            case '/level1':
              this.LevelIsLocked(1) ? next(false) : next(this.goToLevel(1));
              break;

            case '/level2':
              this.LevelIsLocked(2) ? next(false) : next(this.goToLevel(2));
              break;

            case '/level3':
              this.LevelIsLocked(3) ? next(false) : next(this.goToLevel(3));
              break;

            case '/level4':
              this.LevelIsLocked(4) ? next(false) : next(this.goToLevel(4));
              break;
          }

        })

    },

    
    created () {
        this.$nuxt.$on('update-errors', (e) => {
            this.errors = e;
        })
    }
}
</script>

<style lang="scss" scoped>
</style>