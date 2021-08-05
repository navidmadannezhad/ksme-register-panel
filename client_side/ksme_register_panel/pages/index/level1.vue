<template>
    <div class="level1">
        <div class="form">
            <div class="name">
                <input type="text" v-model="first_name" placeholder="نام">
            </div>
            <div class="fathers_name">
                <input type="text" v-model="last_name" placeholder="نام خانوادگی">
            </div>
            <div class="birthday">
                <p class="intro">تاریخ تولد</p>
                <date-picker id="date-picker" v-model="birthday"></date-picker>
            </div>
            <div class="national_number">
                <input type="text" placeholder="کد ملی/ شماره شناسنامه" v-model="national_number">
            </div>
            <div class="phone_number">
                <input type="text" placeholder="شماره تلفن همراه" v-model="phone_number">
            </div>
            <div class="email">
                <input type="text" placeholder="ایمیل" v-model="email">
            </div>

            <div class="next_level">
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
            birthday: '',
            national_number: '',
            phone_number: '',
            email: ''
        }
    },

    methods:{
        validateLevel1(){
            let data = {
                first_name: this.first_name,
                last_name: this.last_name,
                birthday: this.birthday,
                national_number: this.national_number,
                phone_number: this.phone_number,
                email: this.email

            }

            let args = {
                level: 1,
                data: data
            }

            this.$store.dispatch('validateLevel', args)
            .then(response => {
                console.log(response.data);
                //this.$store.commit('openLockOfLevel', 2);
            })
            .catch(err => {
                console.log(err.response.data);
            });
        }
    },

    mounted(){
   
    }

}
</script>