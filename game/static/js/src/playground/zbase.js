class AcGamePlayground {
    constructor(root) {
        this.root = root;
        this.$playground = $(`<div>GAME</div>`);

        this.hide();
        this.root.$ac_game.append(this.$playground);

        this.start();
    }

    start() {
    }

    show(){
        this.$playground.show();
    }

    hide() {
        this.$playground.hide();
    }
}
