import {combineReducers} from 'redux';
import {trendingReducer} from './trendingReducer';
import {myCoursesReducer} from './myCoursesReducer';

export default combineReducers({
    trending: trendingReducer,
    myCourses: myCoursesReducer
})