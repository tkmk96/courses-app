import {FETCHED_TRENDING} from '../actions/types';

export const trendingReducer = (state = [], action) => {
  switch (action.type) {
      case FETCHED_TRENDING:
          return action.payload;
      default:
          return state;
  }
};