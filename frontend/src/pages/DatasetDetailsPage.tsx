import { useParams } from "react-router-dom";
import { useDataset } from "../hooks/useDataset";
import DatasetDetails from "../components/datasets/DatasetDetails";

export default function DatasetDetailsPage() {

    const { id } = useParams();

    const {
        dataset,
        loading,
        error
    } = useDataset(id!);


    if (loading) {
        return <p>Loading dataset...</p>;
    }


    if (error) {
        return <p>{error}</p>;
    }


    if (!dataset) {
        return <p>Dataset not found.</p>;
    }


    return (
        <>
            <h1>Dataset Details</h1>

            <DatasetDetails
                dataset={dataset}
            />
        </>
    );
}