import { useStore } from '@/stores/uiStore';

export default function Sample() {
  const bears = useStore((state) => state.bears)
  return <h1>{bears} bears around here...</h1>
}