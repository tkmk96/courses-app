import React from 'react';
import {Link} from 'react-router-dom';

const CourseInfo = (props) => {
    return (
        <li className='courseInfo'>
            <h3>{props.name}</h3>
            <p>{props.description}</p>
            <Link
                className='btn btn-info'
                to={'/course-detail/' + props.id}
            >
                See more
            </Link>
        </li>
    );
};

export default CourseInfo;