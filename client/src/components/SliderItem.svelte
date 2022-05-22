<script>
    export let image, text, color, backgroundColor
</script>

<div
    class="color-container"
    style="background-image: url('{image}'); color: {color}; background-color: {backgroundColor};"
>
    <p>{text}</p>
</div>

<style>
    .color-container {
        height: 500px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        user-select: none;

        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
    }
    .color-container > p {
        font-size: 24px;
        font-weight: 500;
    }
</style>
  