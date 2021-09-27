<template>
    <div class="level1">
        <div class="form">
            <div class="name input">
                <input type="text" v-model="first_name" placeholder="نام">
            </div>
            <div class="fathers_name input">
                <input type="text" v-model="last_name" placeholder="نام خانوادگی">
            </div>
            <div class="birthday input">
                <p class="intro">تاریخ تولد</p>
                <date-picker id="date-picker" v-model="birthday" />
            </div>
            <div class="national_number input">
                <input type="text" placeholder="کد ملی/ شماره شناسنامه" v-model="national_number">
            </div>
            <div class="phone_number input">
                <input type="text" placeholder="شماره تلفن همراه" v-model="phone_number">
            </div>
            <div class="email input">
                <input type="text" placeholder="ایمیل" v-model="email">
            </div>

            <div class="next_level input">
                <button class="next_level" @click="validateLevel1">مرحله بعد</button>
                <!-- <NuxtLink class="next_level" tag="button" to='/level2'>مرحله بعد</NuxtLink> -->
            </div>
        </div>
    </div>
</template>


<script>
import VuePersianDatetimePicker from 'vue-persian-datetime-picker'
export default {
    components: {
        datePicker: VuePersianDatetimePicker
    },

    data(){
        return{
            birthday: '',
            first_name:'',
            last_name:'',
            national_number: '',
            phone_number: '',
            email: '',
        }
    },

    methods:{
        validateLevel1(){
            this.changeLoadingState();

            localStorage.setItem('birthday', this.birthday);
            localStorage.setItem('first_name', this.first_name);
            localStorage.setItem('last_name', this.last_name);
            localStorage.setItem('national_number', this.national_number);
            localStorage.setItem('phone_number', this.phone_number);
            localStorage.setItem('email', this.email);

            this.$store.dispatch('validateLevel1')
            .then(response => {
                this.changeLoadingState();
                this.$store.commit('openLockOfLevel', { num: 2 });
                this.$router.push({'path': '/register/level2'});
            })
            .catch(err => {
                let error;
                if(!err.response){
                    error = {0: ['مشکل در اتصال به اینترنت']}
                }else{
                    error = err.response.data;
                }
                this.changeLoadingState();
                this.updateErrorsInParent(error);
            });
        },

        changeLoadingState(){
            this.$store.commit('changeLoadingState');
        },

        updateErrorsInParent(data){
            this.$nuxt.$emit('update-errors', data);
        }
    },

    computed:{
        stored_birthday(){
            return localStorage.getItem('birthday') ? localStorage.getItem('birthday') : '';
        },
        stored_first_name(){
            return localStorage.getItem('first_name') ? localStorage.getItem('first_name') : '';
        },
        stored_last_name(){
            return localStorage.getItem('last_name') ? localStorage.getItem('last_name') : '';
        },
        stored_national_number(){
            return localStorage.getItem('national_number') ? localStorage.getItem('national_number') : '';
        },
        stored_phone_number(){
            return localStorage.getItem('phone_number') ? localStorage.getItem('phone_number') : '';
        },
        stored_email(){
            return localStorage.getItem('email') ? localStorage.getItem('email') : '';
        }
    },

    mounted(){
        this.birthday = this.stored_birthday;
        this.first_name = this.stored_first_name;
        this.last_name = this.stored_last_name;
        this.national_number = this.stored_national_number;
        this.phone_number = this.stored_phone_number;
        this.email = this.stored_email;
    }

}
</script>