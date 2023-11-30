// @ts-ignore
import qs from 'qs';
import request from '../utils/request';
import service from "../utils/request";


export const fetchData = () => {
    return request({
        url: './table.json',
        method: 'get'
    });
};

interface RequestDataParams {
    url: string;
    method: string;
    query: any;
}

export function requestData({url, method, query}: RequestDataParams) {
    if (method === 'get') {
        return service({
            method: method,
            params: query,
            url: url
        })
    }
    if (method === 'post') {
        return service({
            method: method,
            url: url,
            // data: qs.stringify(query)
            data: query,
        })
    }
}