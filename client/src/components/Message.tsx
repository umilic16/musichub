import { FunctionComponent, useState, useEffect } from "react";
import styles from "./Message.module.css";

type MessageType = {
  user?: string;
  text?: string;
};

const Message: FunctionComponent<MessageType> = ({
  user,
  text,
}) => {
  const [dots, setDots] = useState<string>(".");

  useEffect(() => {
    const interval = setInterval(() => {
      setDots((prevDots) => {
        if (prevDots === "...") {
          return ".";
        } else {
          return prevDots + ".";
        }
      });
    }, 350);

    return () => clearInterval(interval);
  }, []);

  const icon = user == "user" ? "/avatar-user.png" : "/avatar-assistant.png";

  return (
    <div className={styles.container}>
      <div className={styles.message}>
        <div className={styles.avatar}>
          <img className={styles.icon} alt="" src={icon} />
        </div>
        {text === "..." ? (
          <span className={styles.dots}>{dots}</span>
        ) : (
          <div className={styles.text}>{text}</div>
        )}
      </div>
      <div className={styles.line}></div>
    </div>
  );
};

export default Message;
