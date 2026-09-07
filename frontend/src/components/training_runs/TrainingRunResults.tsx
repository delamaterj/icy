import type { TrainingRunDetails } from "../../types/training_runs";
import { Link } from "react-router-dom";

interface Props {
    details: TrainingRunDetails;
}

export default function ExperimentDetails({details}: Props) {

    return (
        <>
            <h2>Training Run Details</h2>

            <div className="details-grid">

            <div className="detail-item">
                <strong>ID: </strong>
                <span>{details.id}</span>
            </div>
            <div className="detail-item">
                <Link to={`/experiments/${details.experiment_id}`} target="_blank" rel="noopener nofererrer">
                    Experiment
                </Link>
            </div>
            <div className="detail-item">
                <strong>Status: </strong>
                <span>{details.status}</span>
            </div>
            <div className="detail-item">
                <strong>Created At: </strong>
                <span>{details.created_at}</span>
            </div>
            <div className="detail-item">
                <strong>Test Size: </strong>
                <span>{details.test_size}</span>
            </div>
            <div className="detail-item">
                <strong>Random Seed: </strong>
                <span>{details.random_seed}</span>
            </div>
            <div className="detail-item">
                <strong>Started At: </strong>
                <span>{details.started_at ?? "Not started"}</span>
            </div>
            <div className="detail-item">
                <strong>Completed At: </strong>
                <span>{details.completed_at ?? "Not started"}</span>
            </div>
            {details.result && (
                <>
                    <div className="detail-item">
                        <strong>Accuracy: </strong>
                        <span>{details.result.accuracy}</span>
                    </div>
                    <div className="detail-item">
                        <strong>Precision: </strong>
                        <span>{details.result.precision}</span>
                    </div>
                    <div className="detail-item">
                        <strong>Recall: </strong>
                        <span>{details.result.recall}</span>
                    </div>
                    <div className="detail-item">
                        <strong>F1 Score: </strong>
                        <span>{details.result.f1_score}</span>
                    </div>
                </>
            )}
            </div>
        </>
    );

}