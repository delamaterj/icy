import { useEffect, useState } from "react";
import { getTrainingRuns } from "../api/trainingrunApi";
import type { TrainingRunSummary } from "../types/training_runs";

export function useTrainingRuns(id: string) {

    const [trainingRuns, setTrainingRuns] = useState<TrainingRunSummary[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    async function fetchTrainingRuns(experiment_id: string) {

        try {
            setLoading(true);
            const response = await getTrainingRuns(experiment_id);
            setTrainingRuns(response);
            setError(null);
        } catch (err) {
            setError("Unable to load training runs.");
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        if (!id) return;
        fetchTrainingRuns(id);
    }, [id]);

    return {
        trainingRuns,
        loading,
        error,
        refresh: () => fetchTrainingRuns(id)
    };
}