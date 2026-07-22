import DatasetTable from "../components/datasets/DatasetTable";

import { useDatasets } from "../hooks/useDatasets";

export default function DatasetsPage() {

    const {
        datasets,
        loading,
        error
    } = useDatasets();

    if (loading) {
        return <p>Loading datasets...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <>
            <h1>Datasets</h1>
            <DatasetTable
                datasets={datasets}
            />
        </>
    );
}