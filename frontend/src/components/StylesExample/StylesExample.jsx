export default function StylesExample() {
  return (
    <>
      <div
        className="text-container"
        style={{ 
          backgroundColor: 'blue', 
          margin: '0',
          padding: '0',
        }}
      >
        <h1>Title H1</h1>
        <h2>Title h2</h2>
        <h3>Title h3</h3>
        <h4>Title h4</h4>
        <h5>Title h5</h5>
        <h6>Title h6</h6>
        <p>Paragraph</p>
      </div>
      
      <div
        className="buttons-container"
        style={{
          margin: '0',
          padding: '0',
          display: 'flex',
          justifyContent: 'center',
          backgroundColor: 'green',
        }}
      >
        <button className="button-color1">Button 1</button>
        <button className="button-color2">Button 2</button>
        <button className="button-color3">Button 3</button>
        <button className="button-color4">Button 4</button>
        <button className="button-color5">Button 5</button>
        <button className="button-color6">Button 6</button>
      </div>
    </>
  );
}