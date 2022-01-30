import firebase from 'firebase/compat/app';
import fire from '../firebase';

function SignIn() {
    
  const signInWithGoogle = () => {
    const auth = fire.auth();
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider);
  }

  return (
    <button onClick={signInWithGoogle}>Sign in with Google</button>
  )
}

export default SignIn; 