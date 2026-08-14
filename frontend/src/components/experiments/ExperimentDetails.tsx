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
                Target Column:
                {" "}
                {experiment.target_column}
            </p>
            <p>
                Test Size:
                {" "}
                {experiment.test_size}
            </p>
            <p>
                Random Seed:
                {" "}
                {experiment.random_seed}
            </p>
        </div>
    );

}