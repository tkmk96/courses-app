import React, {Component} from 'react';
import {Link, withRouter} from 'react-router-dom';

class Navbar extends Component {

    state = {
        expanded: false
    };

    render() {
        const {pathname} = this.props.location;
        const {expanded} = this.state;
        return(
            <nav className='navbar navbar-default'>
                <div className='container-fluid'>
                    <div className='navbar-header'>
                        <button type='button'
                                className={'navbar-toggle ' + (expanded ? '' : 'collapsed')}
                                data-toggle='collapse'
                                data-target='#bs-example-navbar-collapse-1'
                                aria-expanded={expanded}
                                onClick={() => this.setState(prevState => ({expanded: !prevState.expanded}))}
                        >
                            <span className='sr-only'>Toggle navigation</span>
                            <span className='icon-bar'></span>
                            <span className='icon-bar'></span>
                            <span className='icon-bar'></span>
                        </button>
                        <Link className='navbar-brand' to='/'>Courses</Link>
                    </div>
                    {expanded &&
                    <div className="navbar-collapse collapse in" id="bs-example-navbar-collapse-1" aria-expanded="true">
                        <ul className="nav navbar-nav">
                            <li className={pathname === '/trending' ? 'active' : ''}><Link
                                to='/trending'>Trending</Link></li>
                            <li className={pathname === '/my-courses' ? 'active' : ''}><Link to='/my-courses'>My
                                courses</Link></li>
                        </ul>
                        <ul className="nav navbar-nav navbar-right">
                            <li><Link to='/logout'>Logout</Link></li>
                        </ul>
                    </div>
                    }
                    <div className='collapse navbar-collapse'>
                        <ul className='nav navbar-nav'>
                            <li className={pathname === '/trending' ? 'active' : ''}><Link to='/trending'>Trending</Link></li>
                            <li className={pathname === '/my-courses' ? 'active' : ''}><Link to='/my-courses'>My courses</Link></li>
                        </ul>
                        <ul className='nav navbar-nav navbar-right'>
                            <li><Link to='/logout'>Logout</Link></li>
                        </ul>
                    </div>
                </div>
            </nav>
        );
    }
}

export default withRouter(Navbar);