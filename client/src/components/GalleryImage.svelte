<script>
    export let data;
    import Paper from "@smui/paper";

    let image = "https://dummyimage.com/600x360";

    fetch("/getImg", {
        method: "POST",
        body: JSON.stringify({ filename: data.image }),
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((response) => response.blob())
        .then((imageBlob) => {
            const imageObjectURL = URL.createObjectURL(imageBlob);
            image = imageObjectURL;
        });
</script>

<div class="lg:w-1/3 sm:w-1/2 p-4">
    <div class="flex relative">
        <img alt="gallery" class="absolute inset-0 w-full h-full object-cover object-center" src={image} />
        <div class="px-8 py-10 relative z-10 w-full border-4 border-gray-200 bg-white opacity-0 hover:opacity-95">
            <!-- <h2 class="tracking-widest text-sm title-font font-medium text-indigo-500 mb-1">THE SUBTITLE</h2> -->
            <h1 class="title-font text-lg font-medium text-gray-900 mb-3">{data.title}</h1>
            <p class="leading-relaxed">{data.description}</p>
        </div>
    </div>
</div>
