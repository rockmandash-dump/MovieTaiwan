import React, { Component } from 'react';
import Placeholder from '../img/placeholder.png';
import { Motion, spring } from 'react-motion';

class MovieCard extends Component {
  render() {
    let { title, year, genre, poster } = this.props;
    // let posterStyle =
    // poster.length > 0 ? { backgroundImage: pathToPosters(poster[0]) } : {};
    let posterStyle =
      poster.length > 0
        ? {
            backgroundImage:
              'url(' + require('../img/poster/' + poster[0]) + ')'
          }
        : {
            backgroundImage: 'url(' + Placeholder + ')'
          };
    // let posterStyle = {
    //   backgroundImage:
    //     'url(https://images.unsplash.com/photo-1491857902420-1c6ea059b1a0?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&s=2d142700c2a5f6b404adf5c619de94e2)'
    // };

    return (
      <div className="moviecard">
        <div className="poster" style={posterStyle}>
          <p className="year">{year}</p>
        </div>
        <h1 className="title">{title}</h1>
        <p className="genre">{genre}</p>
      </div>
    );
  }
}

export default MovieCard;
