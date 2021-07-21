import { apiUrl } from "../api";
import { useState, useEffect } from "react";

const Job = () => {
  const [data, setData] = useState(null);
  const [application, setApplication] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = () => {
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.log(error));
  };

  const postData = () => {
    fetch(apiUrl, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHTTPRequest",
      },
    })
      .then((response) => response.json())
      .then((data) => setApplication(data))
      .catch((err) => console.log(err));
  };

  return (
    <div className="data">
      <h2>Job Details</h2>
      {data && (
        <div>
          <p>{data.id}</p>
          <p>{data.name}</p>
          <p>{data.role}</p>
        </div>
      )}
      {application && (
        <div>
          <h2>Success! You applied to job number {application.job_id} as:</h2>
          <p>{application.candidate_email}</p>
        </div>
      )}
      <button onClick={postData}>Apply</button>
    </div>
  );
};

export default Job;
