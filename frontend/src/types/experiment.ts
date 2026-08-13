export type ExperimentModel = 
| "LOGISTIC_REGRESSION" 
| "DECISION_TREE" 
| "RANDOM_FOREST";

export interface ExperimentSummary {
    id: string;
    dataset_id: string;
    name: string;
    status: string;
    model: string;
    created_at: string;
}

export interface ExperimentDetails extends ExperimentSummary {
    description: string | null;
    target_column: string;
    test_size: number;
    random_seed: number;
}

export interface CreateExperimentRequest {
    dataset_id: string;
    name: string;
    description?: string;
    model: ExperimentModel;
    target_column: string;
    test_size?: number;
    random_seed?: number;
}
