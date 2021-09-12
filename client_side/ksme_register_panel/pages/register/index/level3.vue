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
                <button class="next_level" @click="validateLevel3">تکمیل فرآیند ثبت نام</button>
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

            this.pushToVuexState('extra_words', this.extra_words);
            this.pushToVuexState('corporate_field', this.corporate_field);

            this.$store.dispatch('validateLevel3')
            .then(response => {
                this.$store.commit('openLockOfLevel', { num: 4 });
                this.$router.push({'path': 'level4'});
            })
            .catch(err => {
                this.updateErrorsInParent(err.response.data)
            }).finally(() => {
                this.changeLoadingState();
            })
        },

        changeLoadingState(){
            this.$store.commit('changeLoadingState');
        },

        pushToVuexState(paramName, newValue){
            this.$store.commit('renewParameter', { paramName, newValue });
        },

        updateErrorsInParent(data){
            this.$nuxt.$emit('update-errors', data);
        }
    },

    computed:{
        corporate_field(){
            return `${this.tolidMohtava ? 'تولید محتوا': ''}, ${this.journal ? 'مقاله نویسی': ''} `;
        }
    }
}
</script>