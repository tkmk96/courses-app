import axios from 'axios';
import {
    FETCHED_COURSE, FETCHED_MY_COURSE, FETCHED_MY_COURSES, FETCHED_SIMILAR_COURSE, FETCHED_SIMILAR_COURSE_FOR_USER,
    FETCHED_TRENDING,
    RESET_SIMILAR_COURSE, RESET_SIMILAR_COURSE_FOR_USER
} from './types';
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
        res.data.forEach(({course, name, description, id, rating}) => {
            courses.push({id: course, courseUser: id, name, description, rating})
        });
        dispatch({
            type: FETCHED_MY_COURSES,
            payload: courses
        });
    }
};

export const fetchCourse = (id) => {
    return async dispatch => {
        const res = await axios.get(`/course/${id}/`);
        dispatch({
            type: FETCHED_COURSE,
            payload: res.data
        });
        dispatch(fetchSimilarCourses(res.data))
    }
};

export const fetchSimilarCoursesForUser = () => {
    return async dispatch => {
        dispatch(resetSimilarCoursesForUser());
        const res = await axios.get(`/user/${USER_ID}/`);
        const courses = res.data.recommendations;
        courses.forEach(async r => {
            const res = await axios.get(`/course/${r.recommended_course}/`);
            const {id, rating, name} = res.data;
            dispatch({
                type: FETCHED_SIMILAR_COURSE_FOR_USER,
                payload: {id, rating, name}
            });
        });
    }
};

export const buyCourse = (courseId) => {
    return async dispatch => {
        const formData = new FormData();
        formData.set('course', courseId);
        formData.set('user', USER_ID);
        const response = await axios({
            method: 'post',
            url: '/buy/',
            data: formData,
            config: { headers: {'Content-Type': 'multipart/form-data' }}
        });
        dispatch(fetchCourse(courseId));
        const res = await axios.get(`/buy/${response.data.id}/`);
        const {course, name, description, id, rating} = res.data;
        dispatch({
            type: FETCHED_MY_COURSE,
            payload: {id: course, courseUser: id, name, description, rating}
        })
    }
};

export const rateCourse = (newRating, courseId, courseUserId) => {
    return async dispatch => {
        const formData = new FormData();
        formData.set('rating', newRating);
        const response = await axios({
            method: 'patch',
            url: `/buy/${courseUserId}/`,
            data: formData,
            config: { headers: {'Content-Type': 'multipart/form-data' }}
        });
        dispatch(fetchCourse(courseId));
        const res = await axios.get(`/buy/${response.data.id}/`);
        const {course, name, description, id, rating} = res.data;
        dispatch({
            type: FETCHED_MY_COURSE,
            payload: {id: course, courseUser: id, name, description, rating}
        })
    }
};

export const fetchSimilarCourses = (course) => {
    return async (dispatch) => {
        dispatch(resetSimilarCourses());
        const ids = [];
        const courses = course.recommendBuy.slice(0, 2);
        courses.forEach(async r => {
            const res = await axios.get(`/course/${r.recommended_course}/`);
            const {id, rating, name} = res.data;
            ids.push(id);
            dispatch({
                type: FETCHED_SIMILAR_COURSE,
                payload: {id, rating, name}
            });
        });
        const similarCourses = course.recommendSimilar.slice(0, 2);
        similarCourses.forEach(async r => {
            if (!ids.includes(r.recommended_course)) {
                const res = await axios.get(`/course/${r.recommended_course}/`);
                const {id, rating, name} = res.data;
                dispatch({
                    type: FETCHED_SIMILAR_COURSE,
                    payload: {id, rating, name}
                });
            }
        });
    }
};

export const resetSimilarCourses = () => {
    return {
        type: RESET_SIMILAR_COURSE
    }
};

export const resetSimilarCoursesForUser = () => {
    return {
        type: RESET_SIMILAR_COURSE_FOR_USER
    }
};

