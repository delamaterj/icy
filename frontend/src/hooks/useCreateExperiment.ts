import { useState } from "react";

import { createExperiment } from "../api/experimentApi";

import type {
    CreateExperimentRequest,
    ExperimentSummary
} from "../types/experiment";


export function useCreateExperiment() {

    const [experiment, setExperiment] = useState<ExperimentSummary>();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    async function submitExperiment(data: CreateExperimentRequest) {

        try {

            setLoading(true);
            setError(null);

            const response : ExperimentSummary = await createExperiment(data);
            setExperiment(response);

            return response;

        } catch (err) {

            setError("Unable to create experiment.");
            throw err;

        } finally {

            setLoading(false);

        }
    }

    return {
        experiment,
        loading,
        error,
        createExperiment: submitExperiment
    };
}