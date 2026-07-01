import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  Sequence,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
  staticFile
} from "remotion";

interface Scene {
  id: number;
  image: string;
  duration: number;
  text?: string;
}

interface VideoProps {
  scenes: Scene[];
  audio: string;
  music: string;
  title: string;
}

export const MyVideo: React.FC<VideoProps> = ({
  scenes,
  audio,
  music,
  title
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  let currentFrame = 0;
  
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      {/* Background Music */}
      {music && <Audio src={staticFile(music)} volume={0.3} />}
      
      {/* Voice Over */}
      {audio && <Audio src={staticFile(audio)} volume={1} />}
      
      {/* Scenes */}
      {scenes.map((scene, index) => {
        const startFrame = currentFrame;
        const durationFrames = scene.duration * fps;
        currentFrame += durationFrames;
        
        return (
          <Sequence key={index} from={startFrame} durationInFrames={durationFrames}>
            <SceneComponent scene={scene} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

const SceneComponent: React.FC<{ scene: Scene }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  
  // Ken Burns effect
  const scale = interpolate(frame, [0, durationInFrames], [1, 1.1], {
    extrapolateRight: "clamp"
  });
  
  // Fade in/out
  const fadeIn = interpolate(frame, [0, 10], [0, 1], {
    extrapolateRight: "clamp"
  });
  const fadeOut = interpolate(frame, [durationInFrames - 10, durationInFrames], [1, 0], {
    extrapolateLeft: "clamp"
  });
  const opacity = Math.min(fadeIn, fadeOut);
  
  return (
    <AbsoluteFill style={{ opacity }}>
      {scene.image && (
        <Img
          src={staticFile(scene.image)}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            transform: `scale(${scale})`
          }}
        />
      )}
      
      {scene.text && (
        <AbsoluteFill style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "flex-end",
          paddingBottom: "10%"
        }}>
          <div style={{
            color: "white",
            fontSize: 48,
            fontWeight: "bold",
            textShadow: "2px 2px 8px rgba(0,0,0,0.8)",
            textAlign: "center",
            maxWidth: "80%"
          }}>
            {scene.text}
          </div>
        </AbsoluteFill>
      )}
    </AbsoluteFill>
  );
};
