import {FETCHED_COURSE} from '../actions/types';

export const courseDetailReducer = (state = {}, action) => {
  switch (action.type) {
      case FETCHED_COURSE:
          return action.payload;
      default:
          return state;
  }
};