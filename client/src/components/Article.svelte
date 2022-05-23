<script>
    export let data;
    export let index;
    export let colors;
</script>

<div class="p-4 lg:w-1/3">
    <div class="h-full bg-gray-100 bg-opacity-75 px-8 pt-16 pb-24 rounded-lg overflow-hidden text-center relative" style="background-color:{colors.backgroundColor};">
        <h1 class="title-font sm:text-2xl text-xl font-medium text-gray-900 mb-3" style="color:{colors.color};">{data.title}</h1>
        <h2>{data.category}</h2>
        <p class="leading-relaxed mb-3 max-h-32 overflow-hidden" style="color:{colors.color};">{data.text}</p>
        <a class="text-indigo-500 inline-flex items-center" href={"/" + index}
            >Learn More
            <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 12h14" />
                <path d="M12 5l7 7-7 7" />
            </svg>
        </a>
    </div>
</div>

<style>
</style>
