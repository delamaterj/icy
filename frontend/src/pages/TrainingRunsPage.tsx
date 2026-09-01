import TrainingRunsTable from "../components/training_runs/TrainingRunsTable";
import { useTrainingRuns } from "../hooks/useTrainingRuns";
import { useParams } from "react-router-dom";

export default function TrainingRunsPage() {

    const { id } = useParams();

    const {
        trainingRuns,
        loading,
        error
    } = useTrainingRuns(id ?? "");

    if (loading) {
        return <p>Loading training runs...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <>
            <h1>Training Runs</h1>
            <TrainingRunsTable
                training_runs={trainingRuns}
                experimentId={id ?? ""}
            />
        </>
    );
}