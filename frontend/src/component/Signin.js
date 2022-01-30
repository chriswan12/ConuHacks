import firebase from 'firebase/compat/app';
import fire from '../firebase';
import { Button } from '@material-ui/core';

function SignIn() {
    
  const signInWithGoogle = () => {
    const auth = fire.auth();
    const provider = new firebase.auth.GoogleAuthProvider();
    auth.signInWithPopup(provider);
  }

  return (
    <Button variant="outlined" style={{padding: "10px", margin: "10px", size: "medium"}} color="primary" onClick={signInWithGoogle}>Sign in with Google</Button>
  )
}

export default SignIn; 