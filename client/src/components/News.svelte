<script>
    export let data;
</script>

<div class="news">
    news
    {data.text}
    <div class="img">
        img
    </div>
</div>

<style>
    .news {
        height: 300px;
        width: auto;
        background-color: grey;
        position: relative;
    }

    .img {
        width: 300px;
        height: 300px;
        background-color: blue;
        position: absolute;
        right: 0px;
        top: 0px;
    }
</style>