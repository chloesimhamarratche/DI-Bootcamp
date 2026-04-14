import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from "react-responsive-carousel";

function App() {
  return (
    <div>
      <Carousel>

        <div>
          <img src="https://upload.wikimedia.org/wikipedia/commons/6/6e/Hong_Kong_Skyline.jpg" />
          <p className="legend">Hong Kong</p>
        </div>

        <div>
          <img src="https://upload.wikimedia.org/wikipedia/commons/0/0e/Ruins_of_St._Paul%2C_Macau.jpg" />
          <p className="legend">Macao</p>
        </div>

        <div>
          <img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Tokyo_Tower_and_around_Skyscrapers.jpg" />
          <p className="legend">Japan</p>
        </div>

        <div>
          <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/Las_Vegas_Strip_at_night.jpg" />
          <p className="legend">Las Vegas</p>
        </div>

      </Carousel>
    </div>
  );
}

export default App;
