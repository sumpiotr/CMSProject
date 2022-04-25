import Menu1 from "./components/Menu1.svelte";
import Articles from "./components/Articles.svelte";

export class ComponentManager {
    static getComponentByName(name) {
        switch (name) {
            case "Menu1":
                return Menu1;
            case "Articles":
                return Articles;
            default:
                return null;
        }
    }
}
