import type { UploadDatasetResponse } from "../../types/dataset";

interface UploadResultProps {
    result: UploadDatasetResponse | null | undefined;
    error: string | null;
}

export default function UploadResult({
    result,
    error
}: UploadResultProps) {

    if (error) {

        return (
            <div>
                <h2>Upload Failed</h2>
                <p>{error}</p>
            </div>
        );

    }

    if (!result) {
        return null;
    }

    if (result.passed) {

        return (
            <div>
                <h2>Dataset Uploaded Successfully</h2>
                <p>Status: {result.status}</p>
                <p>Dataset ID: {result.dataset_id}</p>
            </div>
        );
    }

    return (
        <div>
            <h2>Dataset Uploaded, But Validation Failed</h2>
            <p>Status: {result.status}</p>
            <p>Validation Errors:</p>
            <ul>
                {
                    result.errors.map((error, index) => (
                        <li key={index}>{error}</li>
                    ))
                }
            </ul>
            <p>Dataset ID: {result.dataset_id}</p>
        </div>
    );
}