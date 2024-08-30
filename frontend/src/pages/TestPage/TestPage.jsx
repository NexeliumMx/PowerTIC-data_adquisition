import React from 'react';
import LoremIpsum from '../../components/LoremIpsum/LoremIpsum.jsx';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import './TestPage.scss';

function Footer() {
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

function TestPage() {
  return (
    <> 
      <div className='page-container'>
        <Sidebar />

        <div className='page-content'>
          <div className='lorem-container'>
            <LoremIpsum />
          </div>

          <div className='text-container'>
            <h1>Title H1</h1>
            <h2>Title h2</h2>
            <h3>Title h3</h3>
            <h4>Title h4</h4>
            <h5>Title h5</h5>
            <h6>Title h6</h6>
            <p>Paragraph</p>
          </div>

          <div className='buttons-container' style={{ marginTop: '20px', display: 'flex', gap: '10px' }}>
            <button className="button-color1">Button 1</button>
            <button className="button-color2">Button 2</button>
            <button className="button-color3">Button 3</button>
            <button className="button-color4">Button 4</button>
            <button className="button-color5">Button 5</button>
            <button className="button-color6">Button 6</button>
          </div>

          <div className='lorem-container'>
            <LoremIpsum />
          </div>
          
        </div>
      </div>
    </>
  );
}

export default TestPage;
