import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Layout from './components/Layout'
import InteractivePCA from './pages/InteractivePCA'
import DataMethodology from './pages/DataMethodology'
import 'bulma/css/bulma.min.css'

const App = () => {
     return (
          <BrowserRouter>
               <Routes>
                    <Route path="/" element={<Layout />}>
                         <Route
                              index
                              element={
                                   <Navigate
                                        to="/interactive-pca"
                                        replace
                                   />
                              }
                         />
                         <Route
                              path="interactive-pca"
                              element={<InteractivePCA />}
                         />
                         <Route
                              path="data-methodology"
                              element={<DataMethodology />}
                         />
                    </Route>
               </Routes>
          </BrowserRouter>
     )
}

export default App
