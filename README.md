# A-Location-Based-Smart-Drive
Course project of UVic ECE569A - Selected Topics in Computer Engineering: Internet of Things: Analytics and Security<br>
Instructor: Wei Li<br>
Term: 2023 fall


##  Group members and Work distribution
       Project Duration: 8 weeks
       Team Members:
•	Student 1:   Yi Lu                            V00901547       yilu@uvic.ca                          QA Tester
•	Student 2:   Ruilin Wang                 V01031203       ruilinwang@uvic.ca       Backend Developer
•	Student 3:   Lian Duan                     V01047375       lduan@uvic.ca                      Database Specialist
•	Student 4:   Jiaxing Yao                  V01047304       jiaxingyao@uvic.ca                   Frontend Developer
•	Student 5:  Walaeldin Abdalla         V01042368       Walaeldina@uvic.ca    Project Manager


Ruilin Wang is the main developer for both frontend and backend. The software part of whole project is totally built by Ruilin Wang. Meanwhile, the location smart drive is developed by Wang and Jiaxing Yao offers many contributed help and work.

I extend my heartfelt gratitude to all team members for their remarkable dedication during the preparation and execution of this project. My responsibility as the Project Manager was critical to its success:
• I established a definitive scope and meticulously detailed the project requirements.
• I crafted a comprehensive project timeline, replete with milestones, adhering strictly to our established project management methodologies.
• I brought together a multifaceted team, comprising a Backend Developer, Frontend Developer, Database Specialist, and QA testers, and facilitated their collaboration.
• I carefully delineated roles and responsibilities, ensuring unambiguous ownership and accountability among the team.
The cornerstone of my role was to rigorously test and validate the functionality of our innovative smart drive system, with an unwavering focus on perfecting file organization leveraged by real-time geolocation data .As a Project Manager, my crowning achievement has been to provide unwavering support and effectively manage all activities and tasks, steering the project to completion on schedule and in alignment with the stipulated requirements. I am proud to declare that the project was a resounding success, a testament to the hard work and synergy of our dedicated team.
This final sentence highlights the successful outcome of the project, attributing it to both your leadership and the collective efforts of the team.







## Project topics
Design and implement a cloud or local-computer based portal access smart drive system with any popular web browser on a computer or a cell phone/pad. User can drag and drop files to the portal interfacing area. The system will automatically put the files in different folders (on cloud or on your local computer) based on the real time location (name of the city) of the devices, such as “Vancouver”, “Surrey”, “Victoria”, “Burnaby”, “Coquitlam”, etc. If a new location is used, the system will automatically create a new folder for this new location and find out the city name of the location to use as the folder name, if the system cannot find the name of the city, the system will ask the user. The system will confirm after uploading (success/fail).

## Project Requirements:

The project requirements can be divided into functional and non-functional categories:
1.	File Upload: Users should be able to upload files by dragging and dropping or selecting files from their devices.
2.	Location Detection: The system should determine the user's location (city) in real-time using the Google Maps API.
3.	City-Specific Folders: Automatically create folders corresponding to the detected city and organize files within these folders.
4.	User Authorization: Define roles and permissions to control user access to files and folders.
5.	User Interface: Develop a user-friendly and responsive UI for easy file uploads and user interaction.
6.	Database Management: Set up  storing user accounts Location folder , file metadata, and folder information.

Our project plan activities start  from 16/10/2023 to 25/11/2023 includes specific tasks, responsible students, and timelines :


Project 
Stages 	Date 	Project Activity	                               Tasks 
Stage 1	16/10/2023 -22/10/2023	Design and Architecture	Student 1 (Frontend Developer):Task: Design the user interface (UI) for the portal.
Student 2      (Backend Developer):Task: Design the backend architecture and API endpoints.
Student 3     (Database Specialist):Task: Design the database schema.
Stage 2	23/10/2023 25/10/2023	Design and Architecture
	      All students continue working on their design tasks as needed.
Stage 3	26/10/2023 - 30/11/2023	Design and Architecture	All students continue working on their design tasks as needed.
Stage 4	1/11/2023 - 3/11/2023):	Design and Architecture
	      All students complete their design tasks and we will Review and validate the design components with the team.
Stage 5	4/11/2023 - 7/11/2023	Development
	        Student 1 (Frontend Developer):Task: Implement the UI using React.
Student 2    (Backend Developer):Task: Develop the Flask backend.
Student 3    (Database Specialist):Task: Set up the database and schema.Task: Create the database connection.
Stage 6	7/11/2023 - 10/11/2023  Development  All students continue working on their development tasks.
Stage 7         (11/11/2023 – 15 /11/2023):Integration and Testing
             Student 4 (QA Tester):Task: Develop test cases and test plan.Student 2 (Backend Developer):Task: Integrate the frontend and backend and  Address any integration issues.
              Student 3 (Database Specialist):Task: Test database functionality.
Stage 8	(16/11/2023 - 25/11`/2023)	Final Testing, Deployment, and Documentation	Student 4 (QA Tester):Task: Execute test cases and report issues and Task: Ensure all features are working as expected.
            Student 2 (Backend Developer):Task: Deploy the system on a cloud server (e.g., Heroku).
            Student 5 (Project Manager):Task: Prepare project documentation, including user guides and README.
             Student 1 (Frontend Developer):Task: Implement final UI enhancements and user experience improvements.




Testing Plan Design:

Objective:
We set out to rigorously test and validate the functionality of our smart drive system, ensuring flawless file organization based on real-time geolocation.

Scope of Testing:
•	Functional Testing: We confirmed the drag-and-drop feature and location-based sorting worked as intended.
•	Integration Testing: We verified the seamless interaction between the frontend interface and backend services.
•	System Testing: We evaluated the complete and fully integrated application against the requirements.
•	Performance Testing: We ascertained that the system performed well under typical and peak loads.
•	Security Testing: We identified any potential vulnerabilities in handling sensitive data, particularly related to file access and location data processing.
•	Usability Testing: We confirmed that the system was user-friendly and the prompts for manual location input were intuitive.

Test Environment:
•	Location: 1) University of Victoria, Engineering Lab Wing. 'Cordova bay' and 2) 'Village park Estates'.
•	Date and Time: Monday, 13/11/2012, starting at 11:00 AM at 'Cordova bay' and continuing at 11:30 AM at 'Village park Estates'.
•	Hardware: We used  two laptop computers .
•	Software: We tested across browsers (Chrome, Firefox, Edge) with the latest updates for compatibility testing.
•	Network: We used both wired and wireless connections to simulate different network environments.

Resources:
•	Personnel: all  team Members .
•	Tools: We used automated testing tools for performance measurement, and monitoring tools for real-time observation.
•	Documentation: We prepared detailed test cases .



Test Schedule :
1.	Preparation on  9/11/2023:
•	We finalized and reviewed all test cases and scripts.
•	We set up the test environment and ensured all tools were operational.
•	We conducted a dry run of the test cases to ensure clarity and preparedness.
2.	Execution on 13/11/2023 :
•	We performed tests sequentially, starting with functional tests and proceeding through to performance and security tests.
•	We logged all actions, observations, and system responses meticulously.
•	We utilized both manual and automated testing approaches where appropriate.





