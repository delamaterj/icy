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
    status: string;
    created_at: string;
    target_column: string;
    test_size: Float32Array;
    random_seed: BigInteger;
}

export interface CreateExperimentRequest {
    dataset_id: string;
    name: string;
    description?: string;
}