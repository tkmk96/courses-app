import React, { Component } from 'react';
import {fetchCourse, fetchSimilarCoursesForUser} from '../store/actions/index';
import {connect} from 'react-redux';
import axios from 'axios';
import {USER_ID} from '../constants/constants';
import StarRatings from 'react-star-ratings';

const result = {buy: 0, similar: 0, random: 0, similarUser: 0};

function shuffle(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

class Test extends Component {

    state = {
        courses: [],
        course: {}
    };

    async componentDidMount() {
        await this.refetch(1);
    }

    refetch = async (firstId) => {
        const ids = [];
        this.setState({courses: []});
        let res = await axios.get(`/course/${firstId}/`);
        this.setState({course: res.data});
        if (res.data.recommendBuy.length > 0) {
            const index = Math.floor(Math.random() * res.data.recommendBuy.length);
            let id = res.data.recommendBuy[index].recommended_course;
            let r = await axios.get(`/course/${id}/`);
            let course = {...r.data, type: 'buy'};
            ids.push(course.id);
            this.setState(prevState => ({courses: [...prevState.courses, course]}));
        }
        if (res.data.recommendSimilar.length > 0) {
            const index = Math.floor(Math.random() * res.data.recommendSimilar.length);
            let id = res.data.recommendSimilar[index].recommended_course;
            if (!ids.includes(id)) {
                ids.push(id);
                let r = await axios.get(`/course/${id}/`);
                let course = {...r.data, type: 'similar'};
                this.setState(prevState => ({courses: [...prevState.courses, course]}));
            }
        }
        // res = await axios.get(`/user/${USER_ID}/`);
        // if (res.data.recommendations.length > 0) {
        //     const index = Math.floor(Math.random() * res.data.recommendations.length);
        //     let id = res.data.recommendations[index].recommended_course;
        //     if (!ids.includes(id)) {
        //         ids.push(id);
        //         let r = await axios.get(`/course/${id}/`);
        //         let course = {...r.data, type: 'similarUser'};
        //         this.setState(prevState => ({courses: [...prevState.courses, course]}));
        //     }
        // }
        const id = Math.floor((Math.random() * 700) + 1);
        if (!ids.includes(id)) {
            res = await axios.get(`/course/${id}/`);
            let course = {...res.data, type: 'random'};
            this.setState(prevState => ({courses: [...prevState.courses, course]}));
        }
        let courses = [...this.state.courses];
        shuffle(courses);
        this.setState({courses});
    };

    render() {
        console.log(result);
        return(
            <div className='myCourses col-sm-12'>
                <h2 className='header'>{this.state.course.name}</h2>
                {this.state.courses.map(course => {
                    return (
                        <div key={course.id} className='course col-sm-4'>
                            <h5 className='mb20'>{course.name}</h5>
                            <div className='mb20'>
                                <StarRatings
                                    rating={course.rating || 0}
                                    starRatedColor="#419641"
                                    numberOfStars={5}
                                    starDimension='15px'
                                    starSpacing='3px'
                                />
                            </div>
                            <button className='btn btn-success'
                                onClick={() => {
                                    result[course.type] += 1;
                                    this.refetch(course.id)
                                }}
                            >See more</button>
                        </div>
                    )
                })}
            </div>
        );
    }

}
const mapStateToProps = ({similarCourses, similarCoursesForUser}) => ({similarCourses, similarCoursesForUser});

export default connect(mapStateToProps, {fetchCourse, fetchSimilarCoursesForUser})(Test);