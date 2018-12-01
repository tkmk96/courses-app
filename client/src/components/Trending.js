import React, {Component} from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';

class Trending extends Component {

    state = {
        courses: []
    };

    componentDidMount() {
        axios.get('/course').then(res => {
            const courses = res.data;
            this.setState({courses: courses.slice(0, 10)});
        });
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
        return this.state.courses.map((course) => {
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

export default Trending;