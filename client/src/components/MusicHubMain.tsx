import { FunctionComponent, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Functionalities from "./Functionalities";
import styles from "./MusicHubMain.module.css";

const MusicHubMain: FunctionComponent = () => {
  const navigate = useNavigate();

  const onButtonClick = useCallback(() => {
    navigate("/chat");
  }, [navigate]);

  return (
    <div className={styles.main}>
      <div className={styles.content}>
        <div className={styles.headingGroup}>
          <div className={styles.title}>
            Welcome to
            <div className={styles.musichubContainer}>
              <div className={styles.lineGradient} />
              MusicHub
            </div>
          </div>
          <div className={styles.baseline}>
            Discover and enjoy music like never before with your personal AI music
            assistant.
          </div>
        </div>
        <div className={styles.buttonContainer}>
          <div
            className={styles.button}
            onClick={onButtonClick}
          >
            Try now!
          </div>
        </div>
      </div>
      <Functionalities />
    </div>
  );
};

export default MusicHubMain;
