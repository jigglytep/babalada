<script lang="ts">
  import type { PageData } from "./$types";
	export let data: PageData;

  let comments = [
    {user: "StockExpert", content: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequatur totam est corrupti!"},
    {user: "John Smith", content:  "Illo, perferendis atque delectus cupiditate praesentium dignissimos repellat reprehenderit."},
    {user: "StockPresident", content: "Ratione iusto ipsam doloribus adipisci maxime officiis nesciunt sint totam at dolores?"},
    {user: "MrStocks", content: "Lorem ipsum dolor sit amet consectetur, adipisicing elit."},
    {user: "StockTrader1000", content: "Recusandae obcaecati nemo harum fuga neque eligendi similique illum mollitia ducimus, nostrum provident exercitationem qui amet"}
  ]

</script>

<div id="main-container">
  <div id="forum">
    <h1>{data.slug}</h1>
    <h3>Posted on 7/11/2023 by BabaladaUser1</h3>
    <br />
    <div id="content">
      <h3>Repellendus Necessitatibus</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Consequatur totam est corrupti voluptate quidem minus rem, cupiditate quod ea, exercitationem mollitia eius, esse non at laudantium alias fugiat natus consectetur? Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit nisi incidunt cupiditate. Officia est aperiam unde distinctio voluptates ab iusto maiores fugiat autem nostrum? Eaque dolorum molestias pariatur quae obcaecati. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus a laborum libero ipsam itaque aliquam ea, sed saepe asperiores aperiam alias, ratione reprehenderit dolorum quidem est ad perferendis delectus. Deleniti.</p>
      <br />
      <h3>Consectetur Adipisicing Elit</h3>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis eum, esse enim qui ut in minus eaque quos rem nulla. Reprehenderit veniam, fuga voluptas totam laboriosam maiores ipsa odit asperiores. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum, id, voluptatum culpa ducimus nisi blanditiis sequi adipisci excepturi illum, facere vitae harum enim sit ex. Provident rerum sit consectetur ipsa! Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolor quaerat ea asperiores accusamus, sit soluta quibusdam dolorum rerum. Dicta consequuntur esse veritatis voluptas adipisci mollitia rerum porro qui tempora id. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Saepe eius distinctio ducimus, molestias id voluptatum reprehenderit eum sit dicta, veniam consequatur eligendi tenetur mollitia, reiciendis repellendus quis maiores. Expedita, laudantium. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia, libero ipsam quos, eveniet ipsum fugit cupiditate dicta ullam, consectetur quasi quae amet facere culpa accusamus assumenda rerum at. Quam, facilis!</p>
      <br />
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo, perferendis atque delectus cupiditate praesentium dignissimos repellat reprehenderit ratione iusto ipsam doloribus adipisci maxime officiis nesciunt sint totam at dolores Lorem ipsum dolor sit amet consectetur, adipisicing elit. Recusandae obcaecati nemo harum fuga neque eligendi similique illum mollitia ducimus, nostrum provident exercitationem qui amet. Temporibus dolorem quasi fugit. Dolorum, dolore.</p>
  </div>
  </div>
  <div id="comments-container">
    <h1>Comments</h1>
    {#each comments as c}
      <div class="comment">
        <div class="comment-content">
          <h3>User: {c.user}</h3>
          <br />
          <p>{c.content}</p>
        </div>
      </div>
    {/each}
  </div>
</div>

<style lang="scss">
  #main-container {
    width: 90%;
    margin: auto;
    margin-bottom: 0;
    padding: 1em 1em 1em 0;
  }

  #forum {
    border: 2px solid black;
    border-radius: 15px;
    box-shadow: 3px 3px black;
    padding: .75em;
  }

  #comments-container {
    border: 2px solid black;
    border-radius: 15px;
    box-shadow: 3px 3px black;
    h1 {
      padding: .25em .75em .25em .75em;
    }
  }

  
  #content{
    h3 {
      padding-bottom: .25em;
    }
    p {
      text-indent: 2em;
    }
  }

  .comment {
    border: 1px solid black;
  }

  .comment-content{
    padding: 1em;
  }
</style>