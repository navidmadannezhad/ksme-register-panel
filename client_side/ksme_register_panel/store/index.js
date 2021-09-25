import { level1Request,level2Request, level3Request } from './http';

export const state = {
    level1Lock: false,
    level2Lock: true,
    level3Lock: true,
    level4Lock: true,

    isLoading: false,
}

export const mutations = {
    openLockOfLevel(state, args){
        eval(`state.level${args.num}Lock = false`);
    },

    changeLoadingState(state){
        state.isLoading = !state.isLoading;
    },
}

export const actions = {

    validateLevel1({commit, state}){
        let args = {
            first_name: localStorage.getItem('first_name'),
            last_name: localStorage.getItem('last_name'),
            birthday: localStorage.getItem('birthday'),
            email: localStorage.getItem('email'),
            national_number: localStorage.getItem('national_number'),
            phone_number: localStorage.getItem('phone_number')
        };

        return level1Request(args);
    },

    validateLevel2({commit, state}){
        let args = {
            educational_field: localStorage.getItem('educational_field'),
            educational_level: localStorage.getItem('educational_level'),
            student_number: localStorage.getItem('student_number'),
            skills: localStorage.getItem('skills'),
            activities: localStorage.getItem('activities')
        }

        return level2Request(args);
    },

    validateLevel3({commit, state}){
        let args = {
            first_name: localStorage.getItem('first_name'),
            last_name: localStorage.getItem('last_name'),
            birthday: localStorage.getItem('birthday'),
            email: localStorage.getItem('email'),
            national_number: localStorage.getItem('national_number'),
            phone_number: localStorage.getItem('phone_number'),
            educational_field: localStorage.getItem('educational_field'),
            educational_level: localStorage.getItem('educational_level'),
            student_number: localStorage.getItem('student_number'),
            skills: localStorage.getItem('skills'),
            activities: localStorage.getItem('activities'),
            corporate_field: localStorage.getItem('corporate_field'),
            extra_words: localStorage.getItem('extra_words')
        }

        return level3Request(args);
    },

    deleteLocalStorageItems({commit, state}){
        localStorage.removeItem('first_name');
        localStorage.removeItem('last_name');
        localStorage.removeItem('birthday');
        localStorage.removeItem('phone_number');
        localStorage.removeItem('student_number');
        localStorage.removeItem('national_number');
        localStorage.removeItem('skills');
        localStorage.removeItem('activities');
        localStorage.removeItem('corporate_field');
        localStorage.removeItem('educational_field');
        localStorage.removeItem('educational_level');
        localStorage.removeItem('extra_words');
        localStorage.removeItem('email');
    }

}