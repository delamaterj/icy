import { useParams } from "react-router-dom";
import { useTrainingRunResults } from "../hooks/useTrainingRunResults";
import TrainingRunResults from "../components/training_runs/TrainingRunResults";

export default function ExperimentDetailsPage() {

    const { id, id2 } = useParams();

    const {
        trainingRuns,
        loading,
        error
    } = useTrainingRunResults(id ?? "", id2 ?? "");

    if (loading) {
        return <p>Loading results...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    if (!trainingRuns) {
        return <p>Training run results not found.</p>;
    }

    return (
        <>
            <TrainingRunResults
                details={trainingRuns}
            />
        </>
    );
}