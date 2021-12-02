import React from 'react'
import styled from 'styled-components'
import { loginUrl } from './spotify';

const Button = styled.button`
  padding: '20px';
  border-radius: '99px';
  background-color: 'green';
  font-weight: 600;
  color: 'green';
  text-decoration: 'none';
`;

function Login() {
    return (
        <div className="LoginButton">
            <h1>Welcome to Spotify Logins</h1>
            {/* <img src="https://getheavy.com/wp-content/uploads/2019/12/spotify2019-830x350.jpg" alt="Spotify-Logo"/> */}
            <a href={loginUrl}>
                <Button>LOGIN WITH SPOTIFY.</Button>
            </a>
        </div>
    )
}

export default Login