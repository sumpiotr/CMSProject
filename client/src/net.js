export class Net {
    static updatePage(fullData) {
        fetch("./savePage", {
            method: "POST",
            body: JSON.stringify({ newData: fullData }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                console.log("updated", d);
            });
    }
}
