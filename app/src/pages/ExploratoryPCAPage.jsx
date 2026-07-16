import Heading from '../components/Heading'
import Content from '../components/Content'
import PCA from '../components/PCA'

const ExploratoryPCAPage = () => {
  return (
    <section className="section">
      <div className="container">
        <header className="block mb-3">
          <Heading size={1} className="is-family-primary has-text-black">
            Music Preferences and Feelings
          </Heading>
          <Content size={5} className="is-family-secondary has-text-black p-5">
            Examine the relationship between music preferences and the construction of feelings through <span className="is-italic">Principal Component Analysis (PCA)</span>. The{' '}
            <span className="is-italic">Exploratory PCA</span> visualizes how different songs cluster according to similar scaled sonic and emotional characteristics. 12 unique scaled sonic values are
            processed to build the <span className="is-italic">PCA</span> coordinates for each song. Additionally, <span className="is-italic">Russell's Core Affect Framework</span> is leveraged to
            understand how different types and extents of valence and arousal contribute to the formation of feelings when listening to each song. The{' '}
            <span className="is-italic">Exploratory PCA</span> offers a comprehensive tooltip to explore all data points and their corresponding song attributes.{' '}
            <span className="is-italic">Russell's Core Affect Framework</span> maps each <span className="is-italic">Primary Feeling</span> into one of four neurophysiological quadrants depending on
            the particular manifestation of valence and arousal. Each quadrant is color-coded as{' '}
            <span
              style={{
                color: 'rgb(200, 180, 0)',
              }}
            >
              ■ Quadrant 1 (High Arousal + Positive Valence)
            </span>
            ,{' '}
            <span
              style={{
                color: 'rgb(255,0,0)',
              }}
            >
              ■ Quadrant 2 (High Arousal + Negative Valence)
            </span>
            ,{' '}
            <span
              style={{
                color: 'rgb(0,0,255)',
              }}
            >
              ■ Quadrant 3 (Low Arousal + Negative Valence)
            </span>
            , and{' '}
            <span
              style={{
                color: 'rgb(0, 180, 0)',
              }}
            >
              ■ Quadrant 4 (Low Arousal + Positive Valence)
            </span>
            . Observe that a subset of songs is associated with a <span className="is-italic">Primary Feeling</span> mapping to a <span className="is-italic">Core Affect Quadrant</span> that differs
            from the surrounding spatial quadrant in the <span className="is-italic">Exploratory PCA</span>. Although <span className="is-italic">My Sacrifice</span> by{' '}
            <span className="is-italic">Creed</span> is associated with a <span className="is-italic">Core Affect Quadrant</span> equal to Quadrant 1, the scatter point is spatially located in
            Quadrant 3 in the <span className="is-italic">Exploratory PCA</span>. This occurrence presents an opportunity to (1) consider why some songs are associated with a particular{' '}
            <span className="is-italic">Core Affect Quadrant</span> but mathematically cluster to a different spatial quadrant in the <span className="is-italic">Exploratory PCA</span>, and (2)
            consider why some respondents experience a particular <span className="is-italic">Primary Feeling</span> when listening to a song.
          </Content>
        </header>
        <main className="box has-background-white-bis p-5 mb-3">
          <div className="is-flex is-justify-content-center is-align-items-center">
            <PCA />
          </div>
        </main>
        <footer className="block mb-3">
          <Content size={5} className="is-family-secondary has-text-black p-5">
            Main Conclusions
          </Content>
        </footer>
      </div>
    </section>
  )
}

export default ExploratoryPCAPage
