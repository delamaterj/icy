import { useParams } from "react-router-dom";
import { useExperiment } from "../hooks/useExperiment";
import ExperimentDetails from "../components/experiments/ExperimentDetails";

export default function ExperimentDetailsPage() {

    const { id } = useParams();

    const {
        experiment,
        loading,
        error
    } = useExperiment(id ?? "");

    if (loading) {
        return <p>Loading experiment...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    if (!experiment) {
        return <p>Experiment not found.</p>;
    }

    return (
        <>
            <h1>
                Experiment Details
            </h1>
            <ExperimentDetails
                experiment={experiment}
            />
        </>
    );
}