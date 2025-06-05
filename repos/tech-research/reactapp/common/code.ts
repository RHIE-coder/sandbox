import {produce} from 'immer'

const baseState = [
    {
        titie: "learn typescript",
        done: true,
    },
    {
        title: "try immer",
        done: false
    }
]

const nextState = produce(baseState, draftState => {
    draftState.push({title: "tweet about it"})
    draftState[1].done = true
})

console.log(nextState)