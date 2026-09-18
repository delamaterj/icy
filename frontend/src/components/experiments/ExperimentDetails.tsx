import type { ExperimentDetails as ExperimentDetailsType } from "../../types/experiment";
import { Link } from "react-router-dom";

interface Props {
    experiment: ExperimentDetailsType;
}

export default function ExperimentDetails({experiment}: Props) {

    return (
        <>
            <h2>{experiment.name}</h2>

            <div className="details-grid">

            <div className="detail-item">
                <Link to={`/datasets/${experiment.dataset_id}`}>Dataset</Link>
            </div>

            <div className="detail-item">
                <strong>Status: </strong> 
                <span>{experiment.status}</span>
            </div>

            <div className="detail-item">
                <strong>Description: </strong>
                <span>
                {
                    experiment.description ??
                    "No description provided."
                }
                </span>
            </div>

            <div className="detail-item">
                <strong>Created: </strong>
                <span>{experiment.created_at}</span>
            </div>

            <div className="detail-item">
                <strong>Target Column: </strong>
                <span>{experiment.target_column}</span>
            </div>

            <div className="detail-item">
                <strong>Training Runs: </strong>
                <span><Link to={`/experiments/${experiment.id}/runs`}>Training Runs</Link></span>
            </div>

            </div>
        </>
    );

}