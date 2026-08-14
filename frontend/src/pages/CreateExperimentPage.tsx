import { useParams } from "react-router-dom";
import ExperimentForm from "../components/experiments/ExperimentForm";
import { useCreateExperiment } from "../hooks/useCreateExperiment";
import type { CreateExperimentRequest } from "../types/experiment";
import {useNavigate} from 'react-router-dom';

export default function CreateExperimentPage() {

    const { dataset_id } = useParams();
    const navigate = useNavigate();

    const {
        createExperiment,
        loading,
        error
    } = useCreateExperiment();

    async function handleCreate(data: CreateExperimentRequest) {

        try {
            const response = await createExperiment(data);
            console.log(response);
            alert("Experiment successfully created");
            navigate(`/experiments/${response.id}`, { replace: true } );
        }
        catch (err) {
            console.log(err);
        }
    }

    return (
        <>
            <h1>
                Create Experiment
            </h1>
            {
                error &&
                <p>{error}</p>
            }
            <ExperimentForm
                initialDatasetId={dataset_id ?? ""}
                onSubmit={handleCreate}
                loading={loading}
            />
        </>
    );
}