export const data = [1,2,3,4];

export class Animal {
    constructor(type) {
        this.type = type;
    }

    makeNoise(sound = 'bark') {
        console.log(sound);
    }

    static return10() {
        return 10;
    }

    get metaData() {
        return `${this.type}`;
    }
}