import Heading from '../components/Heading'
import Content from '../components/Content'

const DataMethodologyPage = () => {
  return (
    <section className="section">
      <div className="container">
        <header className="block mb-3">
          <Heading size={1} className="is-family-primary has-text-black">
            Data Methodology
          </Heading>
          <Content size={5} className="is-family-secondary has-text-black p-5"></Content>
        </header>
        <main className="block mb-3">
          <Content size={5} className="is-family-secondary has-text-black p-5"></Content>
        </main>
        <footer className="block mb-3">
          <Content size={5} className="is-family-secondary has-text-black p-5"></Content>
        </footer>
      </div>
    </section>
  )
}

export default DataMethodologyPage
