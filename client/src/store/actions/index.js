import axios from 'axios';
import {FETCHED_MY_COURSES, FETCHED_TRENDING} from './types';
import {USER_ID} from '../../constants/constants';

export const fetchTrending = () => {
    return async dispatch => {
        const res = await axios.get('/trending/');
        const courses = [];
        res.data.forEach(({course, name, description}) => {
            courses.push({id: course, name, description})
        });
        dispatch({
            type: FETCHED_TRENDING,
            payload: courses
        });
    }
};

export const fetchMyCourses = () => {
    return async dispatch => {
        const res = await axios.get(`/course/${USER_ID}/my_courses/`);
        const courses = [];
        res.data.forEach(({course, name, description}) => {
            courses.push({id: course, name, description})
        });
        dispatch({
            type: FETCHED_MY_COURSES,
            payload: courses.slice(0, 4)
        });
    }
};