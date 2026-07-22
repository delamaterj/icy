import {
    BrowserRouter,
    Routes,
    Route,
    Navigate
} from "react-router-dom";

import HealthPage from "../pages/HealthPage";
import DatasetsPage from "../pages/DatasetPage";

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
                    path="/datasets"
                    element={<DatasetsPage />}
                />

            </Routes>
        </BrowserRouter>
    );
}