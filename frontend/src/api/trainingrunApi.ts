import type {TrainingRunSummary, 
TrainingRunDetails} from "../types/training_runs.ts";
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