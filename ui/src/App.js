import React from 'react';
import './App.css';

// window.location.href.split('/')[2]
const PROJ_NAME = 0;
const USER = 1;
const HW1_AVAIL = 2;
const HW1_CAP = 3;
const HW2_AVAIL = 4;
const HW2_CAP = 5;

// App: Function that runs Project
function App() {
	return (
		<div className="App">
			<header className="App-header">
				<Projects />
			</header>
		</div>
	);
}

export default App;

// Project: Displays the list of projects to page
class Projects extends React.Component {
	render() {
		return (
			<div className="projectWrap">
				<p className="projectTitle">Projects</p>
				<ProjectData />
				<div className="emptySpace" />
			</div>
		)
	}
}

// Place data into a stored list
class ProjectData extends React.Component {

	// Initialize data
	constructor(props) {
		super(props);
		this.state = {
			currProjectName: "",
			currProjectUser: "",
			project_list: []
		};

		// get and print data from "init"
		GetInitialData(props);

		this.state.project_list.push([0, "Project 0", "User 1", "HWSet1: 50/100", "HWSet2: 30/100"])
		this.state.project_list.push([1, "Project 1", "User 2", "HWSet1: 50/100", "HWSet2: 0/100"])
		this.state.project_list.push([2, "Project 2", "User 3", "HWSet1: 50/50", "HWSet2: 30/40"])
		this.state.project_list.push([3, "Project 3", "User 4", "HWSet1: 50/70", "HWSet2: 30/50"])
	}

	// Create a single project with given data
	renderProject(i, proj, usr, hw1, hw2) {
		return (
			<Project
				key={i.toString()}  // "key" is recommended by console (don't use it much in project tho)
				idx={i}
				Name={proj}
				User={usr}
				HWSet1={hw1}
				HWSet2={hw2}
				onCheckInClick={() => this.handleCheckIn(i)}
				onCheckOutClick={() => this.handleCheckOut(i)}
			/>
		)
	}

	// Create template that prompts user to make new project
	renderNewProject() {
		return (
			<ProjectAdder
				onNewProjectClick={() => this.handleNewProject()}
				onNewProjectName={() => this.handleNewProjectName()}
				onNewProjectUser={() => this.handleNewProjectUser()}
			/>
		)
	}

	// Update page with the data stored
	render() {
		const new_project_list = []
		const project_list = this.state.project_list.slice()
		for (let i = 0; i < project_list.length; i++) {
			const project_data = project_list[i];
			new_project_list.push(this.renderProject(project_data[0],
				project_data[1],
				project_data[2],
				project_data[3],
				project_data[4]))
		}
		return (
			<div>
				{new_project_list}
				<div className="emptySpace" />
				{this.renderNewProject()}
			</div>
		)
	}

	//// Handlers

	// Check-In HWSet
	handleCheckIn(i) {
		/* Get current list and hw selection index */
		const project_list = this.state.project_list.slice();

		/* Get input value (chk-in value) and make sure it's not empty */
		const check_in_val = document.getElementById("check_in:" + project_list[i][1]).value;
		if(check_in_val !== "" && !isNaN(check_in_val)) {

			/* Get current value and capacity of hw selection */

			project_list[i][3] = "HWSet 1: " + check_in_val + "/100";

			/* Set chk-in values to state */
			this.setState({
				project_list: project_list
			});

			/* Clear input text fields */
			document.getElementById("check_in:" + project_list[i][1]).value = "";
		}

		GetCheckInData(project_list[i], parseInt(check_in_val));
	}

	// Check-In HWSet
	handleCheckOut(i) {
		const project_list = this.state.project_list.slice();
		project_list[i][3] = "HWSet 1: 0/100";
		this.setState({
			project_list: project_list
		});
	}

	// Add new HWSet to Data
	handleNewProject() {
		const projectName = this.state.currProjectName;
		const projectUser = this.state.currProjectUser;
		if (typeof projectName === 'string' && typeof projectUser === 'string') {
			if (projectName.trim() !== '' && projectUser.trim() !== '') {
				const project_list = this.state.project_list.slice();
				project_list.push([project_list.length, projectName, projectUser, "HWSet 1: 55/70", "HWSet 2: 31/50"]);
				this.setState({
					project_list: project_list,
				})
				document.getElementById("newProjectName").value = "";
				document.getElementById("newProjectUser").value = "";
			}
		}
	}

	// Update value of current new project name
	handleNewProjectName() {
		var newProjectName = document.getElementById("newProjectName").value;
		this.setState({
			currProjectName: newProjectName
		})
	}

	// Update value of current user
	handleNewProjectUser() {
		var newProjectUser = document.getElementById("newProjectUser").value;
		this.setState({
			currProjectUser: newProjectUser
		})
	}

}

// 

/* Return data at given url */
async function GetInitialData(props) {

	// fetch from url, but wait for the data
	const response = await fetch("/init");
	// obtain json and parse it
	// var data = JSON.parse(JSON.stringify(await response.json()));
	console.log(await response.json());
	// return the json

	// console.log("Project 0: " + data.proj0[PROJ_NAME]);
	// console.log("Project 1: " + data.proj1[PROJ_NAME]);
	// console.log("Project 2: " + data.proj2[PROJ_NAME]);
	// console.log("Project 3: " + data.proj3[PROJ_NAME]);

	// return data;
}

/* Return data at given url */
async function GetCheckInData(project_list, val) {

	// console.log(project_list[1]);
	// console.log(val);

	const newData = {"HWSet1": val, "HWSet2": 50};

	alert(val + " hardware checked in");

	const result = await fetch('/check_in', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newData)
    })

	const resultInJson = await result.json();
	// console.log(resultInJson);

	// // fetch from url, but wait for the data
	// const response = await fetch("/hardware/proj_id=<HWSet1>/chk_out=<qty>");
	// // obtain json and parse it
	// var data = JSON.parse(JSON.stringify(await response.json()));
	// return the json

	// console.log(data.proj0[PROJ_NAME]);

	return newData;
}

// HTML Functions

/* Project: Format Project with props given */
function Project(props) {
	return (
		<div className="project">
			{/* Title */}
			<div className="column">
				<p className="projectName">{props.Name}</p>
			</div>
			{/* Users with Access */}
			<div className="column">
				<p className="user">{props.User}</p>
			</div>
			{/* Sets available */}
			<div className="column">
				<p className="hwDescription">{props.HWSet1}</p>
				<p className="hwDescription">{props.HWSet2}</p>
			</div>
			{/* Select HW */}
			<div className="column">
				<p className="hwDescription">Select HWSet:</p>
				<select className="hwSelect" name="hwset" id="hwset">
					<option value="hws1">HWSet 1</option>
					<option value="hws1">HWSet 2</option>
				</select>
			</div>
			{/* Check In */}
			<div className="column">
				<input className="hwInput"
					id={"check_in:" + props.Name}
					type="text"
					placeholder="Enter Value" />
				<button className="checkBtn"
					type="button"
					onClick={props.onCheckInClick} >
					Check In
				</button>
			</div>
			{/* Check Out*/}
			<div className="column">
				<input className="hwInput"
					id={"check_out:" + props.Name}
					type="text"
					placeholder="Enter Value" />
				<button className="checkBtn"
					type="button"
					onClick={props.onCheckOutClick} >
					Check Out
				</button>
			</div>
			{/* Join or Leave */}
			<div className="column">
				<button className="joinBtn" type="button">Join</button>
			</div>
		</div>
	)
}

/* ProjectAdder: Adds a user input to project data */
function ProjectAdder(props) { // TODO: NEED TO IMPLEMENT ADDING TO MEMORY GIVEN INPUT
	return (
		<div className="project">
			{/* Title */}
			<div className="newProjectColumn">
				<input className="newProjectInput"
					id="newProjectName"
					type="text"
					placeholder="Enter Project Name"
					onChange={props.onNewProjectName}
				/>
			</div>
			{/* Users with Access */}
			<div className="newProjectColumn">
				<input className="newProjectInput"
					id="newProjectUser"
					type="text"
					placeholder="Enter User Name"
					onChange={props.onNewProjectUser}
				/>
			</div>
			{/* Join or Leave */}
			<div className="newProjectColumn">
				<button className="addProjectBtn" type="button" onClick={props.onNewProjectClick}>Add Project</button>
			</div>
		</div>
	)
}
