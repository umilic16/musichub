import { FunctionComponent, useCallback, useState } from "react";
import Message from "../components/Message";
import React from 'react';
import styles from "./Chat.module.css";

type MessageType = {
  user: string;
  text: string;
};

const Chat: FunctionComponent = () => {
  const [messages, setMessages] = useState<MessageType[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isRequestPending, setIsRequestPending] = useState(false);

  const handleSendMessage = () => {
    if (inputValue.trim() !== '' && !isRequestPending) { // check if a request is not already pending
      const newMessage: MessageType = {
        user: 'user',
        text: inputValue,
      };
  
      setMessages((prevMessages) => [...prevMessages, newMessage]);
      setIsRequestPending(true); // mark a new request as pending

      fetch('http://127.0.0.1:5000', {
        method: 'POST',
        body: JSON.stringify({ message: inputValue }),
        headers: { 'Content-Type': 'application/json' },
      })
      .then((response) => response.json())
      .then((data) => {
        const newResponse: MessageType = {
          user: 'assistant',
          text: data.response.data,
        };
        setMessages((prevMessages) => [...prevMessages, newResponse]);
        setIsRequestPending(false); // mark the request as completed
      })
      .catch((error) => {
        console.error('Error:', error);
        setIsRequestPending(false); // mark the request as completed (even in case of an error)
      });
      
      setInputValue('');
    }
  };
  
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleInputKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  return (
    <div className={styles.content}>
      <div className={styles.gradientContainer}>
        <div className={styles.gradient}></div>
      </div>
      <div className={styles.chat}>
        <div className={styles.chatBox}>
          {messages.map((message, index) => (
            <Message key={index} user={message.user} text={message.text} />
          ))}
          {isRequestPending && <Message user="assistant" text="..." />}
        </div>
        <div className={styles.bottomContainer}>
          <div className={styles.searchBar}>
            <input
              className={styles.input}
              placeholder="Example : What do you know about Mozart?"
              type="text"
              value={inputValue}
              onChange={handleInputChange}
              onKeyDown={handleInputKeyPress}
            />
            <button className={styles.button} onClick={handleSendMessage}>
              <img className={styles.icon} alt="" src="/send.png" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Chat;
