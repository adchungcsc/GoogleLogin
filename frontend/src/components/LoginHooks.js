import {refreshTokenSetup} from "../utils/TokenRefresh";
import {useGoogleLogin} from "react-google-login";

const clientId = '838132247517-n9cve8sucts7h0cp93bhjifogr3i4k88.apps.googleusercontent.com'

function LoginHooks(){
    const onSuccess = (res) => {
        console.log('[Login Success] currentUser: ', res.profileObj)
        refreshTokenSetup(res);
    };

    const onFailure = (res) => {
        console.log('[Login Failed] res:', res)
    };

    const {signIn} = useGoogleLogin({
        onSuccess,
        onFailure,
        clientId,
        isSignedIn: true,
        accessType: 'offline',
    })

    return (
        <button onClick={signIn} className="button">
            {/*<img src="icons/google.svg"></img>*/}
            <span className="buttonText">Sign in with Google</span>
        </button>
    );

}

export default LoginHooks;