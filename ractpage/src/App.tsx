// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.tsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }


import { useState } from 'react';

const myVar = "hello world";

function MyButton() {

  const [count, setCount] = useState(0)
  
  function handleClick() {
    setCount(count+1)
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  )
}


function AdminPanel() {
  return (
    <h1>Admin Page</h1>
  )
}

function LoginForm() {
  return (
    <h1>Login Page</h1>
  )
}

const isLoggedIn = true;

const products = [
  {title: 'Cabbage', id: 1},
  {title: 'Garlic', id: 2},
  {title: 'Apple', id: 3},
]


function App() {
  

  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
      <h2>{myVar}</h2>
      <div>
      {
        isLoggedIn? (
          <AdminPanel />
        ) : (
          <LoginForm />
        )
      }
      </div>
      <ul>
        {
          products.map(product => 
            <li key={product.id}>
              {product.title}
            </li>
          )
        }
      </ul>
    </div>
  )
}

export default App
