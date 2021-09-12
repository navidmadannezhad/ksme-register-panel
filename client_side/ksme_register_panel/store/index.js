import { level1Request,level2Request, level3Request } from './http';

export const state = {
    level1Lock: false,
    level2Lock: true,
    level3Lock: true,
    level4Lock: true,

    isLoading: false,

    first_name: '',
    last_name: '',
    birthday: '',
    email: '',
    national_number: '',
    phone_number: '',
    educational_field: '',
    educational_level: '',
    student_number: '',
    skills: '',
    activities: '',
    extra_words: '',
    corporate_field:''
}

export const mutations = {
    renewParameter(state, args){
        eval(`state.${args.paramName} = "${args.newValue}"`);
    },
    
    openLockOfLevel(state, args){
        eval(`state.level${args.num}Lock = false`);
    },

    changeLoadingState(state){
        state.isLoading = !state.isLoading;
    }
}

export const actions = {

    validateLevel1({commit, state}){
        let args = {
            first_name: state.first_name,
            last_name: state.last_name,
            birthday: state.birthday,
            email: state.email,
            national_number: state.national_number,
            phone_number: state.phone_number
        };

        return level1Request(args);
    },

    validateLevel2({commit, state}){
        let args = {
            educational_field: state.educational_field,
            educational_level: state.educational_level,
            student_number: state.student_number,
            skills: state.skills,
            activities: state.activities
        }

        return level2Request(args);
    },

    validateLevel3({commit, state}){
        let args = {
            first_name: state.first_name,
            last_name: state.last_name,
            birthday: state.birthday,
            email: state.email,
            national_number: state.national_number,
            phone_number: state.phone_number,
            educational_field: state.educational_field,
            educational_level: state.educational_level,
            student_number: state.student_number,
            skills: state.skills,
            activities: state.activities,
            corporate_field: state.corporate_field,
            extra_words: state.extra_words
        }

        return level3Request(args);
    },

}