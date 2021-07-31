<template>
    <div class="level2">
        <div class="form">
            <div class="reshte">
                <input type="text" v-model="reshte" placeholder="رشته تحصیلی">
            </div>
            <div class="maghta">
                <p class="intro">مقطع تحصیلی</p>
                <select name="maghta" v-model="maghta">
                    <option value="select" selected disabled>انتخاب کنید</option>
                    <option value="diplom">دیپلم</option>
                    <option value="fogh_diplom">فوق دیپلم</option>
                    <option value="karshenasi">کارشناسی</option>
                    <option value="karshenasi_arshad">کارشناسی ارشد</option>
                    <option value="doctora">دکترا</option>
                </select>
            </div>
            <div class="student_number">
                <input type="text" placeholder="شماره دانشجویی" v-model="student_number">
            </div>
            <div class="skills">
                <textarea type="text" placeholder="توانایی ها (علمی گرفته تا اخلاقی)" v-model="skills"></textarea>
            </div>
            <div class="experience">
                <textarea type="text" placeholder="فعالیت های کاری و پژوهشی" v-model="experience"></textarea>
            </div>

            <div class="next_level">
                <NuxtLink class="next_level" tag="button" to='/level3'>مرحله بعد</NuxtLink>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return{
            reshte: '',
            maghta: '',
            student_number: '',
            skills: '',
            experience: ''
        }
    }
}
</script>