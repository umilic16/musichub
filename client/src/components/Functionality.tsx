import { FunctionComponent } from "react";
import styles from "./Functionality.module.css";

type FunctionalityType = {
  title?: string;
  description?: string;
  icon?: string;
};

const Functionality: FunctionComponent<FunctionalityType> = ({
  title,
  description,
  icon
}) => {
  return (
    <div className={styles.functionality}>
      <div className={styles.iconContainer}>
        <img
          className={styles.icon}
          alt=""
          src={icon}
        />
      </div>
      <div className={styles.content}>
        <div className={styles.title}>{title}</div>
        <div className={styles.description}>{description}</div>
      </div>
    </div>
  );
};

export default Functionality;
