import { useState } from "react";
import { runTrainingRun } from "../api/trainingrunApi";

export const useRunTrainingRun = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const run = async (trainingRunId: string) => {
        try {
            setLoading(true);
            setError(null);

            await runTrainingRun(trainingRunId);

            return true;
        } catch (err) {
            setError("Failed to run training run.");
            return false;
        } finally {
            setLoading(false);
        }
    };

    return {
        run,
        loading,
        error,
    };
};