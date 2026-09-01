import type { TrainingRunDetails } from "../../types/training_runs";
import { Link } from "react-router-dom";

interface Props {
    details: TrainingRunDetails;
}

export default function ExperimentDetails({details}: Props) {

    return (
        <div>
            <h2>Training Run Details</h2>
            <p>ID: {" "}{details.id}</p>
            <p>
                <Link to={`/experiments/${details.experiment_id}`} target="_blank" rel="noopener nofererrer">
                    Experiment
                </Link>
            </p>
            <p>Status:{" "}{details.status}</p>
            <p>Created At:{" "}{details.created_at}</p>
            <p>Test Size:{" "}{details.test_size}</p>
            <p>Random Seed:{" "}{details.random_seed}</p>
            <p> Started At:{" "}{details.started_at ?? "Not started"}</p>
            <p>Completed At:{" "}{details.completed_at ?? "Not started"}</p>
            {details.result && (
                <>
                    <p>Accuracy:{" "}{details.result.accuracy}</p> 
                    <p>Precision:{" "}{details.result.precision}</p> 
                    <p>Recall:{" "}{details.result.recall}</p> 
                    <p>F1 Score:{" "}{details.result.f1_score}</p> 
                </> 
            )}
        </div>
    );

}