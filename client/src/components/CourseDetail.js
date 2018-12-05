import React, { Component } from 'react';
import StarRatings from 'react-star-ratings';
import axios from 'axios';
import SimilarCourses from './SimilarCourses';
import {USER_ID} from '../constants/constants';

class CourseDetail extends Component {

    state = {
        similarCourses: [],
        course: null
    };

    componentWillReceiveProps(nextProps) {
        const {id} = nextProps.match.params;
        if (id !== this.props.match.params.id) {
            this.getData(id);
            this.setState({similarCourses: []});
        }
    }

    componentDidMount() {
        const {id} = this.props.match.params;
        this.getData(id);
    }

    getData = async (id) => {
        const res = await axios.get(`/course/${id}/`);
        this.setState({course: res.data});
        const courses = res.data.recommendBuy.slice(0, 2);
        courses.forEach(async r => {
            const res = await axios.get(`/course/${r.recommended_course}/`);
            const {id, rating, name} = res.data;
            this.setState(prevState => ({similarCourses: [...prevState.similarCourses, {id, rating, name}]}));
        });
        const similarCourses = res.data.recommendSimilar.slice(0, 2);
        similarCourses.forEach(async r => {
            const res = await axios.get(`/course/${r.recommended_course}/`);
            const {id, rating, name} = res.data;
            this.setState(prevState => ({similarCourses: [...prevState.similarCourses, {id, rating, name}]}));
        });
    };

    buy = async courseId => {
        const formData = new FormData();
        formData.set('course', courseId);
        formData.set('user', USER_ID);
        const res = await axios({
            method: 'post',
            url: '/buy/',
            data: formData,
            config: { headers: {'Content-Type': 'multipart/form-data' }}
        });
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
                <button
                    className='btn btn-lg btn-warning'
                    onClick={() => this.buy(course.id)}
                >
                    Buy for {course.price} €
                </button>
                <SimilarCourses header='People also bought' courses={this.state.similarCourses}/>
            </div>
        );
    }
}

export default CourseDetail;