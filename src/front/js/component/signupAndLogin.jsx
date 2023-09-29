import React from 'react';
import LoginForm from './loginForm.jsx';
import SignupForm from './signupForm.jsx';

const DropdownButton = ({ label, className, children }) => (
    <div className={`dropdown-center ${className}`}>
        <button
            className={`btn dropdown-toggle ${className}`}
            type='button'
            data-bs-toggle="dropdown"
            aria-expanded="false"
        >
            {label}
        </button>
        <div className="dropdown-menu dropdown-menu-end p-2 me-0">
            {children}
        </div>
    </div>
);

const SignupAndLogin = () => {
    return (
        <>
            <DropdownButton label="Sign Up" className="btn-secondary me-2">
                <SignupForm />
            </DropdownButton>

            <DropdownButton label="Log In" className="btn-primary">
                <LoginForm />
            </DropdownButton>
        </>
    );
}

export default SignupAndLogin;