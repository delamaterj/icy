import TrainingRunsTable from "../components/training_runs/TrainingRunsTable";
import { useTrainingRuns } from "../hooks/useTrainingRuns";
import { useParams } from "react-router-dom";
import { useState } from "react";
import CreateTrainingRunForm from "../components/training_runs/TrainingRunForm";

export default function TrainingRunsPage() {

    const { id } = useParams();

    const {
        trainingRuns,
        loading,
        error,
        refresh
    } = useTrainingRuns(id ?? "");

    const [showCreateForm, setShowCreateForm] = useState(false);

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
            {showCreateForm && (
            <CreateTrainingRunForm
            experimentId={id ?? ""}
            onSuccess={() => {
            setShowCreateForm(false);
            refresh();
            }}/>
        )}
        <button
        type="button"
        onClick={() => setShowCreateForm(true)}>
            + Add Training Run
        </button>
        </>
    );
}