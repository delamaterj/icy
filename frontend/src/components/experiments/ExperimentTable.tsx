import type { ExperimentSummary } from "../../types/experiment";
import { Link } from "react-router-dom";

interface Props {
    experiments: ExperimentSummary[];
}

export default function ExperimentTable({experiments}: Props) {

    return (

        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Dataset ID</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {
                    experiments.map((experiment) => (
                        <tr key={experiment.id}>
                            <td>
                                <Link to={`/experiments/${experiment.id}`}>
                                    {experiment.name}
                                </Link>
                            </td>
                            <td>
                                {experiment.dataset_id}
                            </td>
                            <td>
                                {experiment.status}
                            </td>
                        </tr>
                    ))
                }
            </tbody>
        </table>
    );
}