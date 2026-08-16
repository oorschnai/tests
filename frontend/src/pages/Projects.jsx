import React, { useEffect, useState } from "react";

export default function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetch("/api/v3/projects")
      .then((response) => response.json())
      .then((data) => setProjects(data.items ?? []));
  }, []);

  return (
    <main>
      <h1>Projects</h1>
      <ul>
        {projects.map((project) => (
          <li key={project.code}>{project.name}</li>
        ))}
      </ul>
    </main>
  );
}
