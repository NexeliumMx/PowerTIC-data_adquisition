import './Tile.scss'; // Create this file for styles

const Tile = ({ title, icon: Icon, content1,content2, width }) => {
  return (
    <div className="tile-container" style={{ width: width }}>
      <div className="tile-header">
        {Icon && <Icon className="tile-icon" />}
        <h3 className="tile-title">{title}</h3>
      </div>
      <div className="tile-content">
        {content1}
      </div>
      <div className="tile-content">
        {content2}
      </div>
      
    </div>
  );
}

export default Tile;