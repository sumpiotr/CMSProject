<script>
    export let data;

    import Carousel from "svelte-carousel";
    import { _getCurrentPageIndexByCurrentParticleIndexInfinite } from "svelte-carousel/src/utils/page";
    import SliderItem from "./SliderItem.svelte";

    console.log("slider images: ", data.images);

    let images = new Array(data.images.length);

    console.log(data);

    for (let i = 0; i < data.images.length; i++) {
        fetch("/getImg", {
            method: "POST",
            body: JSON.stringify({ filename: data.images[i].image }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.blob())
            .then((imageBlob) => {
                // Then create a local URL for that image and print it
                const imageObjectURL = URL.createObjectURL(imageBlob);
                console.log(imageObjectURL);

                images[i] = imageObjectURL;
            });
    }
</script>

{#if data.autoplay == true}
    <Carousel autoplay autoplayDuration={data.duration * 1000} pauseOnFocus>
        {#each data.images as _, i}
            <SliderItem image={images[i]} text={data.descriptions[i]} color={data.color} backgroundColor={data.backgroundColor} />
        {/each}
    </Carousel>
{:else}
    <Carousel>
        {#each data.images as _, i}
            <SliderItem image={none[i]} text={data.descriptions[i]} color={data.color} backgroundColor={data.backgroundColor} />
        {/each}
    </Carousel>
{/if}
