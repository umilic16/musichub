import { FunctionComponent } from "react";
import Functionality from "./Functionality";
import styles from "./Functionalities.module.css";

const Functionalities: FunctionComponent = () => {
  return (
    <div className={styles.functionalities}>
      <Functionality
        title="Contextual awareness"
        description="Remembers what user said earlier in the conversation."
        icon="/conversation.png"
      />
      <Functionality
        title="Music knowledge"
        description="Provides accurate and informative responses to any music-related question."
        icon="/knowledge.png"
      />
      <Functionality
        title="Limited to youtube"
        description="Currently limited to playing music only from YouTube."
        icon="/youtube.png"
      />
    </div>
  );
};

export default Functionalities;
