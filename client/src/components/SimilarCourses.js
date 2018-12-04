import React from 'react';
import StarRatings from 'react-star-ratings';
import {Link} from 'react-router-dom';

const SimilarCourses = (props) => {
    return (
        <div className='recommend'>
            <h2 className='mb20 text-center'>Similar courses</h2>
            <div className='courses'>
                {props.courses.map(course => {
                    return (
                        <div key={course.id} className='course col-sm-3'>
                            <h5 className='mb20'>{course.name}</h5>
                            <div className='mb20'>
                                <StarRatings
                                    rating={course.rating}
                                    starRatedColor="#419641"
                                    numberOfStars={5}
                                    starDimension='15px'
                                    starSpacing='3px'
                                />
                            </div>
                            <Link className='btn btn-success' to={`/course-detail/${course.id}`}>See more</Link>
                        </div>
                    )
                })}
            </div>
        </div>
    )
};

export default SimilarCourses;