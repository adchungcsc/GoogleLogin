import React from 'react';
import {GoogleLogin} from 'react-google-login';
import {refreshTokenSetup} from "../utils/TokenRefresh";


const clientId = '838132247517-n9cve8sucts7h0cp93bhjifogr3i4k88.apps.googleusercontent.com'

function Login() {
    const onSuccess = (res) => {
        console.log('[Login Success] currentUser: ', res.profileObj)
        refreshTokenSetup(res);
    };

    const onFailure = (res) => {
        console.log('[Login Failed] res:', res)
    };

    return (
        <div>
            <GoogleLogin clientId={clientId}
                         render={renderProps => (
                             <button onClick={renderProps.onClick} disabled={renderProps.disabled}>
                                 This is a custom google button
                             </button>
                         )}
                         buttonText="Login"
                         onSuccess={onSuccess}
                         onFailure={onFailure}
                         cookiePolicy={'single_host_origin'}
                         style={{marginTop: '100px'}}
                         isSignedIn={true}/>
        </div>
    )
}

export default Login;