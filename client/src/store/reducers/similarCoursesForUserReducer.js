import {
    FETCHED_SIMILAR_COURSE, FETCHED_SIMILAR_COURSE_FOR_USER, RESET_SIMILAR_COURSE,
    RESET_SIMILAR_COURSE_FOR_USER
} from '../actions/types';

export const similarCoursesForUserReducer = (state = [], action) => {
  switch (action.type) {
      case FETCHED_SIMILAR_COURSE_FOR_USER:
          return [...state, action.payload];
      case RESET_SIMILAR_COURSE_FOR_USER:
          return [];
      default:
          return state;
  }
};