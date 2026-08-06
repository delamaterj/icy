import type { ExperimentDetails as ExperimentDetailsType } from "../../types/experiment";
import { Link } from "react-router-dom";

interface Props {
    experiment: ExperimentDetailsType;
}

export default function ExperimentDetails({experiment}: Props) {

    return (
        <div>
            <h2>
                {experiment.name}
            </h2>
            <p>
                <Link to={`/datasets/${experiment.dataset_id}`}>Dataset</Link>
            </p>
            <p>
                Status: {experiment.status}
            </p>
            <p>
                Description:
                {" "}
                {
                    experiment.description ??
                    "No description provided."
                }
            </p>
            <p>
                Created:
                {" "}
                {experiment.created_at}
            </p>
            <p>
                Started:
                {" "}
                {
                    experiment.started_at ??
                    "Not started"
                }
            </p>
            <p>
                Completed:
                {" "}
                {
                    experiment.completed_at ??
                    "Not completed"
                }
            </p>
        </div>
    );

}