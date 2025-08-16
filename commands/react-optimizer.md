# React Performance Optimizer

Analyze the provided React code and identify optimization opportunities across these key areas:

## � Component Optimization
- **Re-renders**: Implement React.memo, useMemo, useCallback to prevent unnecessary renders
- **State Management**: Optimize useState placement, avoid over-nesting state
- **Component Splitting**: Break large components into smaller, focused units
- **Lazy Loading**: Use React.lazy() and Suspense for code splitting

## = Hooks & State
- **Custom Hooks**: Extract reusable logic, reduce component complexity
- **Effect Dependencies**: Optimize useEffect dependency arrays, prevent infinite loops
- **State Colocation**: Move state closer to where it's used
- **Context Optimization**: Split contexts to avoid unnecessary re-renders

## =� Data & Lists
- **Virtualization**: Use react-window/react-virtualized for large lists
- **Keys**: Ensure stable, unique keys for list items
- **Data Fetching**: Implement proper loading states, error boundaries
- **Memoization**: Cache expensive computations and object references

## <� Rendering Performance
- **Bundle Analysis**: Identify and eliminate unused dependencies
- **Image Optimization**: Implement lazy loading, responsive images
- **CSS-in-JS**: Optimize styled-components, emotion performance
- **Profiling**: Use React DevTools Profiler to identify bottlenecks

## =' Development Patterns
- **Error Boundaries**: Implement comprehensive error handling
- **Prop Drilling**: Replace with Context API or state management
- **Side Effects**: Properly handle async operations and cleanup
- **Testing**: Ensure optimizations don't break functionality