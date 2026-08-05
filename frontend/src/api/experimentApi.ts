import type {ExperimentSummary, 
ExperimentDetails,
CreateExperimentRequest} from "../types/experiment.ts";
import { apiFetch } from "../api/client.ts";

export function getExperiments() {

    return apiFetch<ExperimentSummary[]>(
        "/experiments", {
        method: "GET"
    });
}

export function getExperimentById(id: string) {

    return apiFetch<ExperimentDetails>(
        `/experiments/${id}`, {
    });
}

export function createExperiment(data: CreateExperimentRequest) {

    return apiFetch<ExperimentSummary>(
        "/experiments",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
}