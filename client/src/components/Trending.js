import React, {Component} from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';
import {connect} from 'react-redux';
import {fetchTrending} from '../store/actions/index';

class Trending extends Component {

    componentDidMount() {
        this.props.fetchTrending();
    }

    render() {
        return(
            <div className='trending col-sm-8 col-sm-offset-2'>
                <h2 className='text-center'>Trending</h2>
                <ol className='coursesList'>{this.renderCoursesList()}</ol>
            </div>
        );
    }

    renderCoursesList() {
        return this.props.trending.map((course) => {
            return (
                <li key={course.id} className='course'>
                    <h3>{course.name}</h3>
                    <p>{course.description}</p>
                    <Link
                        className='btn btn-info'
                        to={'/course/' + course.id}
                    >
                        See more
                    </Link>
                </li>
            )
        })
    }
}

const mapStateToProps = ({trending}) => ({trending});

export default connect(mapStateToProps, {fetchTrending})(Trending);