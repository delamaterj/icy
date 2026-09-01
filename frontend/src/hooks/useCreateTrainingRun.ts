import { useState } from "react";

import { createTrainingRun } from "../api/trainingrunApi";

import type {
    CreateTrainingRunRequest,
    CreateTrainingRunResponse
} from "../types/training_runs";


export function useCreateTrainingRun() {

    const [trainingRun, setTrainingRun] = useState<CreateTrainingRunResponse>();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    async function submitTrainingRun(experiment_id: string, data: CreateTrainingRunRequest) {

        try {

            setLoading(true);
            setError(null);

            const response : CreateTrainingRunResponse = await createTrainingRun(experiment_id, data);
            setTrainingRun(response);

            return response;

        } catch (err) {

            setError("Unable to create training run.");
            throw err;

        } finally {

            setLoading(false);

        }
    }

    return {
        trainingRun,
        loading,
        error,
        createTrainingRun: submitTrainingRun
    };
}