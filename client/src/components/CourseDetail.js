import React, { Component } from 'react';
import StarRatings from 'react-star-ratings';
import axios from 'axios';
import SimilarCourses from './SimilarCourses';
import {USER_ID} from '../constants/constants';
import {
    buyCourse, fetchCourse, fetchMyCourses, fetchSimilarCourses, rateCourse,
    resetSimilarCourses
} from '../store/actions/index';
import {connect} from 'react-redux';

class CourseDetail extends Component {

    componentDidMount() {
        this.props.resetSimilarCourses();
        this.props.fetchMyCourses();
        const {id} = this.props.match.params;
        this.props.fetchCourse(id);
    }

    componentWillReceiveProps(nextProps) {
        const {id} = nextProps.match.params;
        if (id !== this.props.match.params.id) {
            this.props.fetchCourse(id);
            this.props.resetSimilarCourses();
        }
    }

    buy = courseId => {
        this.props.buyCourse(courseId);
        this.props.fetchMyCourses();
    };

    rate = (rating, course) => {
        const courseUser = this.props.myCourses.find(c => c.id === course).courseUser;
        this.props.rateCourse(rating, course, courseUser);
    };

    render() {
        const {courseDetail: course} = this.props;
        if (course === null) {
            return null;
        }
        const canBuy = this.props.myCourses.find(c => course.id === c.id) === undefined;
        const rating = canBuy ? null : this.props.myCourses.find(c => course.id === c.id).rating;
        return(
            <div className='courseDetail col-sm-12'>
                <h2 className='header'>{course.name}</h2>
                <h3>
                    <small>{course.lectures ? course.lectures + ' lectures | ' : '' }
                        {course.difficulty}
                    </small>
                </h3>
                <div className='ratings'>
                    <StarRatings
                        rating={course.rating}
                        starRatedColor="#f6f60d"
                        numberOfStars={5}
                        starDimension='30px'
                        starSpacing='5px'
                    />
                    <span className='count'>({course.ratingsCount} ratings)</span>
                </div>
                <h4 className='header'>{course.description}</h4>
                {canBuy ?
                    <button
                        className='btn btn-lg btn-warning'
                        onClick={() => this.buy(course.id)}
                    >
                        Buy for {course.price} €
                    </button>
                    :

                    <div>
                        <h5>Your rating:</h5>
                        {rating === null ?
                            <StarRatings
                                starRatedColor="#f6f60d"
                                numberOfStars={5}
                                starDimension='30px'
                                starSpacing='5px'
                                changeRating={(rating) => this.rate(rating, course.id)}
                            /> :
                            <StarRatings
                                rating={rating}
                                starRatedColor="#f6f60d"
                                numberOfStars={5}
                                starDimension='30px'
                                starSpacing='5px'
                            />
                        }
                    </div>
                }
                <SimilarCourses header='People also bought' courses={this.props.similarCourses}/>
            </div>
        );
    }
}

const mapStateToProps = ({myCourses, similarCourses, courseDetail}) => ({myCourses, similarCourses, courseDetail});

export default connect(mapStateToProps, {fetchMyCourses, resetSimilarCourses, fetchCourse, buyCourse, rateCourse})(CourseDetail);