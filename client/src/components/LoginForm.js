import React, {Component} from 'react';
import {connect} from 'react-redux';
import {Link} from 'react-router-dom';

class LoginForm extends Component {

    state = {
        email: '',
        password: ''
    };

    render() {
        return(
            <form className='loginForm col-md-6 col-sm-offset-3' onSubmit={this._handleSubmit}>
                <h3 className='text-center'>Login</h3>
                <div className='form-group'>
                    <label className='control-label' htmlFor='emailInput'>Email</label>
                    <div className=''>
                        <input
                            className='form-control'
                            id='emailInput'
                            required
                            type='email'
                            value={this.state.email}
                            onChange={(e) => this.setState({email: e.target.value})}
                        />
                    </div>
                </div>
                <div className='form-group'>
                    <label className='control-label' htmlFor='passwordInput'>Password</label>
                    <div className=''>
                        <input
                            className='form-control'
                            id='passwordInput'
                            value={this.state.password}
                            required
                            type='password'
                            onChange={(e) => this.setState({password: e.target.value})}
                        />
                    </div>
                </div>
                <div className='buttons'>
                    <button type='submit' className='btn btn-info'>Submit</button>
                    <Link to='/register' className='btn btn-default rightBtn'>Switch to Sign Up</Link>
                </div>
            </form>
        );
    }

    _handleSubmit = e => {
        this.setState({email: '', password: ''});
        e.preventDefault();
    };
}

export default connect(null)(LoginForm);