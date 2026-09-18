import { Link } from "react-router-dom";

export default function NavBar() {
    
    return (
        <nav className="navbar">
            <div className="navbar-container">
                <Link to="/" className="navbar-brand">
                    ICY
                </Link>

                <ul className="navbar-links">
                    <li>
                        <Link to="/datasets">Datasets</Link>
                    </li>
                    <li>
                        <Link to="/experiments">Experiments</Link>
                    </li>
                    <li>
                        <Link to="/datasets/upload">Upload Dataset</Link>
                    </li>
                </ul>
            </div>
        </nav>
    );
}