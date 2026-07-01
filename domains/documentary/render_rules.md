# Documentary Render Rules

## Rendering Philosophy
Documentary rendering should prioritize clarity, consistency, and professionalism. The output should feel polished but not over-produced, maintaining authenticity while ensuring technical quality.

## Technical Specifications

### Resolution
- **Primary**: 1920x1080 (Full HD)
- **Secondary**: 3840x2160 (4K) for high-end projects
- **Aspect Ratio**: 16:9 (widescreen)
- **Frame Rate**: 30 fps (standard), 24 fps (cinematic)

### Codec Settings
- **Codec**: H.264 (compatible), H.265 (efficient)
- **Bitrate**: 8-12 Mbps for 1080p, 20-30 Mbps for 4K
- **Profile**: High
- **Level**: 4.1 or higher

### Audio Settings
- **Sample Rate**: 48 kHz
- **Bit Depth**: 24-bit
- **Channels**: Stereo (2.0)
- **Bitrate**: 320 kbps

## Scene Duration Guidelines

### Standard Scenes
- **Minimum**: 5 seconds
- **Optimal**: 8-15 seconds
- **Maximum**: 20 seconds
- **Average**: 10-12 seconds

### Transition Scenes
- **Duration**: 3-5 seconds
- **Purpose**: Bridge between topics
- **Audio**: Crossfade music

### Montage Scenes
- **Duration**: 15-30 seconds
- **Pacing**: 2-4 seconds per clip
- **Music**: Primary audio element

## Rendering Pipeline

### Step 1: Pre-Render Checks
- [ ] All assets loaded correctly
- [ ] Audio levels balanced
- [ ] Text overlays readable
- [ ] Transitions smooth
- [ ] Color grading consistent

### Step 2: Scene Rendering
- Render each scene individually
- Check for artifacts or glitches
- Verify audio sync
- Confirm timing matches script

### Step 3: Assembly
- Concatenate scenes in order
- Apply global color correction
- Add opening and closing titles
- Insert credits if needed

### Step 4: Final Render
- Export at target resolution
- Apply compression settings
- Generate preview version
- Create backup archive

## Quality Assurance

### Technical Checks
- **Resolution**: Matches specification
- **Frame Rate**: Consistent throughout
- **Audio Sync**: Lip-sync within 1 frame
- **Color**: No banding or artifacts
- **Compression**: No visible blocking

### Creative Checks
- **Pacing**: Matches narration rhythm
- **Transitions**: Smooth and appropriate
- **Text**: Readable at all sizes
- **Audio**: Clear and balanced
- **Overall**: Engaging and professional

### Accessibility
- **Subtitles**: Available and accurate
- **Audio Description**: Consider for visually impaired
- **Color Contrast**: Meets WCAG standards
- **Text Size**: Readable on mobile devices

## Performance Optimization

### Rendering Speed
- **GPU Acceleration**: Enable if available
- **Parallel Processing**: Render scenes simultaneously
- **Proxy Files**: Use lower resolution for preview
- **Caching**: Store rendered frames for reuse

### File Size Management
- **Target**: 500MB-1GB per 10 minutes
- **Compression**: Balance quality and size
- **Segmentation**: Split large projects
- **Archiving**: Compress completed projects

## Export Formats

### Primary Exports
- **Master**: High bitrate, archival quality
- **Web**: Optimized for streaming (YouTube, Vimeo)
- **Mobile**: Lower resolution, smaller file size
- **Preview**: Quick render for review

### Metadata
- **Title**: Clear and descriptive
- **Description**: Summary of content
- **Tags**: Relevant keywords
- **Credits**: All contributors listed
- **License**: Usage rights specified

## Troubleshooting

### Common Issues
- **Audio drift**: Resync audio track
- **Color shift**: Check color profile settings
- **Frame drops**: Reduce complexity or render settings
- **File corruption**: Re-render affected sections
- **Compatibility**: Test on multiple devices

### Quality Recovery
- **Artifacts**: Re-render with higher bitrate
- **Sync issues**: Adjust timing manually
- **Color problems**: Apply color correction
- **Audio issues**: Remix and re-export

## Project Organization

### Directory Structure
```
project/
├── raw/
│   ├── scenes/
│   ├── audio/
│   └── assets/
├── renders/
│   ├── previews/
│   ├── finals/
│   └── archives/
├── project_files/
│   ├── remotion/
│   └── exports/
└── documentation/
    ├── script/
    └── notes/
```

### Naming Convention
```
[project]_[scene]_[version]_[date].[ext]
Example: documentary_scene01_v2_2024-01-15.mp4
```
