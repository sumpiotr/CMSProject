<script>
    import GalleryImage from "../GalleryImage.svelte";

    export let data;
</script>

<section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-wrap -m-4">
            {#each data.images as image}
                <GalleryImage data={image} />
            {/each}
        </div>
    </div>
</section>
