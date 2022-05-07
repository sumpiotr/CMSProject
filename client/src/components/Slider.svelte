<script>
    export let data;
</script>


<div class="slider">
    {data.text}
</div>

<style>
    .slider {
        height: 300px;
        width: auto;
        background-color: green;
    }
</style>


<!--
    <script>
    let src = "img/slider-img-1.jpg"
</script>

<img src="./img/slider-img-1.jpg" alt="jpg1" class="d-block w-100">

<img src={src} alt="test">
<img src="img/slider-img-1.jpg" alt="test">
-->


<!-- Carousel -->
<!-- 
<div class="container-fluid px-0">
    <div class="carousel slide" id="slider" data-ride="carousel" data-interval="20000" data-pause="hover">

        <ol class="carousel-indicators d-none d-md-inline-flex">
            <li data-target="#slider" data-slide-to="0" class="active"></li>
            <li data-target="#slider" data-slide-to="1"></li>
            <li data-target="#slider" data-slide-to="2"></li>
        </ol>

        <div class="carousel-inner "> 
            <div class="carousel-item active">
                <img src="./img/slider-img-1.jpg" alt="jpg1" class="d-block w-100">

                <div class="carousel-caption">
                    <h2 class="display-4">Slide1</h2>
                    <p class="h4">Slide1 Slide1 Slide1</p>
                    <div class="d-none d-md-block">
                        <button type="button" class="btn btn-lg btn-outline-light mr-2 mt-3">Button1</button>
                        <button type="button" class="btn btn-lg btn-primary ml-2 mt-3">Button2</button>
                    </div>

                </div>
            </div>
            <div class="carousel-item">
                <img src="./img/slider-img-2.jpg" alt="jpg2" class="d-block w-100">
            </div>
            <div class="carousel-item">
                <img src="./img/slider-img-3.jpg" alt="jpg3" class="d-block w-100">
            </div>
        </div>

        <a href="#slider" class="carousel-control-prev d-none d-md-flex" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon"></span>
        </a>

        <a href="#slider" class="carousel-control-next d-none d-md-flex" role="button" data-slide="next">
            <span class="carousel-control-next-icon"></span>
        </a>
    </div>

   
</div>

<!-- /Carousel -->

<!-- <style>
    /* Carousel */

    * {
    scroll-behavior: smooth;
    }

    .carousel-indicators li {
        color: azure;
    }

    .carousel-caption {
        position: absolute;
        top: 30%;
        transform: translateY(-50%);
    }

    .carousel-caption h2, .carousel-caption h2 {
        text-shadow: 3px 2px 4px black;
    }

    .carousel-caption h2.display-4 {
        font-size: 150%;
        font-weight: 500;
    }

    .btn-primary {
        background-color: #0c86cc;
        border-color: #0e78be;
    }

    .btn-primary:hover {
        background-color: #0f6197;
        border-color: #09598f;
    }

    .carousel-caption button {
        box-shadow: 3px 2px 4px rgba(0, 0, 0, 0.4);
    }

    .carousel-caption .btn-outline-light {
        box-shadow: 3px 2px 4px rgba(0, 0, 0, 0.4);
    }

    .carousel-caption .btn-outline-light:hover {
        box-shadow: none;
    }

    @media (min-width: 576px) {
        .carousel-caption {
            top: 40%;
        }

        .carousel-caption h2.display-4 {
            font-size: 350%;
        }
    }

    @media (min-width: 768px) {
        .carousel-caption {
            top: 45%;
        }

        .carousel-caption h2.display-4 {
            font-size: 400%;
        }
    }

    @media (min-width: 992px) {
        .carousel-caption {
            top: 45%;
        }

        .carousel-caption h2.display-4 {
            font-size: 500%;
        }
    }

    @media (min-width: 1200px) {
        .carousel-caption {
            top: 50%;
        }

        .carousel-caption h2.display-4 {
            font-size: 600%;
        }
    }
</style> -->