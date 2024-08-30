import { Contrast, Bell, Settings, User } from 'lucide-react';
import './Navbar.scss'; // Import the Navbar-specific styles

const Navbar = ({ title }) => {
  return (
    <div className="navbar-container">
      <div className="navbar-title">
        {title}
      </div>
      <div className="navbar-icons">
        <Contrast className="navbar-icon" />
        <Bell className="navbar-icon" />
        <Settings className="navbar-icon" />
        <User className="navbar-icon" />
      </div>
    </div>
  );
};

export default Navbar;