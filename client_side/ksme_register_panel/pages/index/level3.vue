<template>
    <div class="level3">
        <div class="form">

            <div class="corp_field">
                <p class="intro">تمایل به همکاری در حوزه:</p>
                <div class="options">
                    <div class="option">
                        <input type="checkbox" id="content" name="content" value="content" v-model="content">
                        <label for="content">تولید محتوا</label>
                    </div>
                    <div class="option">
                        <input type="checkbox" id="journal" name="journal" value="journal" v-model="journal">
                        <label for="journal">مقاله نویسی</label>
                    </div>
                </div>
            </div>

            <div class="experience">
                <textarea type="text" placeholder="سخن دیگه ای؟ :)" v-model="extra_saying"></textarea>
            </div>

            <div class="next_level">
                <NuxtLink class="next_level" tag="button" to='/level4'>تکمیل فرآیند ثبت نام</NuxtLink>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return{
            content: '',
            journal: '',
            extra_saying: ''
        }
    }
}
</script>