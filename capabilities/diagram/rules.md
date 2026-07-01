# Diagram Rules

## Diagram Types

| Type | Use Case | Layout |
|------|----------|--------|
| **Flowchart** | Process/workflow | Top-down or left-right |
| **Hierarchy** | Org charts, trees | Radial or top-down |
| **Network** | System architecture | Force-directed |
| **Sequence** | API interactions | Vertical timeline |
| **ERD** | Database design | Boxes and lines |
| **Mind Map** | Brainstorming | Radial from center |
| **Venn** | Overlapping concepts | Overlapping circles |
| **SWOT** | Analysis | 2x2 grid |

## Node Styles

| Node Type | Shape | Use Case |
|-----------|-------|----------|
| Process | Rounded rectangle | Actions/steps |
| Decision | Diamond | Yes/no questions |
| Terminal | Stadium/oval | Start/end points |
| Data | Parallelogram | Input/output |
| Database | Cylinder | Storage |
| External | Rectangle (bold border) | External systems |

## Connection Rules

| Connection | Style | Meaning |
|------------|-------|---------|
| Solid arrow | → | Flow/sequence |
| Dashed arrow | ⇢ | Optional/conditional |
| Solid line | — | Association |
| Dashed line | ╌ | Dependency |
| Thick arrow | ═> | Primary flow |
| Bidirectional | ↔ | Two-way relationship |

## Layout Algorithms

| Algorithm | Best For | Characteristics |
|-----------|----------|-----------------|
| Hierarchical | Trees, org charts | Clear parent-child |
| Force-directed | Networks | Organic spacing |
| Circular | Cyclic processes | Ring layout |
| Grid |矩阵, comparisons | Aligned rows/columns |
| Radial | Central concepts | Star pattern |

## Animation Rules

| Animation | Duration | Use Case |
|-----------|----------|----------|
| Sequential build | 0.3s per node | Step-by-step reveal |
| Connection draw | 0.2s | Link animation |
| Node pop | 0.15s | Emphasis |
| Subtree reveal | 0.5s | Branch expansion |
| Highlight path | 0.3s | Flow tracing |

## Color Coding

| Element | Color | Meaning |
|---------|-------|---------|
| Start | Green (#4CAF50) | Entry point |
| End | Red (#F44336) | Exit point |
| Process | Blue (#2196F3) | Actions |
| Decision | Orange (#FF9800) | Branches |
| Data | Purple (#9C27B0) | I/O |
| External | Gray (#607D8B) | External systems |

## Prompt Template

```
[Diagram type] of [system/concept]:
- Nodes: [count] elements
- Connections: [relationship types]
- Layout: [algorithm]
- Animation: [build type]
- Style: [color scheme]
```

## Integration with Domains

### Software Architecture
- Use network/hierarchy layout
- Color by system boundary
- Include data flow arrows
- Label protocols/data formats

### Business Processes
- Flowchart layout
- Swim lanes for roles
- Decision diamonds prominent
- Include metrics at nodes

### Education
- Mind map for concepts
- Simple, large nodes
- Step-by-step build
- Verbal narration sync

### Science
- ERD for data models
- Sequence for interactions
- Include legends
- Technical accuracy first

## Quality Checklist

- [ ] Nodes don't overlap
- [ ] Connections clearly directed
- [ ] Labels readable
- [ ] Hierarchy clear
- [ ] Legend included
- [ ] Colorblind-safe palette
