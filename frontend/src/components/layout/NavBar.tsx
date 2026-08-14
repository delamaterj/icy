import { Link } from "react-router-dom";

export default function NavBar() {

    return (
        <>
            <nav>
                <ul>
                    <li><Link to="/datasets">Datasets</Link></li>
                    <li><Link to="/experiments">Experiments</Link></li>
                    <li><Link to="/datasets/upload">Upload Dataset</Link></li>
                </ul>
            </nav>
        </>
    );

}