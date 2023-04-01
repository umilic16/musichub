import { FunctionComponent } from "react";
import MusicHubMain from "../components/MusicHubMain";
import styles from "./Home.module.css";

const Home: FunctionComponent = () => {
  return (
    <div className={styles.content}>
      <div className={styles.gradientContainer}>
        <div className={styles.gradient}>
        </div>
      </div>
      <MusicHubMain />
    </div>
  );
};

export default Home;
