import './Footer.scss';

export default function Footer() {
  return (
    <footer className="footer-container">
      <div className="footer-content">
        <div className="footer-section">
          <h4>STACK OVERFLOW</h4>
          <ul>
            <li><a href="#">Questions</a></li>
            <li><a href="#">Help</a></li>
            <li><a href="#">Chat</a></li>
          </ul>
        </div>
        <div className="footer-section">
          <h4>PRODUCTS</h4>
          <ul>
            <li><a href="#">Teams</a></li>
            <li><a href="#">Advertising</a></li>
            <li><a href="#">Talent</a></li>
          </ul>
        </div>
        <div className="footer-section">
          <h4>COMPANY</h4>
          <ul>
            <li><a href="#">About</a></li>
            <li><a href="#">Press</a></li>
            <li><a href="#">Work Here</a></li>
            <li><a href="#">Legal</a></li>
            <li><a href="#">Privacy Policy</a></li>
            <li><a href="#">Terms of Service</a></li>
            <li><a href="#">Contact Us</a></li>
          </ul>
        </div>
        <div className="footer-section">
          <h4>STACK EXCHANGE NETWORK</h4>
          <ul>
            <li><a href="#">Technology</a></li>
            <li><a href="#">Culture & recreation</a></li>
            <li><a href="#">Life & arts</a></li>
            <li><a href="#">Science</a></li>
            <li><a href="#">Professional</a></li>
            <li><a href="#">Business</a></li>
          </ul>
        </div>
      </div>
      <div className="footer-bottom">
        <div className="footer-social">
          <a href="#">Blog</a>
          <a href="#">Facebook</a>
          <a href="#">Twitter</a>
          <a href="#">LinkedIn</a>
          <a href="#">Instagram</a>
        </div>
        <p>© 2024 Stack Exchange Inc; user contributions licensed under <a href="#">CC BY-SA</a>. rev 2024.8.28.14580</p>
      </div>
    </footer>
  );
}