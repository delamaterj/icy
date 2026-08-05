import ExperimentTable from "../components/experiments/ExperimentTable";
import { useExperiments } from "../hooks/useExperiments";

export default function ExperimentsPage() {
    const {
        experiments,
        loading,
        error
    } = useExperiments();

    if (loading) {
        return <p>Loading experiments...</p>;
    }

    if (error) {
        return <p>{error}</p>;
    }

    return (
        <>
            <h1>Experiments</h1>
            <ExperimentTable
                experiments={experiments}
            />
        </>
    );
}