export type TrainingRunStatus = 
    "CREATED"
    "RUNNING"
    "COMPLETED"
    "FAILED";

export interface Results {
    accuracy: number;
    precision: number;
    recall: number;
    f1_score: number;
    confusion_matrix: number[][]
}

export interface TrainingRunSummary {
    id: string;
    experiment_id: string;
    status: string;
    created_at: string;
    started_at: string;
    completed_at: string;
    random_seed: number;
    test_size: number;
}

export interface TrainingRunDetails extends TrainingRunSummary {
    result: Results;
}

export interface CreateTrainingRunRequest {
    test_size: number;
    random_seed: number;
}

export interface CreateTrainingRunResponse {
    id: string;
    experiment_id: string;
    status: TrainingRunStatus;
    created_at: string;
}