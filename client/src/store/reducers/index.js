import {combineReducers} from 'redux';
import {trendingReducer} from './trendingReducer';

export default combineReducers({
    trending: trendingReducer
})