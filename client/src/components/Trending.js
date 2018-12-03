import React, {Component} from 'react';
import {connect} from 'react-redux';
import {fetchTrending} from '../store/actions/index';
import CourseInfo from './CourseInfo';

class Trending extends Component {

    componentDidMount() {
        this.props.fetchTrending();
    }

    render() {
        return(
            <div className='trending col-sm-8 col-sm-offset-2'>
                <h2 className='text-center'>Trending</h2>
                <ol>{this.renderCoursesList()}</ol>
            </div>
        );
    }

    renderCoursesList() {
        return this.props.trending.map((course) => {
            return (
                <CourseInfo key={course.id} {...course}/>
            )
        })
    }
}

const mapStateToProps = ({trending}) => ({trending});

export default connect(mapStateToProps, {fetchTrending})(Trending);