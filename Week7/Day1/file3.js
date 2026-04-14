import React from 'react';
import './Exercise.css';

class Exercise extends React.Component {

  render() {

    const style_header = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "10px",
      fontFamily: "Arial"
    };

    return (
      <div>

        <h1 style={style_header}>This is a Header</h1>

        <p className="para">This is a Paragraph</p>

        <a href="#">This is a Link</a>

        <h3>This is a Form:</h3>
        <form>
          <input placeholder="Enter your name" />
          <button>Submit</button>
        </form>

        <h3>Here is an image:</h3>
        <img 
          src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg"
          width="200"
          alt="react"
        />

        <h3>This is a list:</h3>
        <ul>
          <li>Coffee</li>
          <li>Tea</li>
          <li>Milk</li>
        </ul>

      </div>
    );
  }
}

export default Exercise;
