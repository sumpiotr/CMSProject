<script>
    import Article from "./Article.svelte";

    export let data;
</script>

<section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-wrap -m-4">
            {#each data.children as child}
                <Article data={child} />
            {/each}
        </div>
    </div>
</section>
