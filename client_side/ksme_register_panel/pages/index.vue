<template>
    <div class="panel">

            <div class="form-section">
                <Nuxt></Nuxt>
            </div>


        <div class="loader-section">
                <div class="loader">

                  <svg viewBox="0 0 100 100" ref="svg">
                    <path ref="loaderPath" id="loader-itself" class="loader-level2" d="
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
                 
                      <div class="level-message" ref="levelMessage">اطلاعات اولیه</div>
               
                  </div>

            </div>
        </div>

    </div>
</template>

<script>
export default{
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
        } 
      }
    },

    methods:{
      addLoader(){
        this.$refs.loaderPath.classList.add('loader-stroke-rotate');
        this.$refs.svg.classList.add('svg-rotate');
      },
      
      removeLoader(){
        this.$refs.loaderPath.classList.remove('loader-stroke-rotate');
        this.$refs.svg.classList.remove('svg-rotate');
      },

      removeLoaderClasses(){
        console.log('removed');
        let loaderPathClasses = this.$refs.loaderPath.classList;
        loaderPathClasses.forEach(className => {
          loaderPathClasses.remove(className);
        })
      },

      goToLevel(num){
        this.$refs.levelMessage.innerHTML = eval(`this.level${num}`).message;
        this.removeLoaderClasses();
        this.$refs.loaderPath.classList.add(eval(`this.level${num}`).class);
      },


    },

    mounted(){
        this.$router.push({path: 'level1'});
        this.goToLevel(1);

        this.$router.beforeEach((from, to, next) => {
          switch(from.path){

            case '/level1':
              console.log('1');
              this.goToLevel(1);
              break;

            case '/level2':
              console.log('2');
              this.goToLevel(2);
              break;

            case '/level3':
              console.log('3');
              this.goToLevel(3);
              break;

            case '/level4':
              console.log('4');
              this.goToLevel(4);
              break;
          }
          next();
        })

    }
}
</script>

<style lang="scss" scoped>

</style>