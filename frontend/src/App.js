import Homepage from "./screens/Homepage";
import fire from './firebase';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';
import { useAuthState } from 'react-firebase-hooks/auth';
import SignIn from "./component/Signin";
import './App.css'; 

function App() {

  const auth = fire.auth();
  const [user] = useAuthState(auth);

  return (
    <div className="App">
      <h1 className="title">Welcome to NoteIt</h1>
      {user ? <Homepage user={user}/>  : <SignIn />}
    </div>
  );
}

export default App;
