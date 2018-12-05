import {FETCHED_MY_COURSE, FETCHED_MY_COURSES} from '../actions/types';

export const myCoursesReducer = (state = [], action) => {
  switch (action.type) {
      case FETCHED_MY_COURSES:
          return action.payload;
      case FETCHED_MY_COURSE:
          return [...state, action.payload];
      default:
          return state;
  }
};