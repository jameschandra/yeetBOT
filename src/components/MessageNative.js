import React from 'react';
import '../styles/messagenative.css';

const MessageNative = ({ message }) => {
    return (
        <div className="native-box">
            <p className="native-message">{message}</p>
        </div>
    )
}

export default MessageNative;