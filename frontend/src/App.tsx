import { useEffect, useState } from "react";

interface HealthResponse {
  status: string;
  service: string;
  version: string;
  timestamp: string;
}

function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null);

  useEffect(() => {
    async function fetchHealth() {
      try {
        const response = await fetch("http://localhost:5000/health");

        if (!response.ok) {
          throw new Error("Failed to fetch backend health.");
        }

        const data: HealthResponse = await response.json();
        setHealth(data);
      } catch (error) {
        console.error(error);
      }
    }

    fetchHealth();
  }, []);

  return (
    <main style={{ padding: "2rem" }}>
      <h1>ICY</h1>

      {health ? (
        <>
          <h2>{health.service}</h2>
          <p>Status: {health.status}</p>
          <p>Version: {health.version}</p>
          <p>{health.timestamp}</p>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </main>
  );
}

export default App;