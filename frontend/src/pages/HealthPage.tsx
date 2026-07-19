import { useHealth } from "../hooks/useHealth";

export default function HealthPage() {

    const {
        health,
        loading,
        error
    } = useHealth();

    if (loading)
        return <p>Loading...</p>;

    if (error)
        return <p>{error}</p>;

    return (
        <>
            <h1>{health?.service}</h1>
            <p>Status: {health?.status}</p>
            <p>Version: {health?.version}</p>
            <p>{health?.timestamp}</p>
        </>
    );
    
}