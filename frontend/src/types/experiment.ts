export interface ExperimentSummary {
    id: string;
    dataset_id: string;
    name: string;
    status: string;
}

export interface ExperimentDetails extends ExperimentSummary {
    description: string | null;
    status: string;
    created_at: string;
    started_at: string | null;
    completed_at: string | null;
}

export interface CreateExperimentRequest {
    dataset_id: string;
    name: string;
    description?: string;
}