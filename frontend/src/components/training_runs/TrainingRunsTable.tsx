import type { TrainingRunSummary } from "../../types/training_runs";
import { Link } from "react-router-dom";
import { formatDuration } from "../../utils/formateDuration";

interface Props {
    training_runs: TrainingRunSummary[];
}

export default function TrainingRunsTable({training_runs}: Props) {

    return (

        <table>
            <thead>
                <tr>
                    <th>Experiment</th>
                    <th>Status</th>
                    <th>Created At</th>
                    <th>Duration</th>
                    <th>Results</th>
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
                                    Results
                                </Link>
                            </td>
                        </tr>
                    ))
                }
            </tbody>
        </table>
    );
}