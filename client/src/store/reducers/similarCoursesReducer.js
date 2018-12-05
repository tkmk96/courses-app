import {FETCHED_SIMILAR_COURSE, RESET_SIMILAR_COURSE} from '../actions/types';

export const similarCoursesReducer = (state = [], action) => {
  switch (action.type) {
      case FETCHED_SIMILAR_COURSE:
          return [...state, action.payload];
      case RESET_SIMILAR_COURSE:
          return [];
      default:
          return state;
  }
};