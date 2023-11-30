// @ts-ignore
import qs from 'qs';
import service from "../utils/request";


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