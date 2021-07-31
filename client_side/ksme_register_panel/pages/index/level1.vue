<template>
    <div class="level1">
        <div class="form">
            <div class="name">
                <input type="text" v-model="name" placeholder="نام و نام خانوادگی">
            </div>
            <div class="fathers_name">
                <input type="text" v-model="fathers_name" placeholder="نام پدر">
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
            name: '',
            fathers_name: '',
            birthday: '',
            national_number: '',
            phone_number: '',
            email: ''
        }
    },

    mounted(){
        $(function() {
            $("#datepicker").persianDatepicker();       
        })
    }

}
</script>