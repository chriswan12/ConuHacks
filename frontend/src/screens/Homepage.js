import React, { useState } from 'react'; 
import axios from 'axios'; 

const Homepage = () => { 
    const [selectedFile, setSelectedFile] = useState();
	const [isFilePicked, setIsFilePicked] = useState(false);

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsFilePicked(true);
	};

    // Submit data to the backend with the file 
	const handleSubmission = async () => {
		let formField = new FormData(); 

		if (isFilePicked) { 
			formField.append('inputtedFile', selectedFile); 
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
			</div>
        </div>
    )
}

export default Homepage;