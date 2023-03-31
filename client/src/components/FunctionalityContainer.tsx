import { FunctionComponent } from "react";
import styles from "./FunctionalityContainer.module.css";

type FunctionalityContainerType = {
  title?: string;
  description?: string;
  icon?: string;
};

const FunctionalityContainer: FunctionComponent<FunctionalityContainerType> = ({
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

export default FunctionalityContainer;
