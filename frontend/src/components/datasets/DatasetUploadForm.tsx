import { useState } from "react";
import { useUploadDataset } from "../../hooks/useUploadDataset";
import UploadResult from "./UploadResult";


export default function DatasetUploadForm() {

    const [file, setFile] =
        useState<File | null>(null);


    const {
        upload,
        loading,
        result,
        error
    } = useUploadDataset();


    function handleFileChange(
        event: React.ChangeEvent<HTMLInputElement>
    ) {

        const selectedFile =
            event.target.files?.[0];

        if (selectedFile) {
            setFile(selectedFile);
        }
    }


    async function handleUpload() {

        if (!file) {
            return;
        }

        await upload(file);
    }


    return (
        <>
            <input
                type="file"
                onChange={handleFileChange}
            />

            <button
                onClick={handleUpload}
                disabled={!file || loading}
            >
                {
                    loading
                        ? "Uploading..."
                        : "Upload"
                }
            </button>
            <UploadResult
                result={result}
                error={error}
            />
        </>
    );
}