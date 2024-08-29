import Sidebar from "../../components/Sidebar/Sidebar.jsx";

// Example Elements
import LoremIpsum from "../../components/LoremIpsum/LoremIpsum.jsx";
import StylesExample from "../../components/StylesExample/StylesExample.jsx";

export default function TestPage() {
  return (
    <div className="page-container">
      <Sidebar />

      <div className="page-content">
        <LoremIpsum />
        <StylesExample />
        <LoremIpsum />
      </div>
    </div>
  );
}