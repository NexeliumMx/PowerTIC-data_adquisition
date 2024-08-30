import './Tile.scss'; // Create this file for styles

const Tile = ({ title, icon: Icon, content, width }) => {
  return (
    <div className="tile-container" style={{ width: width }}>
      <div className="tile-header">
        {Icon && <Icon className="tile-icon" />}
        <h3 className="tile-title">{title}</h3>
      </div>
      <div className="tile-content">
        {content}
      </div>
    </div>
  );
}

export default Tile;