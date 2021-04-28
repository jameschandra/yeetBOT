import React from 'react';
import '../styles/messageresponse.css';

const MessageResponse = ({ message }) => {
    return (
        <div className="response-box">
            <p className="response-message">
            {message.split("\n").map((i,key) => {
                return <span>{i}{<br />}</span>
            })}</p>
        </div>
    )
}

export default MessageResponse;