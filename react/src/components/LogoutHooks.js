import {useGoogleLogin} from "react-google-login";

const clientId = '838132247517-n9cve8sucts7h0cp93bhjifogr3i4k88.apps.googleusercontent.com'

function LogoutHooks(){

    const onLogoutSuccess = (res) => {
        alert('Logout successful')
    };

    const onFailure = (res) => {
        console.log('[Logout hook Failed] res:', res)
    };

    const {signOut} = useGoogleLogin({
        clientId,
        onLogoutSuccess,
        onFailure,
    })

    return (
        <button onClick={signOut} className="button">
            {/*<img src="icons/google.svg"></img>*/}
            <span className="buttonText">Sign in with Google</span>
        </button>
    );

}

export default LogoutHooks;