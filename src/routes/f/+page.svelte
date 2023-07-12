<script>
    let names = [
        {title: "Why You Should Buy 30 Stocks of FakeStock123"},
        {title: "How To Learn To Trade Stocks"},
        {title: "Why Babalada Is The Best Stock Trading Website!!"},
        {title: "How The Stock Market Works"},
        {title: "Stock Trading Explain Like A 5-Year-Old Would Do"}
    ]
</script>

<div id="main-container">
    <section id="left-section">
        <div id="sticky">
            <h2 id="trending">Trending</h2>
            <h3 class="topic">Forums</h3>
            <div class="side-content">
                <ol>
                    <li>Why You Should Buy 30 Stocks of FakeStock123</li>
                    <li>FakeStock123? Best Stock Ever?</li>
                    <li>Don't Buy Shares of FakeStock123</li>
                    <li>Wasted My Life Savings on FakeStock123</li>
                    <li>Got 1000 Shares of FakeStock123</li>
                </ol>
            </div>
            <h3 class="topic">Topics</h3>
            <div class="side-content">
                <ol>
                    <li>#FakeStock123</li>
                    <li>#Babalada</li>
                    <li>#StockStories</li>
                    <li>#BestStockOf2023</li>
                    <li>#BestStockTrader</li>
                </ol>
            </div> 
        </div>
    </section>
    <main id="main-section">
        <div class="forum">
            <h2>Best Stocks Of 2023</h2>
            <h3>By StockExpert</h3>
            <p><small>Posted on 7/11/2023</small></p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
        </div>
        <div class="forum">
            <h2>How To Gain 1.3 Million Dollar Through Stocks</h2>
            <h3>John Smith</h3>
            <p><small>Posted on 7/8/2023</small></p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
        </div>
        <div class="forum">
            <h2>Recently Left My Job and Became Full-Time Stock Expect - These Are My Tips and Secerts</h2>
            <h3>By FullTimeStocker</h3>
            <p><small>Posted on 7/5/2023</small></p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
            <br />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum ex perspiciatis odit quo maxime consectetur inventore pariatur veritatis nostrum ducimus vero, architecto velit totam sint quia! Voluptates est quisquam aliquam.</p>
        </div>
    </main>
    <section id="right-section">
        <div id="sticky">
            <h2 class="topic">Your Forums</h2>
            <div class="side-content">
                <ol>
                    {#each names as n}
                        <li><a href="f/{n.title}">{n.title}</a></li>
                    {/each}
                </ol>
            </div>
        </div>
    </section>
</div>


<style>
    #main-container {
        display: grid;
        grid-template-columns: 25% 50% 25%;
        min-height: 88.25vh;
    }

    #left-section {
        grid-column: 1 / 2;
        border: 1.5px solid black;
    }

    #main-section {
        grid-column: 2 / 3;
        border: 1.5px solid black;
    }

    #right-section{
        grid-column: 3 / 4;
        border: 1.5px solid black;
        }

    #trending {
        text-align: center;
        padding-top: .5em;
    }

    .topic {
        text-align: center;
        padding-top: .5em;
        padding-bottom: .5em;
    }

    .forum {
        height: auto;
        width: auto;
        background-color: lightgrey;
        border-radius: 15px;
        margin: 2em 6em;
        padding: .75em;
    }

    #sticky {
        position:sticky;
        top: 0;
        border-top: 1.5px solid black;
    }

    .side-content {
        padding-left: 2em;
        padding-right: 2em;
    }

    li a:link, a:visited, a:hover {
    color: blue;
    text-decoration: none;
  }
</style>