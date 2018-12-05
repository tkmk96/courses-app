import React, { Component } from 'react';
import {fetchMyCourses, fetchSimilarCoursesForUser} from '../store/actions/index';
import {connect} from 'react-redux';
import CourseInfo from './CourseInfo';
import SimilarCourses from './SimilarCourses';

class MyCourses extends Component {

    componentDidMount() {
        this.props.fetchMyCourses();
        this.props.fetchSimilarCoursesForUser();
    }

    render() {
        return(
            <div className='myCourses col-sm-12'>
                <h2 className='header'>My bought courses</h2>
                <ul className='coursesList'>{this.renderCoursesList()}</ul>
                <SimilarCourses header='Recommended for you' courses={this.props.similarCoursesForUser}/>
            </div>
        );
    }

    renderCoursesList() {
        return this.props.myCourses.map((course) => {
            return (
                <CourseInfo key={course.id} {...course}/>
            )
        })
    }
}
const mapStateToProps = ({myCourses, similarCoursesForUser}) => ({myCourses, similarCoursesForUser});

export default connect(mapStateToProps, {fetchMyCourses, fetchSimilarCoursesForUser})(MyCourses);