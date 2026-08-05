import type {ExperimentSummary, 
ExperimentDetails,
CreateExperimentRequest} from "../types/experiment.ts";
import { apiFetch } from "../api/client.ts";

export function getExperiments() {

    return apiFetch<ExperimentSummary[]>(
        "/experiments"
    );
}

export function getExperimentById(id: string) {

    return apiFetch<ExperimentDetails>(
        `/experiments/${id}`
    );
}

export function createExperiment(data: CreateExperimentRequest) {
   
    return apiFetch(
    "/experiments/upload", {
        method: "POST",
        body: JSON.stringify(data)
    });
}