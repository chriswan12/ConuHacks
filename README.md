# ConuHacks

## Inspiration
Upon returning to online school from our internships, we realized that waking up for 9 a.m courses were very difficult and that often it was difficult to retain all the material discussed during lectures. As a result students often need to take time to re-watch lectures which is a chore. We wanted to remove and reduce the need to do this.

## What it does
Due to how common it was for professors to upload Zoom lectures along with Zoom transcriptions, we wanted to pick out the main talking points of each lecture. NoteIt is a web application that employs machine learning and natural language processing that processes these transcripts that were provided into a more condensed version that takes less time to read and process compared to rewatching full lecture recordings. The condensed text is then exported to an MS Word document and then emailed to your Gmail account.

## How we built it
We used Django for handling our data using a REST framework. React.js, HTML/CSS and bits of material-UI components were used to render our simple web page, lastly Google Firebase was used for authentication of Google accounts. The NLP/ML solution was developed using Python, and libraries such as SpaCy, nltk to create the summarized text. A library is then used to create a MS Word document which will be sent to your Gmail using the Python SMTP library and Google Firebase email data.

## Challenges we ran into
One of the challenges we ran into was to get the Django backend working as neither of us had much experience working with it, it was a massive time sink to get it set up and working. The biggest challenge that we encountered was to get the NLP portion to work. It was extremely hard to get a model that could do somewhat better than utter nonsense, however, we did make some progress. Results could always be better.

## Accomplishments that we're proud of
We are quite proud to make this project as a team of two, it was a relatively large implementation overall, and we are just proud to have been able to finish within a good amount of time and a relatively good working result.

## What we learned
Things we learned include REST design frameworks, methods for performing text analysis, overall getting a good sense of workflow and some experience designing software and working as a team. 

## What's next for NoteIt
If possible we would very much like to improve the NLP accuracy of NoteIt so that results can be more accurate and consistent. NoteIt can also use a better UI given more time!```
