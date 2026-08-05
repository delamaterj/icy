import {
    BrowserRouter,
    Routes,
    Route,
    Navigate
} from "react-router-dom";

import HealthPage from "../pages/HealthPage";
import DatasetsPage from "../pages/DatasetPage";
import DatasetDetailsPage from "../pages/DatasetDetailsPage";
import UploadDatasetPage from "../pages/UploadDatasetPage";
import ExperimentsPage from "../pages/ExperimentPage";

export default function AppRouter() {
    return (
        <BrowserRouter>
            <Routes>

                <Route
                    path="/"
                    element={<Navigate to="/health" replace />}
                />

                <Route
                    path="/health"
                    element={<HealthPage />}
                />

                <Route
                    path="/datasets/upload"
                    element={<UploadDatasetPage />}
                />

                <Route
                    path="/datasets"
                    element={<DatasetsPage />}
                />

                <Route
                    path="/datasets/:id"
                    element={<DatasetDetailsPage />}
                />

                <Route
                    path="/experiments"
                    element={<ExperimentsPage />}
                />

            </Routes>
        </BrowserRouter>
    );
}