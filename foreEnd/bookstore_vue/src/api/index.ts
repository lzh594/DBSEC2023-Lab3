// @ts-ignore
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
    if (method === 'post' || method === 'put' || method === 'delete') {
        return service({
            method: method,
            url: url,
            data: query,
        })
    }
}