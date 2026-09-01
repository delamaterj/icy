import { useEffect, useState } from "react";
import { getTrainingRunResults } from "../api/trainingrunApi";
import type { TrainingRunDetails } from "../types/training_runs";

export function useTrainingRunResults(exp_id: string, tr_id: string) {

    const [trainingRuns, setTrainingRuns] = useState<TrainingRunDetails>();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    async function fetchTrainingRunDetails(experiment_id: string, training_run_id: string) {

        try {
            setLoading(true);
            const response = await getTrainingRunResults(experiment_id, training_run_id);
            setTrainingRuns(response);
            setError(null);
        } catch (err) {
            setError("Unable to load training run results.");
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        if (!exp_id || !tr_id) return;
        fetchTrainingRunDetails(exp_id, tr_id);
    }, [exp_id, tr_id]);

    return {
        trainingRuns,
        loading,
        error,
        refresh: () => fetchTrainingRunDetails(exp_id, tr_id)
    };
}