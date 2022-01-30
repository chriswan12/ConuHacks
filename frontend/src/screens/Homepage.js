import React, { useState } from 'react'; 
import axios from 'axios'; 
import fire from '../firebase'; 
import 'firebase/auth'; 

const Homepage = ( {user} ) => { 	
    const [selectedFile, setSelectedFile] = useState(null);
	const [isFilePicked, setIsFilePicked] = useState(false);

	const handleSignOut = async () => {
		const auth = fire.auth();
    	auth.signOut();
	}

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsFilePicked(true);
	};

    // Submit data to the backend with the file 
	const handleSubmission = async () => {
		const email = user.email;
	
		if (selectedFile == null) { 
			return 
		}

		let formField = new FormData(); 

		
		if (isFilePicked) { 
			formField.append('inputtedFile', selectedFile); 
			formField.append('useremail', email); 
		}
		

		await axios({
			method: 'post',
			url: 'http://127.0.0.1:8000/api/create',
			data: formField
		}).then((res) => { 
			console.log('DATA: ', res.data);  
		})
	};

    return (
        <div> 
            <input type="file" name="file" onChange={changeHandler} />
			<div>
				<button onClick={handleSubmission}>Submit</button>
				<button onClick={() => handleSignOut()}>Sign Out</button>
			</div>
        </div>
    )
}

export default Homepage;