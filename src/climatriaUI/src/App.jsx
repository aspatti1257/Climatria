import { useState } from "react";
import Header from "./components/Header";
import Home from "./pages/Home";
import Footer from "./components/Footer";

function App() {
  const [isUnsubscribing, setIsUnsubscribing] = useState(false);

  const VITE_BASE_URL = import.meta.env.VITE_BASE_URL;

  return (
    <>
      <Header />
      <Home
        isUnsubscribing={isUnsubscribing}
        setIsUnsubscribing={setIsUnsubscribing}
        VITE_BASE_URL={VITE_BASE_URL}
      />
      <Footer setIsUnsubscribing={setIsUnsubscribing} />
    </>
  );
}

export default App;
