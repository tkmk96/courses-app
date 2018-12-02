import {FETCHED_MY_COURSES} from '../actions/types';

export const myCoursesReducer = (state = [], action) => {
  switch (action.type) {
      case FETCHED_MY_COURSES:
          return action.payload;
      default:
          return state;
  }
};