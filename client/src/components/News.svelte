<script>
    export let data;
</script>

<div style="--color: {data.color}; --backgroundColor: {data.backgroundColor}">
    <div class="news">
        <div class="title">
            <p>{data.title}</p>
        </div>
        <div class="text">
            <p>{data.text}</p>
        </div>
        <div class="img">
            img
        </div>
    </div>
</div>

<style>
    .news {
        height: 300px;
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

    .img {
        width: 300px;
        height: 300px;
        background-color: #fff9e8;
        position: absolute;
        right: 0px;
        top: 0px;

        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>