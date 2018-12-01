import React, { Component, Fragment } from 'react';
import Trending from "./components/Trending";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap-theme.min.css';
import './App.scss';
import Navbar from './components/Navbar';
import {BrowserRouter, Route} from 'react-router-dom';
import MyCourses from './components/MyCourses';
import CourseDetail from './components/CourseDetail';

class App extends Component {
    render() {
        return (
            <BrowserRouter>
                <Fragment>
                    <Navbar/>
                    <div className="container">
                        <div className="row">
                            <Route path='/trending' component={Trending} />
                            <Route path='/my-courses' component={MyCourses} />
                            <Route path='/course/:id' component={CourseDetail} />
                        </div>
                    </div>
                </Fragment>
            </BrowserRouter>
        );
    }
}

export default App;
