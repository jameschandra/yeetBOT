import React from 'react';
import image from '../images/profile-round.png';
import '../styles/chatlist.css';

const ChatList = () => {
    return (
        <div className="chatlist">
            <div className="chatlist-outter">
                <div className="image-div">
                    <img src={image} className="chatlist-picture" alt="profile" />
                </div>
                <div className="right-div">
                    <div className="top-div">
                        <div className="name">
                            Yeet Yeetus
                        </div>
                        <div className="time">
                            9:30 PM
                        </div>
                    </div>
                    <div className="chat-description">
                        How's the yeet my dude
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ChatList;