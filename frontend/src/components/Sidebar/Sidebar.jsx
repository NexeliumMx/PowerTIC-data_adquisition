import { useContext, createContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { MoreVertical, ChevronLast, ChevronFirst, Home, Settings, Users, Download, LayoutDashboard, UtilityPole, FlaskConical, HousePlug} from "lucide-react"; // Add icons as needed
import "./Sidebar.scss";

const SidebarContext = createContext();

const routes = [
  { text: "Home", to: "/", icon: <Home size={24} /> },
  { text: "Locations", to: "/locations", icon: <HousePlug size={24} /> },
  { text: "Load Center", to: "/load-center", icon: <UtilityPole size={24} /> },
  { text: "Dashboard", to: "/dashboard", icon: <LayoutDashboard size={24} /> },  
  { text: "Downloads", to: "/downloads", icon: <Download size={24} /> },
  { text: "Users", to: "/users", icon: <Users size={24} /> },
  { text: "Settings", to: "/settings", icon: <Settings size={24} /> },
  { text: "Test Page", to: "/testpage", icon: <FlaskConical size={24} /> },
];

function SidebarItem({ icon, text, to, active, alert }) {
  const { expanded } = useContext(SidebarContext);
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(to);  // Navigate to the desired route when the item is clicked
  };

  return (
    <li
      className={`sidebar-item ${active ? "active" : ""} ${expanded ? "expanded" : "collapsed"}`}
      onClick={handleClick} // Attach the handleClick function to the onClick event
    >
      {icon}
      <span className="item-text">{text}</span>
      {alert && <div className="item-alert" />}
      {!expanded && (
        <div className="item-tooltip">
          {text}
        </div>
      )}
    </li>
  );
}


export default function Sidebar() {
  const [expanded, setExpanded] = useState(true);

  return (
    <aside className="sidebar-container">
      <nav className="sidebar-nav">
        <div className="sidebar-header">
          <img
            src="https://img.logoipsum.com/243.svg"
            className={`sidebar-logo ${expanded ? "expanded" : "collapsed"}`}
            alt="Logo"
          />
          <button
            onClick={() => setExpanded((curr) => !curr)}
            className="toggle-button"
          >
            {expanded ? <ChevronFirst /> : <ChevronLast />}
          </button>
        </div>

        <SidebarContext.Provider value={{ expanded }}>
          <ul className="sidebar-items">
            {routes.map((route, index) => (
              <SidebarItem
                key={index}
                icon={route.icon}
                text={route.text}
                to={route.to}
                active={route.to === window.location.pathname}
              />
            ))}
          </ul>
        </SidebarContext.Provider>

        <div className="sidebar-footer">
          <img
            src="https://ui-avatars.com/api/?background=c7d2fe&color=3730a3&bold=true"
            alt="User Avatar"
            className="user-avatar"
          />
          <div className={`user-info ${expanded ? "expanded" : "collapsed"}`}>
            <div className="user-details">
              <h4 className="user-name">John Doe</h4>
              <span className="user-email">johndoe@gmail.com</span>
            </div>
            <MoreVertical size={20} />
          </div>
        </div>
      </nav>
    </aside>
  );
}