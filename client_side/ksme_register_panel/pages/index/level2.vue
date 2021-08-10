<template>
    <div class="level2">
        <div class="form">
            <div class="reshte">
                <input type="text" v-model="educational_field" placeholder="رشته تحصیلی">
            </div>
            <div class="maghta">
                <p class="intro">مقطع تحصیلی</p>
                <select name="maghta" v-model="educational_level">
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
                <textarea type="text" placeholder="فعالیت های کاری و پژوهشی" v-model="activities"></textarea>
            </div>

            <div class="next_level">
                <button class="next_level" @click="validateLevel2">مرحله بعد</button>
                <!-- <NuxtLink class="next_level" tag="button" to='/level3'>مرحله بعد</NuxtLink> -->
            </div>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return{
            educational_field: '',
            educational_level: '',
            student_number: '',
            skills: '',
            activities: ''
        }
    },
    methods:{
        validateLevel2(){
            this.changeLoadingState();

            this.pushToVuexState('educational_field', this.educational_field);
            this.pushToVuexState('educational_level', this.educational_level);
            this.pushToVuexState('student_number', this.student_number);
            this.pushToVuexState('skills', this.skills);
            this.pushToVuexState('activities', this.activities);

            this.$store.dispatch('validateLevel2')
            .then(response => {
                console.log(response.data);
                this.$store.commit('openLockOfLevel', { num: 3 });
                this.$router.push({'path': 'level3'});
            })
            .catch(err => {
                console.log(err.response.data);;
            }).finally(() => {
                this.changeLoadingState();
            })
        },

        changeLoadingState(){
            this.$store.commit('changeLoadingState');
        },

        pushToVuexState(paramName, newValue){
            this.$store.commit('renewParameter', { paramName, newValue });
        }
    }
}
</script>