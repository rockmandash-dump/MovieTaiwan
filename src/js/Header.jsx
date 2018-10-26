import React, { Component } from 'react';
import Logo from '../img/logo.png';

class Header extends Component {
  render() {
    return (
      <div className="header">
        <div className="centerbox">
          <img className="logo" src={Logo} alt="logo" />
          <input
            onChange={this.props.onSearchTermChange}
            value={this.props.searchTerm}
            className="searchbar"
            type="text"
            placeholder="輸入您要搜尋的電影..."
          />
        </div>
      </div>
    );
  }
}

export default Header;
