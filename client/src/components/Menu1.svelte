<script>
    export let data;
    export let logged;
    export let admin;
    export let name;
    export let logo;

    let image = "";
    fetch("/getImg", {
        method: "POST",
        body: JSON.stringify({ filename: logo }),
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((response) => response.blob())
        .then((imageBlob) => {
            // Then create a local URL for that image and print it
            const imageObjectURL = URL.createObjectURL(imageBlob);
            console.log(imageObjectURL);

            image = imageObjectURL;
        });
</script>

<header class="text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
            <img src={image} />
            <span class="ml-3 text-xl">{name}</span>
        </a>
        <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
            {#each data as child}
                {#if (child.login == 1 && !logged) || (child.login == 2 && logged) || child.login == 0}
                    {#if (child.admin == 1 && !admin) || (child.admin == 2 && admin) || child.admin == 0}
                        <a class="mr-5 hover:text-gray-900" href="/{child.path}">{child.pageName}</a>
                    {/if}
                {/if}
            {/each}
        </nav>
    </div>
</header>
