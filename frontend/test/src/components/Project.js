import logo from "../images/mobilise-logo.png";

const Project = () => {
  return (
    <header className="project">
      <img className="mobilise-logo" src={logo} alt="mobilise logo" />
      <div className="text-content">
        <h2>Your Projects</h2>
        <p>A place to add and manage projects</p>
      </div>
      <button>Add Project</button>
    </header>
  );
};

export default Project;
