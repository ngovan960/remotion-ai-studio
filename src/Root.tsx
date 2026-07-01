import { Composition } from "remotion";
import { MyVideo } from "./Video";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MyVideo"
        component={MyVideo}
        durationInFrames={30 * 300}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          scenes: [],
          audio: "",
          music: "",
          title: "AI Generated Video"
        }}
      />
    </>
  );
};
