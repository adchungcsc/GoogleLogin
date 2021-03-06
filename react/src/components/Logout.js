import React from 'react';
import {GoogleLogout} from 'react-google-login';

const clientId = '838132247517-n9cve8sucts7h0cp93bhjifogr3i4k88.apps.googleusercontent.com'

function Logout() {
    const onSuccess = () => {
        alert('Logout successful')
    };

    return (
        <div>
            <GoogleLogout clientId={clientId}
                          buttonText="Logout"
                          onLogoutSuccess={onSuccess} />
        </div>
    )
}

export default Logout;