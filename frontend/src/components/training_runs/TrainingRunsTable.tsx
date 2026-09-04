import type { TrainingRunSummary } from "../../types/training_runs";
import { Link } from "react-router-dom";
import { formatDuration } from "../../utils/formateDuration";
import { useRunTrainingRun } from "../../hooks/useRunTrainingRun";

interface Props {
    training_runs: TrainingRunSummary[];
    experimentId: string;
    onRunSuccess: () => void;
}

export default function TrainingRunsTable({training_runs, onRunSuccess,}: Props) {

    const {
        run,
        loading: runLoading,
        error: runError,
    } = useRunTrainingRun();

    const handleRunTrainingRun = async (trainingRunId: string) => {
    const success = await run(trainingRunId);

    if (success) {
        onRunSuccess();
    }
};

    return (
        <>
        <table>
            <thead>
                <tr>
                    <th>Experiment</th>
                    <th>Status</th>
                    <th>Created At</th>
                    <th>Duration</th>
                    <th>Results</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {
                    training_runs.map((training_run) => (
                        <tr key={training_run.id}>
                            <td>
                                <Link to={`/experiments/${training_run.experiment_id}`}>
                                    Experiment
                                </Link>
                            </td>
                            <td>
                                {training_run.status}
                            </td>
                            <td>
                                {training_run.created_at}
                            </td>
                            <td>
                                {formatDuration(
                                    training_run.started_at, 
                                    training_run.completed_at
                                ) ?? "N/A"}
                            </td>
                            <td>
                                <Link to={`/experiments/${training_run.experiment_id}/runs/${training_run.id}`}>
                                    Details
                                </Link>
                            </td>
                            <td>
                                {training_run.status === "CREATED" && (
                                    <button
                                        type="button"
                                        onClick={() =>
                                            handleRunTrainingRun(
                                                training_run.id
                                            )
                                        }
                                        disabled={runLoading}>
                                            {runLoading
                                                ? "RUNNING..."
                                                : "RUN"}
                                    </button>
                                )}
                            </td>
                        </tr>
                    ))
                }
            </tbody>
        </table>

        {runError && (
                <p>{runError}</p>
            )}
            
        {training_runs.length === 0 && (
            <h2>No training runs yet</h2>
        )}

        </>
    );
}