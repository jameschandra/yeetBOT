import React from 'react';
import MessageNative from './MessageNative';
import MessageResponse from './MessageResponse';

const MessageArray = ({ messages }) => {
    return (
        <div>
            { messages.map((message, index) => {
                if (index % 2 === 0) {
                    return <MessageNative message={message} key={index.toString()} />
                } else {
                    return <MessageResponse message={message} key={index.toString()} />
                }
            }) }
        </div>
    );
}

export default MessageArray;