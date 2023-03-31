import { FunctionComponent } from "react";
import FunctionalityContainer from "./FunctionalityContainer";
import styles from "./FunctionalitiesContainer.module.css";

const FunctionalitiesContainer: FunctionComponent = () => {
  return (
    <div className={styles.functionalities}>
      <FunctionalityContainer
        title="Contextual awareness"
        description="Remembers what user said earlier in the conversation."
        icon="/conversation.png"
      />
      <FunctionalityContainer
        title="Music knowledge"
        description="Provides accurate and informative responses to any music-related question."
        icon="/knowledge.png"
      />
      <FunctionalityContainer
        title="Limited to youtube"
        description="Currently limited to playing music only from YouTube."
        icon="/youtube.png"
      />
    </div>
  );
};

export default FunctionalitiesContainer;
