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
                <input type="text" id="datepicker" v-model="birthday">
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
                <NuxtLink class="next_level" tag="button" to='/level2'>مرحله بعد</NuxtLink>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    
    data(){
        return{
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

            this.$store.dispatch.validateLevel(1, data)
            .then(response => {
                this.$store.commit('openLockOfLevel', 2);
            })
            .catch(err => {
                console.log(err.response.response);
            });
        }
    },

    mounted(){
        $(function() {
            $("#datepicker").persianDatepicker();       
        })
    }

}
</script>