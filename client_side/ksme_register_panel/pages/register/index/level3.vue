<template>
    <div class="level3">
        <div class="form">

            <div class="corp_field">
                <p class="intro">تمایل به همکاری در حوزه:</p>
                <div class="options">
                    <div class="option">
                        <input type="checkbox" id="content" name="content" value="content" v-model="tolidMohtava">
                        <label for="content">تولید محتوا</label>
                    </div>
                    <div class="option">
                        <input type="checkbox" id="journal" name="journal" value="journal" v-model="journal">
                        <label for="journal">مقاله نویسی</label>
                    </div>
                </div>
            </div>

            <div class="experience">
                <textarea type="text" placeholder="سخن دیگه ای؟ :)" v-model="extra_words"></textarea>
            </div>

            <div class="next_level">
                <button class="next_level" @click="validateLevel3" ref="btn">تکمیل فرآیند ثبت نام</button>
                <!-- <NuxtLink class="next_level" tag="button" to='/level4'>تکمیل فرآیند ثبت نام</NuxtLink> -->
            </div>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return{
            tolidMohtava: false,
            journal: false,
            extra_words: ''
        }
    },
    methods:{
        validateLevel3(){
            this.changeLoadingState();
            this.disableBtn();

            localStorage.setItem('corporate_field', this.corporate_field);
            localStorage.setItem('extra_words', this.extra_words);

            this.$store.dispatch('validateLevel3')
            .then(response => {
                this.changeLoadingState();
                this.$store.commit('openLockOfLevel', { num: 4 });
                this.$router.push({'path': 'level4'});

                // for security reasons --
                this.$store.dispatch('deleteLocalStorageItems');
            })
            .catch(err => {
                let error;
                if(!err.response){
                    error = {0: ['مشکل در اتصال به اینترنت']}
                }else{
                    error = err.response.data;
                    console.log(err.response);
                }
                this.changeLoadingState();
                this.updateErrorsInParent(error);
                this.enableBtn();
            });
        },

        changeLoadingState(){
            this.$store.commit('changeLoadingState');
        },

        updateErrorsInParent(data){
            this.$nuxt.$emit('update-errors', data);
        },

        disableBtn(){
            this.$refs.btn.disabled = true;
            this.$refs.btn.classList.add('btn-disabled');
        },

        enableBtn(){
            this.$refs.btn.disabled = false;
            this.$refs.btn.classList.remove('btn-disabled');
        }
    },

    computed:{
        corporate_field(){
            return `${this.tolidMohtava ? 'تولید محتوا': ''}, ${this.journal ? 'مقاله نویسی': ''} `;
        },
        stored_extra_words(){
            return localStorage.getItem('extra_words') ? localStorage.getItem('extra_words') : '';
        },
    },

    mounted(){
        this.extra_words = this.stored_extra_words;
    }
}
</script>

<style scoped>
.btn-disabled{
    background-color: #ccc64a !important;
}
</style>