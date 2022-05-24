<script>
    import Article from "./Article.svelte";

    export let data;
    export let articles = [];

    console.log(articles);
    function getIndex(child, index) {
        return articles.length > 0 ? articles.indexOf(child) : index;
    }
</script>

<section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-wrap -m-4">
            {#each data.children as child, index}
                <Article data={child} colors={data} index={getIndex(child, index)} />
            {/each}
        </div>
    </div>
</section>
