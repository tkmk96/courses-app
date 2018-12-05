import React, { Component } from 'react';
import StarRatings from 'react-star-ratings';
import axios from 'axios';
import SimilarCourses from './SimilarCourses';

class CourseDetail extends Component {

    state = {
        similarCourses: [],
        course: null
    };

    componentWillReceiveProps(nextProps) {
        const {id} = nextProps.match.params;
        if (id !== this.props.match.params.id) {
            this.getCourse(id);
        }
    }

    componentDidMount() {
        const {id} = this.props.match.params;
        this.getCourse(id);
        axios.get('/course/').then(({data}) => {
            this.setState({similarCourses: data.slice(0, 4)});
        })
    }

    getCourse = async (id) => {
      const res = await axios.get(`/course/${id}/`);
      this.setState({course: res.data});
    };

    render() {
        const {course} = this.state;
        if (course === null) {
            return null;
        }
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
                <button className='btn btn-lg btn-warning'>Buy for {course.price} €</button>
                <SimilarCourses courses={this.state.similarCourses}/>
            </div>
        );
    }
}

export default CourseDetail;