import React, { useState, useEffect } from "react";
import ChatList from './components/ChatList';
import MessageArray from "./components/MessageArray";
import './App.css';

const App = () => {
  const [chat, setChat] = useState("");
  const [messages, setMessages] = useState([])

  const addMessage = () => {
    setMessages([...messages, chat]);
    setChat("");
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    if (e.key === "Enter" && chat !== "") {
      addMessage();
    }
  }

  useEffect(() => { 
    console.log(messages);
    }, 
    [messages]);

  return (
    <div className="App">
      <div className="outer-wrapper">
        <div className="left-right-outer-wrapper">
          <div className="left-wrapper">
            <div className="left-outer-icons">
              <div className="material-icons icon top">person</div>
              <div className="material-icons icon selected">textsms</div>
              <div className="material-icons icon">person_add</div>
              <div className="material-icons icon">watch_later</div>
              <div className="material-icons icon">article</div>
              <div className="material-icons icon">favorite_border</div>
            </div>
          </div>
          <div className="right-outer-main">
            <div className="upper-main">
              <div className="upper-tabs tabs-selected">
                All  
              </div>
              <div className="upper-tabs">  
                Friends
              </div>
              <div className="upper-tabs">
                Groups 
              </div>
              <div className="upper-tabs">
                Official accounts
              </div>
              <div className="upper-tabs">
                OpenChats  
              </div>
            </div>
            <div className="central-main">
              <div className="left-chat">
                <div className="search-container">
                  <div className="search-bar">
                    Search for chats and messages
                  </div>
                </div>
                <div className="chat-list">
                  <ChatList />
                </div>
              </div>
              <div className="right-chat">
                <div className="title-chat">
                  <div className="left-title-chat">
                    <p className="yeetbot-name">yeetBot</p>
                    <div className="material-icons icon-smaller">volume_down</div>
                    <div className="material-icons icon-smaller">open_in_new</div>
                  </div>
                  <div className="right-title-chat">
                    <div className="material-icons icon-small">search</div>
                    <div className="material-icons icon-small">call</div>
                    <div className="material-icons icon-small">more_vert</div>
                  </div>
                </div>
                <div className="message-array">
                  <MessageArray messages={messages} />
                </div>
                <input 
                  className="chat-input"
                  type="text" 
                  value={chat} 
                  onKeyUp={handleSubmit} 
                  placeholder="Enter a message"
                  onChange={e => setChat(e.target.value)} />
                <div className="bottom-icons">
                  <div className="bottom-left">
                    <div className="material-icons bottom-icon-left">attach_file</div>
                    <div className="material-icons bottom-icon-left">bookmark_border</div>
                    <div className="material-icons bottom-icon-left">crop</div>
                  </div>
                  <div className="bottom-right">
                    <div className="material-icons bottom-icon-right">sentiment_satisfied_alt</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
