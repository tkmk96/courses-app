import {combineReducers} from 'redux';
import {trendingReducer} from './trendingReducer';
import {myCoursesReducer} from './myCoursesReducer';
import {courseDetailReducer} from './courseDetailReducer';
import {similarCoursesReducer} from './similarCoursesReducer';
import {similarCoursesForUserReducer} from './similarCoursesForUserReducer';

export default combineReducers({
    trending: trendingReducer,
    myCourses: myCoursesReducer,
    courseDetail: courseDetailReducer,
    similarCourses: similarCoursesReducer,
    similarCoursesForUser: similarCoursesForUserReducer,
})