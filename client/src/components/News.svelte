<script>
    export let data;

    let image = "";
    fetch("/getImg", {
        method: "POST",
        body: JSON.stringify({ filename: data.images[0].image }),
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

<div style="--color: {data.color}; --backgroundColor: {data.backgroundColor}">
    <div class="news">
        <div class="textNews">
            <div class="title">
                <p>{data.title}</p>
            </div>
            <div class="text">
                <p>{data.text}</p>
            </div>
        </div>
        <div class="img">
            <img src={image} alt="img" width="500" height="500" />
        </div>
    </div>
</div>

<style>
    .news {
        height: 500px;
        width: auto;
        position: relative;

        color: var(--color);
        background-color: var(--backgroundColor);

        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    .title {
        font-size: 24px;
        font-weight: 500;

        margin-bottom: 15px;
    }

    .text {
    }

    .textNews {
        height: 500px;
        width: calc(100vw - 500px);
        position: relative;
        margin-left: -500px;

        color: var(--color);
        background-color: var(--backgroundColor);

        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    .img {
        width: 500px;
        height: 500px;
        background-color: #fff9e8;
        position: absolute;
        right: 0px;
        top: 0px;

        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
