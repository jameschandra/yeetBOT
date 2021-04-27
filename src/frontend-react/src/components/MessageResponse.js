import React from 'react';
import '../styles/messageresponse.css';

const MessageResponse = ({ message }) => {
    return (
        <div className="response-box">
            <p className="response-message">{message}</p>
        </div>
    )
}

export default MessageResponse;