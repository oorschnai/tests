import React, { useEffect, useState } from "react";

const STATUS_ORDER = ["down", "grace", "up", "paused"];

export default function Checks() {
  const [checks, setChecks] = useState([]);

  useEffect(() => {
    fetch("/api/v3/checks")
      .then((response) => response.json())
      .then((data) => {
        const items = data.items ?? [];
        items.sort(
          (a, b) => STATUS_ORDER.indexOf(a.status) - STATUS_ORDER.indexOf(b.status),
        );
        setChecks(items);
      });
  }, []);

  return (
    <main>
      <h1>Checks</h1>
      <table>
        <tbody>
          {checks.map((check) => (
            <tr key={check.code}>
              <td>{check.name}</td>
              <td>{check.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
