import React, { Component } from 'react';
import MovieCard from './MovieCard.jsx';
import Header from './Header.jsx';
import movieData from './movieData.json';

import style from '../scss/style.scss';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchTerm: ''
    };

    this.handleSearchTermChange = this.handleSearchTermChange.bind(this);
  }

  handleSearchTermChange(event) {
    this.setState({ searchTerm: event.target.value });
  }

  render() {
    return (
      <div id="MovieTaiwanApp">
        <Header
          searchTerm={this.state.searchTerm}
          onSearchTermChange={this.handleSearchTermChange}
        />
        <div className="moviecard-container">
          <div className="centerbox">
            {movieData.movies
              .filter(movie => movie.title.indexOf(this.state.searchTerm) >= 0)
              .map(movie => (
                <MovieCard
                  title={movie.title}
                  genre={movie.genre}
                  year={movie.year}
                  poster={movie.poster}
                  key={`${movie.title} ${movie.titleEn}`}
                />
              ))}
          </div>
        </div>
      </div>
    );
  }
}

export default App;
