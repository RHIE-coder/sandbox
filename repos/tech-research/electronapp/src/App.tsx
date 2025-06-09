import Sample from "@/components/Sample"
 
function App() {

  const versions = window.electron.doThing()



  return (
    <>
      <h1>{ctxmsg}</h1>
      <h1>{versions.randomGenerator()}</h1>
      <Sample />
    </>
  )
}
 
export default App;