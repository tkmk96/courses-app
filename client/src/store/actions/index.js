import axios from 'axios';
import {FETCHED_MY_COURSES, FETCHED_TRENDING} from './types';

export const fetchTrending = () => {
    return async dispatch => {
        const res = await axios.get('/course');
        dispatch({
            type: FETCHED_TRENDING,
            payload: res.data
        });
    }
};

export const fetchMyCourses = () => {
    return async dispatch => {
        const res = await axios.get('/course');
        dispatch({
            type: FETCHED_MY_COURSES,
            payload: res.data.slice(0, 4)
        });
    }
};