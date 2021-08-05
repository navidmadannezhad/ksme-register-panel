import axios from 'axios';

export const state = {
    level1Lock: false,
    level2Lock: true,
    level3Lock: true,
    level4Lock: true
}

export const mutations = {
    openLockOfLevel(num, state){
        Vue.set(eval(`state.level${num}Lock`), false);
    }
}

export const actions = {

    validateLevel(context, args){
        return axios({
            url: `http://127.0.0.1:8000/api/level${args.level}/`,
            method: 'post',
            data: args.data,
        })
    }

}