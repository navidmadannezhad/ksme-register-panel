import axios from 'axios';

let level1Request = (data, config) => {
    return axios({
        url: process.env.level1_url,
        method: 'POST',
        data: data
    })
}

let level2Request = (data, config) => {
    return axios({
        url: process.env.level2_url,
        method: 'POST',
        data: data
    })
}

let level3Request = (data, config) => {
    return axios({
        url: process.env.level3_url,
        method: 'POST',
        data: data
    })
}

export { level1Request, level2Request, level3Request };