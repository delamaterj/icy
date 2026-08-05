import { useNavigate } from "react-router-dom";
import ExperimentForm from "../components/experiments/ExperimentForm";
import { useCreateExperiment } from "../hooks/useCreateExperiment";
import type { CreateExperimentRequest } from "../types/experiment";

export default function CreateExperimentPage() {

    const {
        createExperiment,
        loading,
        error
    } = useCreateExperiment();

    async function handleCreate(data: CreateExperimentRequest) {

        try {
            const response = await createExperiment(data);
            console.log(response);
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
                onSubmit={handleCreate}
                loading={loading}
            />
        </>
    );
}