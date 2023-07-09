<script lang="ts">
  import type { PageData } from "./$types";
	export let data: PageData;

  let title = "Why Should You Buy 30 Shares of FakeStock123";
  let author = "John Smtih";
  let created = "7/6/2023";
  let comments = [
    {author: "FakeUser2", created: "7/6/2023", content: "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Expedita, rerum?"},
    {author: "StockExpert", created: "7/6/2023", content: "Hic recusandae labore id repellat reiciendis illum suscipit, in, vero et inventore at, ratione quae. Sed, atque amet? Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa assumenda quis error similique. Facere laboriosam quia non vel reiciendis dolores. Commodi, pariatur non tenetur nobis recusandae est libero blanditiis ullam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam dicta veniam dolore provident expedita nobis quae nisi explicabo, est eos perspiciatis numquam error eum earum qui accusantium odit, iste fugiat."},
    {author: "User1234", created: "7/6/2023", content: "Non excepturi delectus deleniti!"}
  ]
</script>

<div id="main-container">
  <h1>"{title}"</h1>
  <h3 id="byline">Created by {author} on {created}</h3>
  <br />
  <div id="secondary-container">
    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Expedita, rerum? Sed, voluptas officiis. Iste, laudantium non ab enim voluptatum suscipit voluptatem? Reprehenderit velit saepe eum unde ratione nobis perferendis non. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Alias corporis accusamus harum aut eos voluptate, exercitationem repellat officia quo veniam nobis officiis fugit dicta deserunt ducimus aperiam placeat at quibusdam.</p>
    <br />
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique sit possimus excepturi corporis doloremque minima praesentium reprehenderit quas aliquid. Labore odio maiores saepe animi modi reiciendis obcaecati unde sequi autem. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nostrum in sapiente quibusdam asperiores unde, enim ex debitis repudiandae accusantium nemo facilis, quam incidunt laborum facere nesciunt sunt consequatur aperiam consectetur!</p>
    <br /> 
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Non excepturi delectus deleniti! Hic recusandae labore id repellat reiciendis illum suscipit, in, vero et inventore at, ratione quae. Sed, atque amet? Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa assumenda quis error similique. Facere laboriosam quia non vel reiciendis dolores. Commodi, pariatur non tenetur nobis recusandae est libero blanditiis ullam! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam dicta veniam dolore provident expedita nobis quae nisi explicabo, est eos perspiciatis numquam error eum earum qui accusantium odit, iste fugiat.</p>
    <br />
  </div>
  <h1>Comments</h1>
  <br />
  {#if comments.length == 0} 
  <p>There are no comment</p>
  {:else}
    {#each comments as c}
    <div class="comment">
      <p>{c.author}</p>
      <p>{c.created}</p>
      <br />
      <p>{c.content}</p>
    </div>
    {/each}
  {/if}
</div>

<style>
  #main-container {
    width: 90%;
    margin: auto;
    padding-top: 1em;
  }

  #byline {
    padding-left: 1em;
  }

  #secondary-container {
    width: 95%;
    margin: auto;
  }

  .comment {
    border: 1px solid black;
    border-radius: 15px;
    padding: 1em;
    margin: 1em;
  }
</style>