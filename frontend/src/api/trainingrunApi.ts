import type {TrainingRunSummary, 
TrainingRunDetails,
TrainingRunResponse,
CreateTrainingRunRequest} from "../types/training_runs.ts";
import { apiFetch } from "../api/client.ts";

export function getTrainingRuns(experiment_id: string) {

    return apiFetch<TrainingRunSummary[]>(
        `/experiments/${experiment_id}/runs`, {
        method: "GET"
    });
}

export function getTrainingRunResults(experiment_id: string, training_run_id: string) {

    return apiFetch<TrainingRunDetails>(
        `/experiments/${experiment_id}/runs/${training_run_id}`, {
        method: "GET"
    });
}

export function createTrainingRun(experiment_id: string, data: CreateTrainingRunRequest) {

    return apiFetch<TrainingRunResponse>(
        `/experiments/${experiment_id}/runs`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
}

export const runTrainingRun = (trainingRunId: string) => {
    return apiFetch<TrainingRunResponse>(
        `/training-runs/${trainingRunId}/run`, {
        method: "POST"
    });
}