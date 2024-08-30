import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';

// Example Elements
import LoremIpsum from "../../components/LoremIpsum/LoremIpsum.jsx";
import StylesExample from "../../components/StylesExample/StylesExample.jsx";

export default function TestPage() {
  return (
    <div className="page-container">
      <Sidebar />

      <div className="page-content">
        <Navbar title="Test Page Template" />
        <LoremIpsum />
        <StylesExample />
        <LoremIpsum />
      </div>
    </div>
  );
}