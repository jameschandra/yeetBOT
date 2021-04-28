import React from 'react';
import image from '../images/profile-robot.gif';
import '../styles/yeetbotchatlist.css';

const ChatList = () => {
    return (
        <div className="chatlist-yeetbot">
            <div className="chatlist-outter">
                <div className="image-div">
                    <img src={image} className="chatlist-picture" alt="profile" />
                </div>
                <div className="right-div">
                    <div className="top-div">
                        <div className="name">
                            yeetBOT
                        </div>
                        <div className="time">
                            9:35 PM
                        </div>
                    </div>
                    <div className="chat-description">
                        Yeetest Bot that has ever Yeet
                    </div>
                </div>
            </div>
        </div>
    )
}

export default ChatList;