import axios from 'axios';
import {FETCHED_TRENDING} from './types';

export const fetchTrending = () => {
    return async dispatch => {
        const res = await axios.get('/course');
        dispatch({
            type: FETCHED_TRENDING,
            payload: res.data
        });
    }
};