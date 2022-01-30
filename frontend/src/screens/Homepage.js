import React, { useState } from 'react'; 
import axios from 'axios'; 
import fire from '../firebase'; 
import 'firebase/auth'; 
import { Button } from '@material-ui/core';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import Tooltip from '@material-ui/core/Tooltip';
import HelpIcon from '@material-ui/icons/Help';

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
			<Button
				variant="contained"
				color="default"
				startIcon={<CloudUploadIcon />}
				style={{padding: "12px", margin: "10px"}}
			>
			<input type="file" name="file" onChange={changeHandler} />
			</Button> 
			<Tooltip title="upload a file to get an email on a given zoom transcript"><HelpIcon /></Tooltip>
			<div>	
				<Button style={{padding: "8px", margin: "10px"}} variant="outlined"color="primary" onClick={handleSubmission}>Submit</Button>
				<Button style={{padding: "8px", margin: "10px"}}  color="primary" variant="outlined" onClick={() => handleSignOut()}>Sign Out</Button>
			</div>
        </div>
    )
}

export default Homepage;