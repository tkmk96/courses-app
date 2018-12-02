import React, { Component, Fragment } from 'react';
import StarRatings from 'react-star-ratings';
import axios from 'axios';
import {Link} from 'react-router-dom';

const course = {
    category: 1,
    description: "The only course you need to learn web development - HTML, CSS, JS, Node, and More!",
    id: 1,
    name: "The Web Developer Bootcamp",
    price: "11.99",
    users: [136, 297, 503, 601, 816, 945, 1060, 1277, 1383, 1632, 1847, 1955, 2179, 2214, 2525, 2673, 2823, 2969],
    rating: 4.3,
    ratingsCount: 15800
};


class CourseDetail extends Component {

    state = {
        courses: []
    };

    componentDidMount() {
        axios.get('/course').then(({data}) => {
            this.setState({courses: data.slice(0, 4)});
        })
    }

    render() {
        return(
            <div className='courseDetail col-sm-12'>
                <h2 className='header'>{course.name}</h2>
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
                <button className='btn btn-lg btn-warning'>Buy for {course.price} €</button>
                {this.renderSimilarCourses()}
            </div>
        );
    }

    renderSimilarCourses() {
        return (
            <div className='recommend'>
                <h2 className='header'>Similar courses</h2>
                <div>
                    {this.state.courses.map(course => {
                        return (
                            <div key={course.id} className='course col-sm-3'>
                                <h5 className='header'>{course.name}</h5>
                                <div className='header'>
                                    <StarRatings
                                        rating={3.5}
                                        starRatedColor="blue"
                                        numberOfStars={5}
                                        starDimension='15px'
                                        starSpacing='3px'
                                    />
                                </div>
                                <Link className='btn btn-info' to={`/course/${course.id}`}>See more</Link>
                            </div>
                        )
                    })}
                </div>
            </div>
        )
    }
}

export default CourseDetail;